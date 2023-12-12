print('--- Day 3: Gear Ratios ---')

answer = 0

# Open file, read lines and store them in a list.
with open('input.txt', 'r') as file:
    data = file.read()
    lines = data.strip().split('\n')

# Check if the given coordinates are valid and if the character is a symbol.
def is_symbol(i, j):
    if not (0 <= i < len(lines) and 0 <= j < len(lines[0])):
        return False

    return lines[i][j] != "." and not lines[i][j].isdigit()

# Iterate over the lines and check if the current character is a number.
# If it is, check if it is adjacent to a symbol, if it is, add it to the answer.
for i, line in enumerate(lines):
    start = 0 
    column = 0

    while column < len(line):
        start = column
        num = ''

        # Grab a whole number parsing through the string.
        while column < len(line) and line[column].isdigit():
            num += line[column]
            column += 1

        if num == '':
            print(column, line[column])
            column += 1
            continue

        num = int(num)

        if is_symbol(i, start-1) or is_symbol(i, column):
            answer += num
            column += 1
            continue

        for k in range(start-1, column+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                answer += num
                break
        
print('The answer is:', answer)