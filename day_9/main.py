from math import comb

print('--- Day 9: Mirage Maintenance ---')

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
answer = 0
for line in lines:
    line = line.split()
    for index, value in enumerate(line):
        pascal = comb(len(line), index)
        answer += int(value) * pascal * (-1) ** (len(line) - index + 1)

print(answer)