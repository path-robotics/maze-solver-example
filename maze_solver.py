class MazeSolver:
    def __init__(self, maze_string):
        self.maze = maze_string.split('\n')
        self.start = None
        self.end = None
        
    def find_empty_space(self):
        """User Story 1: Find the empty space in a single-row input"""
        if len(self.maze) == 1:
            row = self.maze[0]
            for i, char in enumerate(row):
                if char == ' ':
                    return i
        return -1
    
    def solve(self):
        """Main solving method"""
        # For now, just handle single row
        result = self.find_empty_space()
        if result != -1:
            return f"Empty space found at position {result}"
        return "No solution found"
