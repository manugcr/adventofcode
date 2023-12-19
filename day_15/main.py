print('--- Day 15: Lens Library ---')

with open('input.txt') as f:
    data = f.read().strip().split(',')

def hash(str):
    value = 0
    for character in str:
        value += ord(character)
        value *= 17
        value %= 256
    return value

answer = 0
for d in data:
    answer += hash(d)

print(f'Answer: {answer}')