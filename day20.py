import unittest
import sys
import numpy as np

def visit_houses(N, count=10, m=None):
  """ Calculates the number of presents delivered to each house starting from
      house 1. Returns the house number and number of presents delivered to it
      once the threshold is hit """
  m = N//10 if m is None else m
  houses = np.zeros(N//10, dtype=np.int)
  for i in range(1, N//10):
    for j in range(i, min(i+m*i, N//10), i):
      houses[j] += (i)*count
    if houses[i] >= N:
      return i, houses[i]
  return 0

class TestFuncs(unittest.TestCase):

  def test_visit_houses(self):
    self.assertTrue( visit_houses(120), (6, 120))

if __name__ == '__main__':
  if len(sys.argv) == 2:
    n = int(sys.argv[1])
    h, p = visit_houses(n)
    print('House {} has {} presents'.format(h,p))
  if len(sys.argv) == 4:
    n = int(sys.argv[1])
    c = int(sys.argv[2])
    m = int(sys.argv[3])
    h, p = visit_houses(n, c, m)
    print('House {} has {} presents'.format(h,p))
    
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
