import unittest
import sys
import math

def reindeer( instr ):
  r = {}
  for line in instr.split('\n'):
    l = line.split()
    r[l[0]] = [ int(l[3]), int(l[6]), int(l[-2]) ]
  return r

def dist( r, t ):
  """ Calculates the distance made by a reindeer after a given time """
  ts = t // (r[1] + r[2])
  return r[0]*r[1]*ts + r[0]*min(r[1], t % (r[1] + r[2]))

def winner_dist(rs, t):
  """ Return the winner's distance after a given time """
  d = [ dist(r, t) for r in rs.values() ]
  return max(d)

def winner_points(rs, t):
  """ Return the winner's points after a given time """
  d = {}
  pts = {}
  for k in rs.keys():
    d[k] = 0
    pts[k] = 0

  for i in range(t):
    for k,v in rs.items():
      d[k] += v[0] if i % (v[1]+v[2]) < v[1] else 0
    w = max(d.items(), key=lambda x: x[1])[1]
    for k,v in d.items():
      if v == w: pts[k] += 1
  return max(pts.values())

class TestFuncs(unittest.TestCase):

  def test_reindeer(self):
    r = reindeer('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n\
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
    self.assertEqual( r['Comet'], [ 14, 10, 127 ] )
    self.assertEqual( r['Dancer'], [ 16, 11, 162 ] ) 

  def test_dist(self):
    r = reindeer('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n\
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
    self.assertEqual( dist(r['Comet'], 1000), 1120 )
    self.assertEqual( dist(r['Dancer'], 1000), 1056 )

  def test_winner_dist(self):
    r = reindeer('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n\
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
    self.assertEqual( winner_dist(r, 1000), 1120 )

  def test_winner_points(self):
    r = reindeer('Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.\n\
    Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.')
    self.assertEqual( winner_points(r, 1000), 689 )

if __name__ == '__main__':
  if len(sys.argv) == 3:
    r = reindeer(sys.argv[1])
    w = winner_dist(r, int(sys.argv[2]))
    print('Winner distance:', w)
    p = winner_points(r, int(sys.argv[2]))
    print('Winner points:', p)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
