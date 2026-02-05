# Maze Solver

A simple maze solver that can navigate through various types of mazes, from simple single-row puzzles to complex mazes with rooms, winding paths, and dead ends.

## Requirements

- Python 3.8+
- `uv` for dependency management

## Installation

This project uses `uv` for managing the Python environment. If you don't have `uv` installed, you can install it following the instructions at [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv).

```bash
# The project has no external dependencies beyond Python standard library
uv sync
```

## Running the Solution

To run the main demo that shows all user stories:

```bash
python main.py
```

To run the tests:

```bash
python -m pytest test_maze_solver.py -v
# or
python -m unittest test_maze_solver.py
```

## Implementation

The maze solver uses a breadth-first search (BFS) algorithm to explore the maze. It:
- Parses maze strings into a 2D grid representation
- Finds start (S) and end (E) positions
- Explores all reachable cells using a queue
- Tracks visited positions to avoid loops
- Returns the shortest path from start to end

## User Stories Completed

1. ✅ Find empty space in single-row input
2. ✅ Walk through hallway mazes
3. ✅ Navigate mazes with rooms
4. ✅ Follow winding paths
5. ✅ Handle dead ends and find the exit

---

## Part 2: Analysis

### Analysis Story 1: Limitations

My algorithm may not solve correctly for:

1. **Mazes without a valid start (S) or end (E) marker** - The algorithm requires both markers to function. It will return "No solution found" if either is missing.

2. **Mazes with multiple possible paths** - While the algorithm will find A solution, it doesn't necessarily find ALL solutions or allow the user to choose between them.

3. **Very large mazes** - The current implementation stores the entire path history for each explored position in the queue, which could consume significant memory for large mazes.

4. **Mazes with diagonal movement** - The current implementation only checks 4 directions (up, down, left, right). If diagonal movement is allowed, it won't find those paths.

### Analysis Story 2: Complexity and Optimization

**Current Complexity:**
- Time Complexity: O(R × C) where R is rows and C is columns, as we may visit each cell once
- Space Complexity: O(R × C × P) where P is the path length, since we store the full path for each queue entry

**Optimization Approaches:**

1. **Path Reconstruction** - Instead of storing the complete path in each queue entry, store only the parent pointer for each cell. Reconstruct the path at the end by backtracking through parents. This reduces space complexity to O(R × C).

2. **Better Data Structures** - Currently using a list for the queue (with pop(0) being O(n)). Using `collections.deque` would make queue operations O(1).

3. **Heuristic Search (A\*)** - For finding optimal paths faster, implement A\* algorithm with Manhattan distance heuristic. This could significantly reduce the number of cells explored in larger mazes.

4. **Early Termination** - The current BFS already stops when finding the end, but we could add additional pruning strategies.

5. **Maze Representation** - Currently storing the maze as a list of strings. Converting to a more efficient 2D data structure could improve access times.

### Analysis Story 3: Robot Ship Navigation

**Problem:** Navigate a 1×3 ship through a maze that can move forward/backward and rotate in a 3×3 space.

**Incremental Story Decomposition:**

**Story 1: Basic Ship Representation**
- Define ship state: position (center cell) and orientation (N/S/E/W)
- Create a function to get the 3 cells occupied by the ship given position and orientation
- Validate if a ship configuration is valid (all 3 cells are within bounds and not walls)

**Story 2: Forward/Backward Movement**
- Implement move_forward() and move_backward() functions
- Check collision for all 3 cells of the ship before moving
- Test with a simple straight corridor

**Story 3: Rotation Mechanics**
- Implement rotate_clockwise() and rotate_counterclockwise()
- Validate that the center is in the middle of a 3×3 space
- Check that all destination cells after rotation are free
- Test in an open room

**Story 4: Combined Movement Navigation**
- Modify search algorithm to explore states (position, orientation)
- Each state has multiple possible actions: forward, backward, rotate_cw, rotate_ccw
- Find path from start state to end state (specific position and orientation)
- Test in simple mazes requiring one rotation

**Story 5: Complex Navigation**
- Handle mazes requiring multiple rotations
- Optimize to avoid redundant rotations
- Test in tight spaces where rotation order matters

**Story 6: Optimal Path Finding**
- Add cost/weight to different actions (rotation might be more expensive than movement)
- Use A\* or weighted BFS to find optimal path
- Balance between path length and number of rotations
