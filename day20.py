import unittest
import sys
import numpy as np

def visit_house(N):
  p = 0
  for j in range(1,N+1):
    if N%j == 0:
      p += j*10
  return p

class TestFuncs(unittest.TestCase):

  def test_visit_house(self):
    self.assertTrue( visit_house(6), 120)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    m = int(sys.argv[1])
    n = 800000
    p = visit_house(n)
    while p != m:
      n += 10
      p = visit_house(n)
    
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
