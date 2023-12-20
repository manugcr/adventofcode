print('--- Day 18: Lavaduct Lagoon ---')

perimeter = 0
points = [(0, 0)]
DIRECTION = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}

def area(points):
    result = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        x2, y2 = points[i+1]
        result += x1 * y2 - x2 * y1
    return abs(result) // 2

with open('input.txt', 'r') as f:
    grid = [line.split() for line in f.readlines()]

for i in grid:
    dist = int(i[1])
    dir = DIRECTION[i[0]]
    perimeter += dist
    points.append((points[-1][0] + dist * dir[0], points[-1][1] + dist * dir[1]))

print(points)
print(f'Answer: {area(points) + perimeter//2+1}')