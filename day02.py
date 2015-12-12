import unittest
import sys

def parse_boxes(instr):
  """ Takes an input string and parses it into a list of box dimensions """
  boxes = []
  for line in instr.split('\n'):
    l = line.split('x')
    boxes.append( [ int(i) for i in l ] )

  return boxes

def paper_needed(boxes):
  """ Calculates the area of paper needed for a given list of boxes """
  area = 0
  for box in boxes:
    # The smallest face of the box
    sides = sorted(box)
    small = sides[0]*sides[1]
    area += 2*box[0]*box[1] + 2*box[0]*box[2] + 2*box[1]*box[2] + small

  return area

def ribbon_needed(boxes):
  """ Calculates the length of ribbon needed """
  length = 0
  for box in boxes:
    # Shortest perimeter
    sides = sorted(box)
    p = 2*sides[0] + 2*sides[1]
    v = box[0]*box[1]*box[2]
    length += p + v

  return length
  
class TestFuncs(unittest.TestCase):
  def test_parse_boxes(self):
    self.assertEqual( parse_boxes('2x3x4'), [[2,3,4]] )
    self.assertEqual( parse_boxes('2x3x4\n1x1x10'), [[2,3,4], [1,1,10]] )

  def test_paper_needed(self):
    self.assertEqual( paper_needed([[2,3,4]]), 58 )
    self.assertEqual( paper_needed([[1,1,10]]), 43 )

  def test_ribbon_needed(self):
    self.assertEqual( ribbon_needed([[2,3,4]]), 34 )
    self.assertEqual( ribbon_needed([[1,1,10]]), 14 )

if __name__ == '__main__':
  if len(sys.argv) == 2:
    boxes = parse_boxes(sys.argv[1])
    print('Paper needed:', paper_needed( boxes ), 'Sq ft')
    print('Ribbon needed:', ribbon_needed( boxes ), 'ft')
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
