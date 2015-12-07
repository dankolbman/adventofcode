import unittest
import sys
import numpy as np

def apply_step(step, lights):
  """ Apply a given step to a light configuration """
  line = step.split()
  beg = np.fromstring(line[-3], sep=',')
  end = np.fromstring(line[-1], sep=',')
  end[0] += 1
  end[1] += 1
  if step.startswith('toggle'):
    lights[beg[0]:end[0], beg[1]:end[1]] = np.invert(
                            lights[beg[0]:end[0], beg[1]:end[1]] )
  elif step.startswith('turn on'):
    lights[beg[0]:end[0], beg[1]:end[1]] = np.ones(
                                (end[0]-beg[0], end[1]-beg[1]), dtype=bool)
  elif step.startswith('turn off'):
    lights[beg[0]:end[0], beg[1]:end[1]] = np.zeros(
                                (end[0]-beg[0], end[1]-beg[1]), dtype=bool)


  return lights

def do_all(steps):
  """ Do all given steps and return the state of the lights """
  lights = np.zeros((1000,1000), dtype=bool)
  for step in steps.split('\n'):
    apply_step(step, lights)

  return lights


def apply_step2(step, lights):
  """ Apply a given step to a light configuration """
  line = step.split()
  beg = np.fromstring(line[-3], sep=',')
  end = np.fromstring(line[-1], sep=',')
  end[0] += 1
  end[1] += 1
  if step.startswith('toggle'):
    lights[beg[0]:end[0], beg[1]:end[1]] += 2
  elif step.startswith('turn on'):
    lights[beg[0]:end[0], beg[1]:end[1]] += 1
  elif step.startswith('turn off'):
    lights[beg[0]:end[0], beg[1]:end[1]] -= 1
    lights[lights<0] = 0

def do_all2(steps):
  """ Do all given steps and return the state of the lights """
  lights = np.zeros((1000,1000), dtype=np.int)
  for step in steps.split('\n'):
    apply_step2(step, lights)

  return lights

class TestFuncs(unittest.TestCase):
  
  def test_num_lit(self):
    self.assertEqual( np.sum(do_all('turn on 0,0 through 999,999')), 1000000 )
    self.assertEqual( np.sum(do_all('toggle 0,0 through 999,0')), 1000 )
    self.assertEqual( np.sum(do_all('turn off 499,499 through 500,500')), 0 )
  
  def test_num_lit2(self):
    self.assertEqual( np.sum(do_all2('turn on 0,0 through 0,0')), 1 )
    self.assertEqual( np.sum(do_all2('turn on 0,0 through 1,0')), 2 )
    self.assertEqual( np.sum(do_all2('toggle 0,0 through 999,999')), 2000000 )
    self.assertEqual( np.sum(do_all2('turn on 0,0 through 499,499\n\
turn on 0,0 through 249,249')), 312500 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    final = do_all(sys.argv[1])
    print(np.sum(final), 'lights on after following all instructions')
  elif len(sys.argv) == 3:
    final = do_all2(sys.argv[1])
    print(np.sum(final), 'brightness after following all instructions')
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
