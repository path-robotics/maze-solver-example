class MazeSolver:
    def __init__(self, maze_string):
        self.maze = maze_string.split('\n')
        self.start = None
        self.end = None
        self.path = []
        
    def find_empty_space(self):
        """User Story 1: Find the empty space in a single-row input"""
        if len(self.maze) == 1:
            row = self.maze[0]
            for i, char in enumerate(row):
                if char == ' ':
                    return i
        return -1
    
    def find_start_and_end(self):
        """Find S (start) and E (end) positions in maze"""
        for row_idx, row in enumerate(self.maze):
            for col_idx, char in enumerate(row):
                if char == 'S':
                    self.start = (row_idx, col_idx)
                elif char == 'E':
                    self.end = (row_idx, col_idx)
    
    def walk_hallway(self):
        """User Story 2: Walk through a straight hallway maze"""
        if not self.start or not self.end:
            self.find_start_and_end()
        
        if not self.start or not self.end:
            return None
        
        current = self.start
        self.path = [current]
        
        # Simple approach: try moving right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while current != self.end:
            row, col = current
            moved = False
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                # Check bounds
                if 0 <= new_row < len(self.maze) and 0 <= new_col < len(self.maze[new_row]):
                    cell = self.maze[new_row][new_col]
                    new_pos = (new_row, new_col)
                    
                    # Move if it's empty space or the end, and we haven't been there
                    if (cell == ' ' or cell == 'E') and new_pos not in self.path:
                        current = new_pos
                        self.path.append(current)
                        moved = True
                        break
            
            if not moved:
                break
        
        return self.path if current == self.end else None
    
    def solve(self):
        """Main solving method"""
        # Check if single row first
        if len(self.maze) == 1:
            result = self.find_empty_space()
            if result != -1:
                return f"Empty space found at position {result}"
        
        # Try hallway walking
        result = self.walk_hallway()
        if result:
            return f"Path found with {len(result)} steps: {result}"
        
        return "No solution found"
