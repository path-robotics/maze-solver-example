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
