import unittest
import sys

def h(loc):
  """ A location hash. Can collide for moves outside a range of 1024 """
  return loc[0] + loc[1]*1024

def num_visited(instructions, num_santas=1):
  """ Visits houses according to given instructions for a given number of
      Santas. """
  locs = [ [0,0] for i in range(num_santas) ]
  visited = {}
  csanta = 0
  visited[h(locs[csanta])] = 1
  for move in instructions:
    if move == '^':
      locs[csanta][1] += 1
    elif move =='v':
      locs[csanta][1] -= 1
    elif move == '>':
      locs[csanta][0] += 1
    elif move == '<':
      locs[csanta][0] -= 1

    if h(locs[csanta]) not in visited:
      visited[h(locs[csanta])] = 1
    else:
      visited[h(locs[csanta])] += 1
  
    csanta = (csanta + 1) % num_santas

  return len(visited.values())

class TestFuncs(unittest.TestCase):

  def test_num_visited(self):
    self.assertEqual( num_visited('>'), 2 )
    self.assertEqual( num_visited('^>v<'), 4 )
    self.assertEqual( num_visited('^v^v^v^v^v'), 2 )

    self.assertEqual( num_visited('^v', 2), 3 )
    self.assertEqual( num_visited('^>v<', 2), 3 )
    self.assertEqual( num_visited('^v^v^v^v^v', 2), 11 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    print('Visited', num_visited(sys.argv[1]), 'houses')
  elif len(sys.argv) == 3:
    print(sys.argv[2], 'Santas visited',
          num_visited(sys.argv[1], int(sys.argv[2])), 'houses')
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
