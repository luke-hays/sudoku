import unittest # https://docs.python.org/3/library/unittest.html
import sudoku

class TestSudoku(unittest.TestCase):
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
    solvedGrid = [[None for _ in range(4)] for _ in range(4)]

    grid[0][0] = 2
    grid[1][1] = 1
    grid[1][2] = 3
    grid[2][0] = 3
    grid[2][3] = 1
    grid[3][1] = 2
    grid[3][2] = 4

    self.assertEqual(sudoku.solver(grid), solvedGrid)

  @unittest.skip('')
  def test_solver_6x6(self):
    self.assertEqual(True, False)

  @unittest.skip('')
  def test_solver_9x9(self):
    self.assertEqual(True, False)

if __name__ == '__main__':
  unittest.main()