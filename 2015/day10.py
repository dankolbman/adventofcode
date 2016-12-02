import unittest
import sys

def next_seq( str_seq ):
  """ Produces the next number in the sequence """
  if len(str_seq) == 1:
    return '1' + str_seq[0]

  next_seq_str = ''
  c_char = str_seq[0]
  c_count = 0
  for c in str_seq:
    if c_char == c:
      c_count += 1
    else:
      next_seq_str += str(c_count)+c_char
      c_count, c_char = 1, c
  next_seq_str += str(c_count)+c_char

  return next_seq_str

class TestFuncs(unittest.TestCase):

  def test_next_seq(self):
    self.assertEqual( next_seq('1'), '11')
    self.assertEqual( next_seq('11'), '21')
    self.assertEqual( next_seq('21'), '1211')
    self.assertEqual( next_seq('1211'), '111221')
    self.assertEqual( next_seq('111221'), '312211')

if __name__ == '__main__':
  if len(sys.argv) == 2:
    in_seq = sys.argv[1]
    for i in range(50):
      in_seq = next_seq(in_seq)
    print(len(in_seq))
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
