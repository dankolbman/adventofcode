import unittest
import sys
import re

def is_nice(word):
  """ Checks if a word is nice depending on the given rules """
  if len(re.findall(r'[aeiou]', word)) >= 3:
    if len(re.findall(r'(.)\1', word)) > 0:
      if len(re.findall(r'(ab|cd|pq|xy)', word)) == 0:
        return True
  return False

def is_nice2(word):
  """ Checks if the word is nice according to the new rules """
  if re.search(r'(..).*\1', word) and re.search(r'(.).\1', word):
    return True
  else:
    return False

class TestFuncs(unittest.TestCase):

  def test_is_nice(self):
    self.assertTrue( is_nice('ugknbfddgicrmopn') )
    self.assertTrue( is_nice('aaa') )
    self.assertFalse( is_nice('jchzalrnumimnmhp') )
    self.assertFalse( is_nice('haegwjzuvuyypxyu') )
    self.assertFalse( is_nice('dvszwmarrgswjxmb') )

  def test_is_nice2(self):
    self.assertTrue( is_nice2('qjhvhtzxzqqjkmpb') )
    self.assertTrue( is_nice2('xxyxx') )
    self.assertFalse( is_nice2('uurcxstgmygtbstg') )
    self.assertFalse( is_nice2('ieodomkazucvgmuy') )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    nice = 0
    for word in sys.argv[1].split('\n'):
      if is_nice(word): nice += 1
    print('Found', nice, 'nice words')
  elif len(sys.argv) == 3:
    nice = 0
    for word in sys.argv[1].split('\n'):
      if is_nice2(word): nice += 1
    print('Found', nice, 'nice words')
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
