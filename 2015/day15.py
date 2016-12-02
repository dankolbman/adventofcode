import unittest
import sys
import numpy as np
import scipy.optimize


def process_line(l):
    x = l.replace(',', '').split()
    return (int(x[2]), int(x[4]), int(x[6]), int(x[8]), int(x[10]), x[0])

def calculate_vector(data, x1, x2, x3, x4):
    r1 = data[0][0] * x1 + data[1][0] * x2 + data[2][0] * x3 + data[3][0] * x4 
    r2 = data[0][1] * x1 + data[1][1] * x2 + data[2][1] * x3 + data[3][1] * x4 
    r3 = data[0][2] * x1 + data[1][2] * x2 + data[2][2] * x3 + data[3][2] * x4
    r4 = data[0][3] * x1 + data[1][3] * x2 + data[2][3] * x3 + data[3][3] * x4
    if r1 <= 0 or r2 <= 0 or r3 <= 0 or r4 <= 0:
        return 0 
    return r1 * r2 * r3 * r4

def calculate_vector_2(data, x1, x2, x3, x4):
    r1 = data[0][0] * x1 + data[1][0] * x2 + data[2][0] * x3 + data[3][0] * x4 
    r2 = data[0][1] * x1 + data[1][1] * x2 + data[2][1] * x3 + data[3][1] * x4 
    r3 = data[0][2] * x1 + data[1][2] * x2 + data[2][2] * x3 + data[3][2] * x4
    r4 = data[0][3] * x1 + data[1][3] * x2 + data[2][3] * x3 + data[3][3] * x4
    r5 = data[0][4] * x1 + data[1][4] * x2 + data[2][4] * x3 + data[3][4] * x4
    if r5 != 500:
        return -1
    if r1 <= 0 or r2 <= 0 or r3 <= 0 or r4 <= 0:
        return 0 
    return r1 * r2 * r3 * r4

data = []
for l in open('input.txt').readlines():
    data.append(process_line(l))

# Part 1
t = -1
for x1 in range(0, 101):
    for x2 in range(0, 101 - x1):
        for x3 in range(0, 101 - x1 - x2):
            x4 = 100 - x1 - x2 - x3             
            x = calculate_vector(data, x1, x2, x3, x4)
            if x > t:
                t = x                   
print(t)

# Part 2
t = -1
for x1 in range(0, 101):
    for x2 in range(0, 101 - x1):
        for x3 in range(0, 101 - x1 - x2):
            x4 = 100 - x1 - x2 - x3             
            x = calculate_vector_2(data, x1, x2, x3, x4)
            if x > t:
                t = x                   
print(t)



def ingredients( instr ):
  ing = {}
  for line in instr.split('\n'):
    l = line.replace(':','').replace(',','').split()
    ing[l[0]] = [ int(l[2]), int(l[4]), int(l[6]), int(l[8]), int(l[10]) ]
  
  return ing

def ing_mat( ing ):
  ind = {}
  ing_m = []
  for k,v in ing.items():
    ind[k] = len(ind.keys())
    ing_m.append(np.array(v[0:-1]))

  xs = np.linalg.lstsq(ing_m, np.random.rand(len(ind)))  

  ing_m = -1*np.array(ing_m)
  ing_m = ing_m[:][0:3]

  c = ( {'type': 'ineq', 'fun': lambda x: sum(x) == 100 },
        {'type': 'ineq', 'fun': lambda x: sum(x) - 100 })

  print( ing_m )
  print( ing_m*np.array([44,56]).T )

  r = scipy.optimize.minimize(lambda x: ing_m[0]*x[0] + ing_m[1]*x[1],\
                              np.ones(ing_m.shape[0]),\
                              method='COBYLA',\
                              bounds=[(0,100) for i in ind] ,\
                              constraints=c,
                              options={'maxiter': 10000})
  print(ing_m)
  print(r)

  return np.array(ing_m)

class TestFuncs(unittest.TestCase):

  def test_indgredients(self):
    ing = ingredients( 'Butterscotch: capacity -1, durability -2,\
                          flavor 6, texture 3, calories 8\n\
                         Cinnamon: capacity 2, durability 3,\
                         flavor -2, texture -1, calories 3')
    self.assertEqual( ing['Butterscotch'][0], -1 )
    self.assertEqual( ing['Butterscotch'][2], 6 )
    self.assertEqual( ing['Cinnamon'][1], 3)
    self.assertEqual( ing['Cinnamon'][3], -1)
    ing_mat(ing)

if __name__ == '__main__':
  if len(sys.argv) == 2:
    pass
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
