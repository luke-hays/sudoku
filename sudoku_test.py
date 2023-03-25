import unittest # https://docs.python.org/3/library/unittest.html
import sudoku

class TestSudoku(unittest.TestCase):
  def test_solved_checker(self):
    emptyGrid = [[None for _ in range(4)] for _ in range(4)]
    almostEmptyGrid = [[2,3,1,4],[4,1,3,2],[3,4,2,1],[1,2,4,None]]
    duplicateRowGrid = [[2,3,1,5],[4,1,3,2],[3,4,2,1],[1,2,4,4]]
    duplicateColumnGrid = [[2,3,1,4],[5,1,3,4],[3,4,2,1],[1,2,4,3]]
    validSolvedGrid = [[2,3,1,4],[4,1,3,2],[3,4,2,1],[1,2,4,3]]

    self.assertEqual(sudoku.gridInSolvedState(emptyGrid), False)
    self.assertEqual(sudoku.gridInSolvedState(almostEmptyGrid), False)
    self.assertEqual(sudoku.gridInSolvedState(duplicateRowGrid), False)
    self.assertEqual(sudoku.gridInSolvedState(duplicateColumnGrid), False)
    self.assertEqual(sudoku.gridInSolvedState(validSolvedGrid), True)


  @unittest.skip('')
  def test_generator_4x4(self):
    self.assertEqual(True, False)

  @unittest.skip('')
  def test_generator_6x6(self):
    self.assertEqual(True, False)

  @unittest.skip('')
  def test_generator_9x9(self):
    self.assertEqual(True, False)

  def test_solver_4x4(self):
    grid = [[None for _ in range(4)] for _ in range(4)]
    solvedGrid = [[2,3,1,4],[4,1,3,2],[3,4,2,1],[1,2,4,3]]

    grid[0][0] = 2
    grid[1][1] = 1
    grid[1][2] = 3
    grid[2][0] = 3
    grid[2][3] = 1
    grid[3][1] = 2
    grid[3][2] = 4

    self.assertEqual(sudoku.solver(grid), solvedGrid)

  def test_solver_6x6(self):
    grid = [[None ,1   ,3   ,None ,5    ,None ],
            [None ,None,5   ,None ,None ,None ],
            [5    ,None,None,4, 1 ,None       ],
            [1    ,None,None,None ,None ,None ],
            [None ,None,2   ,1    ,None ,5    ],
            [3    ,None,1   ,None ,4    ,None ]]
    
    solvedGrid = [[2, 1, 3, 6, 5, 4],
                  [4, 2, 5, 3, 6, 1],
                  [5, 3, 6, 4, 1, 2],
                  [1, 6, 4, 5, 2, 3],
                  [6, 4, 2, 1, 3, 5],
                  [3, 5, 1, 2, 4, 6]]

    self.assertEqual(sudoku.solver(grid), solvedGrid)
  
  def test_solver_9x9(self):
    grid = [[None,6,None,1,None,4,None,5,None],
            [None,None,8,3,None,5,6,None,None],
            [2,None,None,None,None,None,None,None,1],
            [8,None,None,4,None,7,None,None,6],
            [None,None,6,None,None,None,3,None,None],
            [7,None,None,9,None,1,None,None,4],
            [5,None,None,None,None,None,None,None,2],
            [None,None,7,2,None,6,9,None,None],
            [None,4,None,5,None,8,None,7,None]]
    
    solvedGrid = [[3, 6, 2, 1, 7, 4, 8, 5, 9],
                  [1, 2, 8, 3, 4, 5, 6, 9, 7],
                  [2, 3, 4, 6, 5, 9, 7, 8, 1],
                  [8, 1, 3, 4, 9, 7, 5, 2, 6],
                  [9, 7, 6, 8, 1, 2, 3, 4, 5],
                  [7, 8, 5, 9, 6, 1, 2, 3, 4],
                  [5, 9, 1, 7, 8, 3, 4, 6, 2],
                  [4, 5, 7, 2, 3, 6, 9, 1, 8],
                  [6, 4, 9, 5, 2, 8, 1, 7, 3]]

    self.assertEqual(sudoku.solver(grid), solvedGrid)

if __name__ == '__main__':
  unittest.main()