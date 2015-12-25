import sys

def get_row_col(row, col, first):
  # The number in the sequence that we want
  count = h(row, col)
  
  for i in range(count-1):
    first = next_n(first)
  return first

def next_n(n):
  return (n * 252533) % 33554393
  
def h(row, col):
  return sum(range(1,row+col-1)) + col

if __name__ == '__main__':
  if len(sys.argv) == 4:
    code = get_row_col(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
    print(code)
  else:
    print('No/incorrect number of arguements given. Running tests...')
    unittest.main()
