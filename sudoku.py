# Sudoku / n-Puzzle Solver - A* Algorithm
# https://en.wikipedia.org/wiki/A*_search_algorithm

from queue import PriorityQueue

def formatGrid(grid):
  for row in range(len(grid)):
    print(grid[row])

def generator():
  return None

def gridInSolvedState(grid):
  for row in range(len(grid)):
    if None in grid[row]: return False
    if (len(set(grid[row])) != len(grid[row])): return False

  for row in range(len(grid)):
    colSet = set()
    for col in range(len(grid)):
      colSet.add(grid[col][row])
    if len(colSet) != len(grid): return False
  return True

def getEmptyPos(grid):
  for row in range(len(grid)):
    for col in range(len(grid)):
      if grid[row][col] == None:
        return [row, col]
      
def getPriority(grid):
  priority = 0
  for row in range(len(grid)):
    for col in range(len(grid)):
      if grid[row][col] == None:
        priority += 1
  return priority

def placementIsValid(n, pos, grid):
  for row in range(len(grid)):
    if grid[row][pos[1]] == n: return False
  for col in range(len(grid)):
    if grid[pos[0]][col] == n: return False
  return True

# With A* put our starting grid on top of a priority queue
# Start from highest priority config and add to queue all configs that can be reached from that with move
# We can try every number from 1 - grid length inclusive
# We should only add states that are valid
# Adding a number to the grid reduces the Nones - use as priority?
def solver(grid):  
  pq = PriorityQueue()

  pq.put((getPriority(grid), grid))
  
  while not pq.empty():
    state = pq.get()
    priority = state[0]
    newGrid = state[1]

    if (gridInSolvedState(newGrid)): 
      # formatGrid(newGrid)
      return newGrid

    pos = getEmptyPos(newGrid)

    for i in range(1, len(grid)+1):
      if (placementIsValid(i, pos, newGrid)):
        clone = [[y for y in x] for x in newGrid]
        clone[pos[0]][pos[1]] = i
        pq.put((priority, clone))

def main():
  print('Hello World')

if __name__ == "__main__":
  main()