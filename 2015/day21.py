import unittest
import sys
import math

shop_str = '''Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Damage+1    25     1       0
Damage+2    50     2       0
Damage+3   100     3       0
Defense+1   20     0       1
Defense+2   40     0       2
Defense+3   80     0       3'''

weapons = []
armor = [[0,0,0]] # No armor set
rings = [[0,0,0],[0,0,0]] # No ring one for each finger

c = 0
for line in shop_str.split('\n'):
  if line == '':
    c += 1
    continue
  item = [ int(i) for i in line.strip().split()[1:] ]
  if c == 0:
    weapons.append(item)
  elif c == 1:
    armor.append(item)
  elif c == 2:
    rings.append(item)

def winning_comb( enemy, expensive=False):
  ''' Brute force all winning combos '''
  poss_comb = [] 
  # Try every weapon 
  for w in range(len(weapons)):
    # Try every armor (including no armor)
    for a in range(len(armor)):
      # Try all ring combinations
      for r1 in range(len(rings)):
        for r2 in range(len(rings)):
          if r1 != r2:
            if not expensive and can_win(enemy, weapons[w], armor[a], rings[r1], rings[r2]):
              poss_comb.append([weapons[w], armor[a], rings[r1], rings[r2]])
            elif expensive and not can_win(enemy, weapons[w], armor[a], rings[r1], rings[r2]):
              poss_comb.append([weapons[w], armor[a], rings[r1], rings[r2]])
              
  return poss_comb

def cheapest_comb( enemy, expensive=False ):
  ''' finds the most expensive combo if expensive is True '''
  w_comb = winning_comb( enemy, expensive )
  w_comb = sorted(w_comb, key=lambda x: x[0][0]+x[1][0]+x[2][0]+x[3][0],reverse=expensive)
  c = w_comb[0]
  return c[0][0] + c[1][0] + c[2][0] + c[3][0]

def can_win( enemy, w, a, r1, r2, hp=100 ):
  ''' determines if a player can win a fight with the given set of apperal '''
  dmg = w[1] + a[1] + r1[1] + r2[1]
  arm = w[2] + a[2] + r1[2] + r2[2]
  # The number of turns until the player dies
  turns = math.ceil(hp/max(enemy[1] - arm, 1))
  poss_dmg = max(dmg-enemy[2], 1)*turns
  # If the possible amount of damage is more than the enemies health
  return poss_dmg >= enemy[0]

class TestFuncs(unittest.TestCase):

  def test_can_win(self):
    enemy = [ 12, 7, 2 ]
    self.assertTrue( can_win( enemy, [0,5,0],[0,0,5],[0,0,0],[0,0,0], 8 ) )

if __name__ == '__main__':
  if len(sys.argv) == 4:
    enemy = [ int(sys.argv[1]) ,int(sys.argv[2]), int(sys.argv[3]) ]

    print('Cheapest winning cost: ', cheapest_comb(enemy) )
    print('Most expensive losing cost: ', cheapest_comb(enemy, True) )
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
