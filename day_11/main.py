print('--- Day 11: Cosmic Expansion ---')

with open('input.txt', 'r') as file:
    grid = file.read().strip().splitlines()

# Get empty rows and cols
empty_rows = []
for r, row in enumerate(grid):
    if all(ch == '.' for ch in row):
        empty_rows.append(r)

empty_cols = []
for c in range(len(grid[0])):
    if all(row[c] == '.' for row in grid):
        empty_cols.append(c)

# Get galaxies
galaxies = []
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == '#':
            galaxies.append((r, c))

answer = 0
scale = 2

# Manhatan distance
for i, (r1, c1) in enumerate(galaxies):
    for (r2, c2) in galaxies[i+1:]:
        for r in range(min(r1, r2), max(r1, r2)):
            if r in empty_rows:
                answer += scale
            else:
                answer += 1
        for c in range(min(c1, c2), max(c1, c2)):
            if c in empty_cols:
                answer += scale
            else:
                answer += 1

print(f'Answer: {answer}')