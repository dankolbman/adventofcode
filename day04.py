import unittest
import hashlib
import sys

def find_hash(key, begin):
  """ Finds an md5 hash of a key + some number that gives a hash beginning 
      with the specified string """
  trial = 0
  while True:
    trialstr = key + str(trial)
    trialhash = hashlib.md5(trialstr.encode())
    if trialhash.hexdigest().startswith(begin):
      return trial
    trial += 1

class TestFuncs(unittest.TestCase):

  def test_find_hash(self):
    self.assertEqual( find_hash('abcdef', '00000'), 609043 )
    self.assertEqual( find_hash('pqrstuv', '00000'), 1048970 )

if __name__ == '__main__':
  if len(sys.argv) == 3:
    print('Answer:', find_hash(sys.argv[1], sys.argv[2]))
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
