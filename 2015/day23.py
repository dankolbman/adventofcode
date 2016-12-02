import unittest
import sys


def proc( instr, reg={ 'a':0, 'b':0 }):

  lines = [ l.replace(',','').strip().split() for l in instr.split('\n') ]
  for l in lines:
    if len(l) == 3 or l[0] == 'jmp':
      l[-1] = int(l[-1])

  l = 0
  while l < len(lines): 
    if lines[l][0] == 'hlf':
      reg[lines[l][1]] /= 2
      l += 1
    elif lines[l][0] == 'tpl':
      reg[lines[l][1]] *= 3
      l += 1
    elif lines[l][0] == 'inc':
      reg[lines[l][1]] += 1
      l += 1
    elif lines[l][0] == 'jmp':
      l += lines[l][1]
    elif lines[l][0] == 'jie':
      if reg[lines[l][1]] % 2 == 0:
        l += lines[l][-1]
      else:
        l += 1
    elif lines[l][0] == 'jio':
      if reg[lines[l][1]] == 1:
        l += lines[l][-1]
      else:
        l += 1
  return reg

class TestFuncs(unittest.TestCase):

  def test_num_visited(self):
    cmds = '''inc a
              jio a, +2
              tpl a
              inc a'''
    self.assertEqual( proc(cmds)['a'], 2 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    r = proc(sys.argv[1])
    print(r)
    r = proc(sys.argv[1], {'a':1,'b':0})
    print(r)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
