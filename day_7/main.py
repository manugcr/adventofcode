print('--- Day 7: Camel Cards ---')

with open('input.txt') as file:
    lines = file.read().strip().split('\n')

# Every hand is exactly one type. From strongest to weakest, they are:

#     Five of a kind, where all five cards have the same label: AAAAA
#     Four of a kind, where four cards have the same label and one card has a different label: AA8AA
#     Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
#     Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
#     Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
#     One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
#     High card, where all cards' labels are distinct: 23456
def get_type(hand):
    # Five of a kind
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return 'Five of a kind'
    # Four of a kind
    elif hand[0] == hand[1] == hand[3] == hand[4] or hand[1] == hand[2] == hand[3] == hand[4]:
        return 'Four of a kind'
    # Full house
    elif hand[0] == hand[1] == hand[2] and hand[3] == hand[4] or hand[0] == hand[1] and hand[2] == hand[3] == hand[4]:
        return 'Full house'
    # Three of a kind
    elif hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
        return 'Three of a kind'
    # Two pair
    elif hand[0] == hand[1] and hand[2] == hand[3] or hand[0] == hand[1] and hand[3] == hand[4] or hand[1] == hand[2] and hand[3] == hand[4]:
        return 'Two pair'
    # One pair
    elif hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        return 'One pair'
    # High card
    else:
        return 'High card'


for i, line in enumerate(lines):
    hand = line.split(' ')[0]
    bid = line.split(' ')[1]

    print(hand, bid)