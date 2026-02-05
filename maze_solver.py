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
    
    def explore_maze(self):
        """User Story 3: Explore maze with rooms using simple search"""
        if not self.start or not self.end:
            self.find_start_and_end()
        
        if not self.start or not self.end:
            return None
        
        # Use a simple queue for breadth-first exploration
        queue = [(self.start, [self.start])]
        visited = set([self.start])
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            current, path = queue.pop(0)
            
            if current == self.end:
                self.path = path
                return path
            
            row, col = current
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                new_pos = (new_row, new_col)
                
                # Check bounds
                if 0 <= new_row < len(self.maze) and 0 <= new_col < len(self.maze[new_row]):
                    cell = self.maze[new_row][new_col]
                    
                    # Can move to empty space or end, if not visited
                    if (cell == ' ' or cell == 'E') and new_pos not in visited:
                        visited.add(new_pos)
                        queue.append((new_pos, path + [new_pos]))
        
        return None
    
    def solve(self):
        """Main solving method"""
        # Check if single row first
        if len(self.maze) == 1:
            result = self.find_empty_space()
            if result != -1:
                return f"Empty space found at position {result}"
        
        # Try exploring the maze
        result = self.explore_maze()
        if result:
            return f"Path found with {len(result)} steps: {result}"
        
        return "No solution found"
