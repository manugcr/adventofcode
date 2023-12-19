from collections import defaultdict

print('--- Day 16: The Floor Will Be Lava ---')

RIGHT, LEFT, UP, DOWN = (1, 0), (-1, 0), (0, -1), (0, 1)
MOVES = {
    ('.', RIGHT): [RIGHT],
    ('.', LEFT): [LEFT],
    ('.', UP): [UP],
    ('.', DOWN): [DOWN],

    ('-', RIGHT): [RIGHT],
    ('-', LEFT): [LEFT],
    ('-', UP): [LEFT, RIGHT],
    ('-', DOWN): [LEFT, RIGHT],
    
    ('|', RIGHT): [UP, DOWN],
    ('|', LEFT): [UP, DOWN],
    ('|', UP): [UP],
    ('|', DOWN): [DOWN],
    
    ('\\', RIGHT): [DOWN],
    ('\\', LEFT): [UP],
    ('\\', UP): [LEFT],
    ('\\', DOWN): [RIGHT],
    
    ('/', RIGHT): [UP],
    ('/', LEFT): [DOWN],
    ('/', UP): [RIGHT],
    ('/', DOWN): [LEFT],
}

with open('input.txt', 'r') as file:
    grid = [list(line.strip()) for line in file]

energized = defaultdict(set)
beams = [(LEFT, RIGHT)]
while len(beams) > 0:
    beams_pos, dir = beams.pop()
    x, y = (beams_pos[0] + dir[0], beams_pos[1] + dir[1])

    if x < 0 or x >= len(grid[0]) or y < 0 or y>= len(grid):
        continue

    if (x, y) in energized and dir in energized[(x, y)]:
        continue

    energized[(x, y)].add(dir)

    for new_dir in MOVES[(grid[y][x], dir)]:
        beams.append(((x, y), new_dir))

print(f'Answer: {len(energized)}')