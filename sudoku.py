# Sudoku / n-Puzzle Solver - A* Algorithm
# https://en.wikipedia.org/wiki/A*_search_algorithm

def formatGrid(grid):
  for row in range(len(grid)):
    for col in range(len(grid)):
      print(f'|{grid[row][col]}\t| ', end='')
    print('\n')

def generator():
  return None

def solver(grid):
  formatGrid(grid)

  return None

def main():
  print('Hello World')

if __name__ == "__main__":
  main()