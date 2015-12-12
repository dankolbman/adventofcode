import unittest
import sys
import json
import re

def count(instr):
  """ Uses regex to identify all numbers and add them """
  s = 0
  matches = re.findall(r'-?[\d]+', instr)
  if not matches:
    return 0
  for m in matches:
    s += int(m)

  return s

def count_obj(obj):
  """ Counts a json object/dict and returns a sum of all items """
  s = 0
  for o in obj.values():
    if o == 'red':
      return 0
    elif type(o) is int:
      s += o
    elif type(o) is dict:
      s += count_obj(o)
    elif type(o) is list:
      s += count_list(o)
  return s

def count_list(l):
  """ Counts a list and returns the sum of all items"""
  s = 0
  for i in l:
    if type(i) is int:
      s += i
    elif type(i) is dict:
      s += count_obj(i)
    elif type(i) is list:
      s += count_list(i)
  return s

def count_json(instr):
  """ Counts all ints in a json object and ignores any object with 'red' """
  jdat = json.loads(instr)
  if type(jdat) is list:
    c = count_list(jdat)
  else:
    c = count_obj(jdat)
  return c

class TestFuncs(unittest.TestCase):

  def test_count(self):
    self.assertEqual( count('[1,2,3]'), 6 )
    self.assertEqual( count('{"a":2,"b":4}'), 6 )
    self.assertEqual( count('[[[3]]]'), 3 )
    self.assertEqual( count('{"a":{"b":4},"c":-1}'), 3 )
    self.assertEqual( count('{"a":[-1,1]}'), 0 )
    self.assertEqual( count('[-1,{"a":1}]'), 0 )
  
  def test_ig_red(self):
    self.assertEqual( count_json('[1,{"c":"red","b":2},3]'), 4 )
    self.assertEqual( count_json('{"d":"red","e":[1,2,3,4],"f":5}'), 0 )
    self.assertEqual( count_json('[1,"red",5]'), 6 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    s = count(sys.argv[1])
    print('Sum:', s)
  elif len(sys.argv) == 3:
    s = count_json(sys.argv[1])
    print('Sum ignoring objects with "red":', s)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
