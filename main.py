from maze_solver import MazeSolver


def main():
    print("=== Single row ===")
    maze1 = "### ###"
    solver = MazeSolver(maze1)
    print(solver.solve())

    print("\n=== Simple turns ===")
    maze2 = """#######
#S    #
##### #
#     #
# #####
#    E#
#######"""
    solver2 = MazeSolver(maze2)
    print(solver2.solve())

    print("\n=== Maze has rooms ===")
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

    print("\n=== Complex turns ===")
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

    print("\n=== Deadends ===")
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
