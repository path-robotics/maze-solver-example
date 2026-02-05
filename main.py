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
    
    # Test User Story 4 - winding paths
    print("\n=== User Story 4 ===")
    maze4 = """###########
#S        #
##### ### #
#   # #   #
# # # # ###
# # #   # #
# ### # # #
#     #  E#
###########"""
    solver4 = MazeSolver(maze4)
    print(solver4.solve())
    
    # Test User Story 5 - dead ends
    print("\n=== User Story 5 ===")
    maze5 = """#########
#S#     #
# # ### #
# #   # #
# ### # #
#     #E#
#########"""
    solver5 = MazeSolver(maze5)
    print(solver5.solve())


if __name__ == "__main__":
    main()
