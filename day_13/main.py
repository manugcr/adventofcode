print('--- Day 13: Point of Incidence ---')

with open('input.txt', 'r') as f:
    blocks = f.read().split('\n\n')
    grids = [block.splitlines() for block in blocks]

def find_mirror(grid):
    for i in range(len(grid) - 1):
        lower = i
        upper = i + 1
        while lower >= 0 and upper < len(grid):
            if grid[lower] != grid[upper]:
                break
            lower -= 1
            upper += 1
        else:
            return i + 1
    return 0

answer = 0
for grid in grids:
    horizontal = find_mirror(grid)
    # Transpose grid
    vertical = find_mirror(list(map(list, zip(*grid))))

    answer += 100 * horizontal
    answer += vertical


print('Answer: ', answer)