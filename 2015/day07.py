import unittest
import sys

bits = 65536

class Gate:
  operator = 'VAL'
  sym = 'abcd'
  in_syms = []
  ins = []
  output = -9999

  def __init__(self, sym, operator, in_syms):
    self.sym = sym
    self.operator = operator
    self.ins = []
    self.in_syms = []
    self.output = -9999
    if operator == 'VAL':
      if in_syms[0].isdigit():
        self.ins = [int(in_syms[0])]
      else:
        self.in_syms = in_syms
    else:
      for sym in in_syms:
        if sym.isdigit():
          self.ins.append(Gate(sym, 'VAL', [sym]))
        else:
          self.in_syms.append(sym)

  def calc_output(self):
    if self.output > -9999:
      return self.output
    if self.operator == 'VAL':
      if type(self.ins[0]) is int:
        self.output = self.ins[0]
      else:
        self.output = self.ins[0].calc_output()
    else:
      if self.operator == 'NOT': 
        self.output = ~self.ins[0].calc_output() % bits
      elif self.operator == 'AND':
        self.output = self.ins[0].calc_output() & self.ins[1].calc_output() % bits
      elif self.operator == 'OR':
        self.output = self.ins[0].calc_output() | self.ins[1].calc_output() % bits
      elif self.operator == 'LSHIFT':
        self.output = self.ins[1].calc_output() << self.ins[0].calc_output() % bits
      elif self.operator == 'RSHIFT':
        self.output = self.ins[1].calc_output() >> self.ins[0].calc_output() % bits

    return self.output

  def __repr__(self):
    return '< {} Gate {} >'.format(self.operator, self.sym)

def make_circ( instr ):
  circ = {}

  # Initialize gates
  for line in instr.split('\n'):
    l = line.strip().split(' ')
    if len(l) < 3:
      continue
    if len(l) == 3: # ASSIGNMENT
      circ[ l[2] ] = Gate( l[2], 'VAL', [l[0]] )
    elif len(l) == 4: # NOT
      circ[ l[3] ] = Gate( l[3], 'NOT', [l[1]] ) 
    elif l[1] == 'AND':
      circ[ l[4] ] = Gate( l[4], 'AND', [l[0], l[2]] )
    elif l[1] == 'OR':
      circ[ l[4] ] = Gate( l[4], 'OR', [l[0], l[2]] )
    elif l[1] == 'LSHIFT':
      circ[ l[4] ] = Gate( l[4], 'LSHIFT', [l[0], l[2]] )
    elif l[1] == 'RSHIFT':
      circ[ l[4] ] = Gate( l[4], 'RSHIFT', [l[0], l[2]] )

  # Link gates
  for gate in circ.values():
    for sym in gate.in_syms:
      gate.ins.append(circ[sym])

  return circ

class TestFuncs(unittest.TestCase):

  def test_circ(self):
    circ = '''123 -> x
        456 -> y
        x AND y -> d
        x OR y -> e
        x LSHIFT 2 -> f
        y RSHIFT 2 -> g
        NOT x -> h
        NOT y -> i'''
  
    output = make_circ(circ)

    self.assertEqual(output['d'].calc_output(), 72)
    self.assertEqual(output['e'].calc_output(), 507)
    self.assertEqual(output['f'].calc_output(), 492)
    self.assertEqual(output['g'].calc_output(), 114)
    self.assertEqual(output['h'].calc_output(), 65412)
    self.assertEqual(output['i'].calc_output(), 65079)
    self.assertEqual(output['x'].calc_output(), 123)
    self.assertEqual(output['y'].calc_output(), 456)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    circ = make_circ(sys.argv[1])
    out = circ['a'].calc_output()
    print('output of a:', out)
    circ = make_circ(sys.argv[1])
    circ['b'].ins = [out]
    new_out = circ['a'].calc_output()
    print('New output of a:', new_out)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
