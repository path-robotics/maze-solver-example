import unittest
from maze_solver import MazeSolver


class TestMazeSolver(unittest.TestCase):
    
    def test_single_row_maze(self):
        """Test User Story 1: Single row with empty space"""
        maze = "### ###"
        solver = MazeSolver(maze)
        result = solver.find_empty_space()
        self.assertEqual(result, 3)
    
    def test_simple_hallway(self):
        """Test User Story 2: Simple hallway navigation"""
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
        """Test User Story 3: Maze with rooms"""
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


if __name__ == '__main__':
    unittest.main()
