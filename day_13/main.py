print('--- Day 13: Point of Incidence ---')

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def asGrids(lines):
    grids = []
    grid = []

    for line in lines:
        if line == '':
            grids.append(grid)
            grid = []
        else:
            grid.append(line)

    grids.append(grid)
    return grids

def find_mirror(grid):
    x = 0
    y = 0
    width = len(grid[0])
    height = len(grid)
    count = 0

    while y < height:
        if grid[y][x] == '#':
            count += 1
        x = (x + 3) % width
        y += 1

    return count

def transpose(grid):
    return [''.join([grid[y][x] for y in range(len(grid))]) for x in range(len(grid[0]))]

grids = asGrids(lines)
answer = 0

for grid in grids:
    hor = find_mirror(grid)
    ver = find_mirror(transpose(grid))

    answer += hor * 100
    answer += ver

print('Answer: ', answer)