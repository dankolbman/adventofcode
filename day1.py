import unittest
import sys

def end_floor(moves):
  """ Returns the final floor after exectuting all the moves """
  return sum([ 1 if i == '(' else -1 for i in moves ])

def enter_basement(moves):
  """ Return the move number that move Santa into the basement
      Returns 0 if he never enters the basement """
  rsum = 0
  cmove = 1
  for move in moves:
    rsum += 1 if move == '(' else -1
    if rsum < 0:
      return cmove
    cmove += 1
  return 0

class TestFuncs(unittest.TestCase):
  def test_end_floor(self):
    self.assertEqual(end_floor('(())'), 0)
    self.assertEqual(end_floor('()()'), 0)
    self.assertEqual(end_floor('((('), 3)
    self.assertEqual(end_floor('(()(()('), 3)
    self.assertEqual(end_floor('))((((('), 3)
    self.assertEqual(end_floor('())'), -1)
    self.assertEqual(end_floor('))('), -1)
    self.assertEqual(end_floor(')))'), -3)
    self.assertEqual(end_floor(')())())'), -3)

  def test_enter_basement(self):
    self.assertEqual(enter_basement(')'), 1)
    self.assertEqual(enter_basement('()())'), 5)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    print( 'Final floor:', end_floor(sys.argv[1]) )
    print( 'Enters basement on floor', enter_basement(sys.argv[1]) )
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
