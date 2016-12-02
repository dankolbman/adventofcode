import unittest
import sys
import itertools

def sum_config( cfg, table ):
  """ Sums a given configuration's happiness """
  s = 0
  for i in range(-1,len(cfg)-1):
    s += table[cfg[i]][cfg[i+1]] + table[cfg[i]][cfg[i-1]]
  return s

def make_people( instr ):
  """ Makes a table of people represented by a dict of people each containing
      a dict of happiness values for their potential neighbors """
  people = {}

  for line in instr.split('\n'):
    l = line.replace('.','').split()
    if l[0] not in people:
      people[l[0]] = {}

    if l[-1] not in people[l[0]]:
      people[l[0]][l[-1]] = {}
    people[l[0]][l[-1]] = int(l[3])
    if l[2] == 'lose':
      people[l[0]][l[-1]] *= -1
  
  return people

def add_me( table ):
  """ Add's a passive 'Me' person to the table """
  print(table)
  table['Me'] = {}

  for k in table.keys():
    table[k]['Me'] = 0
    table['Me'][k] = 0

  return table

def max_happy( table ):
  """ Creates all permutations of a table and returns the max happiness """
  ppl = list(table.keys())

  perms = {}
  for c in itertools.permutations(ppl, len(ppl)):
    perms[c] = sum_config(c, table)

  return max(list(perms.values()))

class TestFuncs(unittest.TestCase):

  ppl = """Alice would gain 54 happiness units by sitting next to Bob.
      Alice would lose 79 happiness units by sitting next to Carol.
      Alice would lose 2 happiness units by sitting next to David.
      Bob would gain 83 happiness units by sitting next to Alice.
      Bob would lose 7 happiness units by sitting next to Carol.
      Bob would lose 63 happiness units by sitting next to David.
      Carol would lose 62 happiness units by sitting next to Alice.
      Carol would gain 60 happiness units by sitting next to Bob.
      Carol would gain 55 happiness units by sitting next to David.
      David would gain 46 happiness units by sitting next to Alice.
      David would lose 7 happiness units by sitting next to Bob.
      David would gain 41 happiness units by sitting next to Carol."""

  def test_make_people(self):
    self.assertEqual( make_people( self.ppl )['David']['Carol'], 41)  
    self.assertEqual( make_people( self.ppl )['Bob']['David'], -63)  

  def test_sum_config(self):
    table = make_people( self.ppl )
    self.assertEqual( sum_config(['David','Alice','Bob','Carol'], table), 330 )

  def test_max_happy(self):
    table = make_people( self.ppl )
    self.assertEqual( max_happy(table), 330 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    table  = make_people(sys.argv[1])
    m = max_happy( table )
    print('Maximum happiness:', m)
    table = add_me( table )
    m = max_happy( table )
    print('Maximum happiness with me:', m)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
