from maze_solver import MazeSolver

def main():
    # Test User Story 1
    maze1 = "### ###"
    solver = MazeSolver(maze1)
    print(solver.solve())


if __name__ == "__main__":
    main()
