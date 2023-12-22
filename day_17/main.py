from heapq import heappush, heappop

print('--- Day 17: Clumsy Crucible ---')

with open('input.txt', 'r') as file:
    grid = [list(map(int, line.strip())) for line in file.readlines()]

seen = set()
queue = [(0, 0, 0, 0, 0, 0)]
while queue:
    hl, row, col, dr, dc, num = heappop(queue)

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        print('Answer: ', hl)
        break

    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        continue

    if (row, col, dr, dc, num) in seen:
        continue

    seen.add((row, col, dr, dc, num))

    if num < 3 and (dr, dc) != (0, 0):
        nr = row + dr
        nc = col + dc
        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
            heappush(queue, (hl + grid[nr][nc], nr, nc, dr, dc, num + 1))
    
    for ndr, ndc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if (ndr, ndc) != (dr, dc) and (ndr, ndc) != (-dr, -dc):
            nr = row + ndr
            nc = col + ndc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                heappush(queue, (hl + grid[nr][nc], nr, nc, ndr, ndc, 1))
            