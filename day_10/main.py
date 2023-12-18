from collections import deque

print('--- Day 10: Pipe Maze ---')

with open('input.txt', 'r') as file:
    grid = file.read().strip().splitlines()

def get_directions(grid, row, col, character):
    # Up direction
    if row > 0 and character in 'S|JL' and grid[row - 1][col] in '|7F' and (row - 1, col) not in seen:
        seen.add((row - 1, col))
        queue.append((row - 1, col))
    # Down direction
    if row < ROWS - 1 and character in 'S|7F' and grid[row + 1][col] in '|JL' and (row + 1, col) not in seen:
        seen.add((row + 1, col))
        queue.append((row + 1, col))
    # Left direction
    if col > 0 and character in 'S-J7' and grid[row][col - 1] in '-LF' and (row, col - 1) not in seen:
        seen.add((row, col - 1))
        queue.append((row, col - 1))
    # Right direction
    if col < COLS - 1 and character in 'S-LF' and grid[row][col + 1] in '-J7' and (row, col + 1) not in seen:
        seen.add((row, col + 1))
        queue.append((row, col + 1))



ROWS = len(grid)
COLS = len(grid[0])

# Get coordinates of starting point 'S'
for row in range(ROWS):
    for col in range(COLS):
        if grid[row][col] == 'S':
            start_row = row
            start_col = col

# Breadth-first search
seen = {(start_row, start_col)}
queue = deque([(start_row, start_col)])
while queue:
    row, col = queue.popleft()
    character = grid[row][col]
    get_directions(grid, row, col, character)


print(f'Answer: {len(seen)//2}')