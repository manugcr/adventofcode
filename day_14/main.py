print('--- Day 14: Parabolic Reflector Dish ---')

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

answer = 0
for y, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == 'O':
            grid[y][x] = '.'
            i = y-1
            while i >= 0 and grid[i][x] == '.':
                i -= 1
            grid[i+1][x] = 'O'
            answer += len(grid)-i-1

print(f'Answer: {answer}')