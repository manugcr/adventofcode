# In the input.txt file there is a list of handful of cubes.
# Each line has this form: Game 100: 16 blue, 12 red, 3 green; 2 green, 7 blue; 5 blue, 4 green; 10 blue, 6 red, 6 green; 5 red, 12 blue, 2 green; 9 red, 12 blue, 11 green
# I need to grab the game number.
# Then i need to grab the number of cubes of each color, and test if there are more than 12 reds, 13 blues or 14 greens.
# Each line contains more than one hand of cubes, delimited by a semicolon.
# if a single hand has more than 12 reds, 13 greens or 14 blues, then the game is invalid.
# If all hands are valid, then the game is valid. And we add the game number to answer variable.
# A game can have more than one hand, and each hand can have the colors in different orders or a color missing.

import re

answer = 0

with open('input.txt', 'r') as file:
    for line in file:
        print('---- Hand ----')
        # Find the game number
        game = (re.search(r'Game \d+', line).group()).split(' ')[1]
        # Find the hands
        hands = re.findall(r'\d+ \w+', line)

        # Check if the game is valid
        valid = True
        for hand in hands:
            # Find the colors and the number of cubes of each color
            colors = re.findall(r'\d+ \w+', hand)
            for color in colors:
                number = int(color.split(' ')[0])
                color = color.split(' ')[1]
                print(color, number)
                if color == 'red' and number > 12:
                    valid = False
                elif color == 'green' and number > 13:
                    valid = False
                elif color == 'blue' and number > 14:
                    valid = False
        
        print(valid)
        if valid:
            answer += int(game)

print(answer)
