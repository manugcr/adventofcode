print('--- Day 19: Aplenty ---')

operators = {
    '>': int.__gt__,
    '<': int.__lt__,
}

def accept(item, name = 'in'):
    if name == 'R':
        return False
    if name == 'A':
        return True
    
    rules, fallback = workflows[name]
    for key, cond, num, target in rules:
        if operators[cond](item[key], num):
            return accept(item, target)
        
    return accept(item, fallback)

with open('input.txt', 'r') as file:
    block1, block2 = file.read().split('\n\n')

workflows = {}
for line in block1.split('\n'):
    name, rest = line[:-1].split('{')
    rules = rest.split(',')
    workflows[name] = ([], rules.pop())
    for rule in rules:
        conditional, target = rule.split(':')
        key = conditional[0]
        cond = conditional[1]
        num = int(conditional[2:])
        workflows[name][0].append((key, cond, num, target))

# Process items
answer = 0
for line in block2.splitlines():
    item = {}
    for segment in line[1:-1].split(','):
        char, num = segment.split('=')
        item[char] = int(num)
    if accept(item):
        answer += sum(item.values())

print(f'Answer: {answer}') 