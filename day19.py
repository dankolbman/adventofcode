import unittest
import sys
import re
import random

def read_repl( instr ):
  replacements = []
  mol = instr.split('\n')[-1].strip()
  for l in instr.split('\n')[0:-2]:
    replacements.append(re.findall('(\w+) => (\w+)', l.strip())[0])
  return replacements, mol

def n_next( replacements, mol ):
  mols = set()
  for i, j in replacements:
    # Find the index of the first occurence of the replacement key (i)
    ind = mol.find(i)
    while len(mol) > ind > -1:
      mols.add( mol[0:ind] + mol[ind:].replace(i, j, 1) )
      ind = mol.find(i, ind+1)
  return len(mols)

def n_need( repl, mol, trials=100 ):
  best = 100000
  random.shuffle(repl)
  s = []
  for i in range(trials):
    steps = 0
    i = 0
    cmol = mol
    while cmol != 'e' and i < 1000:
      i += 1
      random.shuffle(repl)
      for r in repl:
        if r[1] not in cmol: continue
        if cmol.replace(r[1], r[0],1) != 'NRnBSiRnCaRnFArYFArFArF':
          cmol = cmol.replace(r[1], r[0], 1)
        s.append(r)
        steps += 1
        break
    s = []
    if steps < best and cmol == 'e':
      best = steps

  return best

class TestFuncs(unittest.TestCase):

  def test_num_read_repl(self):
    instr ='''H => HO
              H => OH
              O => HH

              HOH'''
    repl, mol = read_repl( instr )
    self.assertEqual(repl[0], ('H', 'HO'))
    self.assertEqual(repl[1], ('H', 'OH'))

  def test_n_next(self):
    instr ='''H => HO
              H => OH
              O => HH

              HOH'''
    repl, mol = read_repl( instr )
    self.assertEqual( n_next( repl, mol ), 4 )
    mol = 'HOHOHO'
    self.assertEqual( n_next( repl, mol ), 7 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    repl, mol = read_repl(sys.argv[1])
    n = n_next( repl, mol )
    print('\n',n, 'possible next molecules')
    n = n_need( repl, mol )
    print(n, 'minimum steps needed')
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
