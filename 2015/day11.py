import unittest
import sys
import re
import itertools
from operator import itemgetter

def is_valid(pwd):
  if 'i' in pwd or 'o' in pwd or 'l' in pwd:
    return False
  if len(re.findall(r'(\w)\1', pwd)) < 2:
    return False

  vals = [ ord(c) for c in pwd ]

  seqs = itertools.groupby(vals, key=lambda n, c=itertools.count(): n-next(c))
  lens = [ len(list(g)) for k,g in seqs]

  if max(lens) < 3:
    return False

  return True

def next_try(pwd):
  if 'i' in pwd:
    h, s, t = pwd.partition('i')
    pwd = h + 'j' + 'a'*len(t)
  if 'o' in pwd:
    h, s, t = pwd.partition('o')
    pwd = h + 'p' + 'a'*len(t)
  if 'l' in pwd:
    h, s, t = pwd.partition('l')
    pwd = h + 'm' + 'a'*len(t)

  # Shift recursively
  if pwd[-1] == 'z':
    return next_try(pwd[:-1]) + 'a'
  else:
    return pwd[:-1] + chr(ord(pwd[-1])+1)

def next_pwd(pwd):
  n_pwd = next_try(pwd)
  while not is_valid(n_pwd):
    n_pwd = next_try(n_pwd)

  return n_pwd

class TestFuncs(unittest.TestCase):

  def test_is_valid(self):
    self.assertFalse( is_valid('hijklmmn') )
    self.assertFalse( is_valid('abbceffg') )
    self.assertFalse( is_valid('abbcegjk') )
    self.assertTrue( is_valid('abcdffaa') )
    self.assertTrue( is_valid('ghjaabcc') )

  def test_next_pwd(self):
    self.assertEqual( next_pwd('abcdefgh'), 'abcdffaa')
    self.assertEqual( next_pwd('ghijklmn'), 'ghjaabcc' )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    n_pwd = next_pwd(sys.argv[1])
    print(n_pwd)
    n_pwd = next_pwd(n_pwd)
    print(n_pwd)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
