import unittest
import sys

in_s = { 'children': 3,
          'cats': 7,
          'samoyeds': 2,
          'pomeranians': 3,
          'akitas': 0,
          'vizslas': 0,
          'goldfish': 5,
          'trees': 3,
          'cars': 2,
          'perfumes': 1 }

def read_aunts( instr ):

  aunts = []
  for line in instr.split('\n'):
    l = line.replace(':','').replace(',','').split()
    things = {}
    things[l[2]] = int(l[3])
    things[l[4]] = int(l[5])
    things[l[6]] = int(l[7])
    aunts.append(things)

  return aunts

def filt_aunts( aunts ):
 
  for a in range(len(aunts)):
    if all(in_s[k] == v for k,v in aunts[a].items()):
      return a+1, aunts[a]

def filt_aunts2( aunts ):
  for a in range(len(aunts)):
    p = []
    for k,v in aunts[a].items():
      if (k == 'cats' or k == 'trees') and v > in_s[k]:
        p.append(aunts[a])
      elif (k == 'pomeranians' or k == 'goldfish') and v < in_s[k]:
        p.append(aunts[a])
      elif k not in ['cats','trees','pomeranians','goldfish'] and v == in_s[k]:
        p.append(aunts[a])
    if len(p) == 3:
      return a+1, aunts[a]
  

class TestFuncs(unittest.TestCase):

  def test_(self):
    pass
    #self.assertEqual( )

if __name__ == '__main__':
  if len(sys.argv) == 2:

    aunts = read_aunts(sys.argv[1])
    a, items = filt_aunts( aunts )
    print(a, items)
    a, items = filt_aunts2( aunts )
    print(a, items)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
