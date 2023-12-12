# Map format:
#   - [0] seed-to-soil
#   - [1] soil-to-fertilizer
#   - [2] fertilizer-to-water
#   - [3] water-to-light
#   - [4] light-to-temperature
#   - [5] temperature-to-humidity
#   - [6] humidity-to-location

print('--- Day 5: If You Give A Seed A Fertilizer ---')

with open('input.txt', 'r') as file:
    lines = file.read().strip().split('\n')

# Integer manipulation algorithm
def findLoc(seed):
    currentNumber = seed
    for map in maps:
        for destinationStart, sourceStart, rangeLenght in map:
            if sourceStart <= currentNumber < sourceStart + rangeLenght:
                currentNumber = destinationStart + (currentNumber - sourceStart)
                break
    return currentNumber

maps = []
locations = []

# List the seeds
seeds = list(map(int, lines[0].split(' ')[1:]))

# Map the lines
i = 0
while i < len(lines):
    maps.append([])
    # Skip each title
    i += 1
    # Grab the values until a blank line
    while i < len(lines) and not lines[i] == '':
        destinationStart, sourceStart, rangeLenght = map(int, lines[i].split())
        maps[-1].append((destinationStart, sourceStart, rangeLenght))
        i += 1
    i += 1

# Find the locations
for seed in seeds:
    location = findLoc(seed)
    locations.append(location)

print('Answer is: ', min(locations))
