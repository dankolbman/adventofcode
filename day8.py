import unittest
import sys

def string_literal( instr ):
  """ Returns the length of the string literal """
  # Should contain enclosing quotes from the input
  return len(instr)

def string_memory( instr ):
  """" Returns the number of characters stored in memory """
  # Take off 2 for the strings
  return len(instr.encode('utf-8').decode('unicode_escape'))-2

def string_encode( instr ):
  """ Returns the number of characters in the re-encoded string """
  # Add two for wrapping it in a new string
  return len(instr.replace('\\', '\\\\').replace('"','\\"')) + 2

class TestFuncs(unittest.TestCase):

  def test_string_literal(self):
    self.assertEqual( string_literal(r'""'), 2 )
    self.assertEqual( string_literal(r'"abc"'), 5 )
    self.assertEqual( string_literal(r'"aaa\"aaa"'), 10 )
    self.assertEqual( string_literal(r'"\x27"'), 6 )

  def test_string_memory(self):
    self.assertEqual( string_memory(r'""'), 0 )
    self.assertEqual( string_memory(r'"abc"'), 3 )
    self.assertEqual( string_memory(r'"aaa\"aaa"'), 7 )
    self.assertEqual( string_memory(r'"\x27"'), 1 )

  def test_string_encode(self):
    self.assertEqual( string_encode(r'""'), 6 )
    self.assertEqual( string_encode(r'"abc"'), 9 )
    self.assertEqual( string_encode(r'"aaa\"aaa"'), 16 )
    self.assertEqual( string_encode(r'"\x27"'), 11 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    lit_count = 0
    mem_count = 0
    enc_count = 0
    for line in sys.argv[1].split('\n'):
      lit_count += string_literal(line)
      mem_count += string_memory(line)
      enc_count += string_encode(line)

    print('Literals:', lit_count)
    print('In memory:', mem_count)
    print('Re-encoded:', enc_count)
    print('Memory difference:', lit_count-mem_count)
    print('Re-encoded difference:', enc_count-lit_count)

  elif len(sys.argv) == 3:
    print(sys.argv[2], 'Santas visited',
          num_visited(sys.argv[1], int(sys.argv[2])), 'houses')
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
