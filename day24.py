import unittest
import sys
import itertools
import functools

def read_presents( instr ):
  p = [ int(l) for l in instr.split('\n') ]
  return p

def QE(l):
  return functools.reduce( lambda x,y: x*y, l)

def fit( p, n ):
  size = sum(p)//n
  for i in range(len(p)):
    comb = [ QE(c) for c in itertools.combinations(p, i) if sum(c) == size ]
    if len(comb) > 0:
      return min(comb)
        

class TestFuncs(unittest.TestCase):

  def test_QE(self):
    self.assertEqual( QE( [11, 9] ), 99 )
    self.assertEqual( QE( [10, 8, 2] ), 160 )
    self.assertEqual( QE( [10, 4 , 3, 2, 1] ), 240 )

  def test_fit(self):
    p = [1,2,3,4,5,7,8,9,10,11]
    self.assertEqual( fit( p, 3 ), 99 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    p = read_presents( sys.argv[1])
    q = fit( p, 3 )
    print('Minimum QE in 3 groups:', q)
    q = fit( p, 4 )
    print('Minimum QE in 4 groups:', q)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
