import unittest
import sys
import itertools
import numpy as np


def tot_dist(path, dists):
  """ Calculate the total distance of a path through a distance matrix """
  #d = sum([ dists[path[i]][path[i-1]] for i in range(1,len(path))])
  d = 0
  for i in range(1,len(path)):
    d += dists[path[i]][path[i-1]]
  return d

def shortest(instr, longest=False):
  
  # Construct locations dict to resolve names to indicies
  locations = {}
  cid = 0
  for line in instr.split('\n'):
    l = line.split()
    if l[0] not in locations:
      locations[l[0]] = cid
      cid += 1
    if l[2] not in locations:
      locations[l[2]] = cid
      cid += 1

  # Make a graph
  dists = np.zeros( (len(locations),len(locations)) )
  for line in instr.split('\n'):
    l = line.split()
    dists[locations[l[0]]][locations[l[2]]] = int(l[4])
    dists[locations[l[2]]][locations[l[0]]] = int(l[4])

  paths = {}
  for c in itertools.permutations(list(locations.values()), len(locations)):
    paths[c] = tot_dist(c, dists)

  return sorted(paths.values(), reverse=longest)[0]

class TestFuncs(unittest.TestCase):

  def test_shortest(self):
    g = 'London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141'
    self.assertEqual( shortest(g), 605 )
  
  def test_longest(self):
    g = 'London to Dublin = 464\nLondon to Belfast = 518\nDublin to Belfast = 141'
    self.assertEqual( shortest(g, True), 982 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    s = shortest(sys.argv[1])
    print('Shortest path:',s)
    l = shortest(sys.argv[1], True)
    print('Longest path:',l)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
