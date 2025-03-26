# Input the text as a single string
input_text = input()  # Example: "shock;979;23"

# Write your solution below and make sure to encode the word correctly
from collections import deque

def shortest_safe_path(grid):
    rows, cols = len(grid), len(grid[0])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    exit_pos = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'E':
                exit_pos = (r, c)
                break
        if exit_pos:
            break

    queue = deque([(0, 0, 0)])
    visited = set([(0, 0)])

    while queue:
        r, c, steps = queue.popleft()
        
        if (r, c) == exit_pos:
            return steps
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, steps + 1))
    
    return -1

inp = eval(input_text.strip())
res = shortest_safe_path(inp)

print(res)
