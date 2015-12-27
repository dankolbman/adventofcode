import unittest
import sys
import math

# cost, damage, health, armor boost, mana boost, turns
spells = { 
  'missle'   : [ 53, 4, 0, 0, 0, 1 ],
  'drain'    : [ 73, 2, 2, 0, 0, 1 ],
  'shield'   : [ 113, 0, 0, 7, 0, 6 ], 
  'poison'   : [ 173, 3, 0, 0, 0, 6 ],
  'recharge' : [ 229, 0, 0, 0, 101, 5 ]
}
spells = [
  [ 53, 4, 0, 0, 0, 1 ],
  [ 73, 2, 2, 0, 0, 1 ],
  [ 113, 0, 0, 7, 0, 6 ], 
  [ 173, 3, 0, 0, 0, 6 ],
  [ 229, 0, 0, 0, 101, 5 ]
}

def next_turn(hp=10, mana=250, boss=13, dmg=8, curr_spells=[] ):
  
  # A losing turn
  if hp <= 0 or mana <= 0:
    return False

  # Begin turn
  atk = 0
  amr = 0
  for s in range(len(curr_spells)):
    dmg -= min(curr_spells[s][1], 1)
    hp += curr_spells[s][2]
    amr += curr_spells[s][3]
    mana += curr_spells[s][4]


  return curr_spells


def do_battles():
  
  

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
