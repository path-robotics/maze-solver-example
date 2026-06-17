import unittest
from maze_solver import MazeSolver


class TestMazeSolver(unittest.TestCase):
    def test_single_row_maze(self):
        maze = "### ###"
        solver = MazeSolver(maze)
        result = solver.find_empty_space()
        self.assertEqual(result, 3)

    def test_simple_hallway(self):
        maze = """#######
#S    #
##### #
#     #
# #####
#    E#
#######"""
        solver = MazeSolver(maze)
        path = solver.explore_maze()
        self.assertIsNotNone(path)
        self.assertEqual(path[0], (1, 1))  # Start
        self.assertEqual(path[-1], (5, 5))  # End

    def test_maze_with_rooms(self):
        maze = """#########
#S      #
# ##### #
# #   # #
# # # # #
# # # # #
#   #  E#
#########"""
        solver = MazeSolver(maze)
        path = solver.explore_maze()
        self.assertIsNotNone(path)
        self.assertTrue(len(path) > 0)

    def test_no_solution(self):
        """Test maze with no solution"""
        maze = """#####
#S# #
### #
#  E#
#####"""
        solver = MazeSolver(maze)
        path = solver.explore_maze()
        self.assertIsNone(path)


if __name__ == "__main__":
    unittest.main()
