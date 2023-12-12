# I need to read the input file and parse through the lines who have this form:
# Card  28: 96 36 98 66 37  8 78 41 55  7 | 77 70 42 37 74  8 96 76 63 64 93 98 78 30 66  1  9 55  7 41 90 29  4 36 22
# Each card has 2 parts, the first part is the numbers that are scratched and the second part is the numbers i have.
# I need to count how many of my numbers are in the scratch part and then depending on the numbers 
# i have it corresponds to the points list.

print('--- Day 4: Scratchcards ---')

points = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
answer = 0

with open('input.txt', 'r') as file:
    data = file.read()
    lines = data.strip().split('\n')

for i, line in enumerate(lines):
    
    # Separate the line into the 2 parts
    scratch, numbers = line.split('|')

    # Separate the numbers into a list of numbers, and a scratch.
    scratch = scratch.strip().split(' ')
    numbers = numbers.strip().split(' ')
    
    # Delete empty spaces in the lists
    while '' in scratch:
        scratch.remove('')
    while '' in numbers:
        numbers.remove('')
    
    count = 0
    for number in numbers:
        if number in scratch:
            count += 1

    print('Card', i, 'has', count, 'winning numbers.')
    answer += points[count]

print('The answer is:', answer)