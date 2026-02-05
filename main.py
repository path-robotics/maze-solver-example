from maze_solver import MazeSolver

def main():
    # Test User Story 1
    print("=== User Story 1 ===")
    maze1 = "### ###"
    solver = MazeSolver(maze1)
    print(solver.solve())
    
    # Test User Story 2
    print("\n=== User Story 2 ===")
    maze2 = """#######
#S    #
##### #
#     #
# #####
#    E#
#######"""
    solver2 = MazeSolver(maze2)
    print(solver2.solve())
    
    # Test User Story 3 - rooms
    print("\n=== User Story 3 ===")
    maze3 = """#########
#S      #
# ##### #
# #   # #
# # # # #
# # # # #
#   #  E#
#########"""
    solver3 = MazeSolver(maze3)
    print(solver3.solve())


if __name__ == "__main__":
    main()
