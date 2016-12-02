import unittest
import sys
import numpy as np
import scipy.ndimage as ndimage

def next_seq(curr, cnr=False):
  old = curr
  footprint = np.array([[1,1,1],
                        [1,0,1],
                        [1,1,1]])

  sums= ndimage.generic_filter(curr, sum, footprint=footprint,
                              mode='constant', cval=0)
  curr = curr.flatten()
  sums = sums.flatten()

  for i in range(len(curr)):
    if curr[i] == 1:
      if sums[i] != 2 and sums[i] != 3:
        curr[i] = 0
    else:
      if sums[i] == 3:
        curr[i] = 1
  curr = curr.reshape(old.shape)
  if cnr:
    curr[0,0] = 1
    curr[0,-1] = 1
    curr[-1,0] = 1
    curr[-1,-1] = 1
  return curr

def read_seq(instr):
  instr = instr.replace('.','0').replace('#','1')
  seq = []
  for line in instr.split('\n'):
    seq.append(np.array( [ int(c) for c in line.strip() ] ))
  seq = np.array(seq)
  return seq

class TestFuncs(unittest.TestCase):

  def test_next_seq(self):
    instr = '''.#.#.#
               ...##.
               #....#
               ..#...
               #.#..#
               ####..'''
    seq = read_seq( instr )
    seq = next_seq(seq)
    seq = next_seq(seq)
    seq = next_seq(seq)
    seq = next_seq(seq)
    self.assertEqual( seq[0][0], 0)

if __name__ == '__main__':
  if len(sys.argv) == 3:
    seq = read_seq(sys.argv[1])
    for i in range(int(sys.argv[2])):
      seq = next_seq(seq)
    print('After {} steps:'.format(int(sys.argv[2])), sum(seq.flat))

    seq = read_seq(sys.argv[1])
    for i in range(int(sys.argv[2])):
      seq = next_seq(seq,True)
    print('With corners, after {} steps:'.format(int(sys.argv[2])), sum(seq.flat))
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
