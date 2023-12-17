# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

print('--- Day 7: Camel Cards ---')

# with open('input.txt', 'r') as file:
#     lines = file.read().strip().split('\n')

# def value(card):
#     return '23456789TJQKA'.index(card)

# def get_count(hand):
#     counts = {}
#     for card in hand:
#         if card not in counts:
#             counts[card] = 0
#         counts[card] += 1
#     return sorted(counts.values(), reverse=True)

# def tiebreak(hand):
#     sc = hand
#     sc.extend([value(x) for x in hand])
#     return sc

# hands = []
# for line in lines:
#     hand, bid = line.split(' ')
#     hands.append((tiebreak(hand), hand, int(bid)))
# hands.sort()

import collections
lines = [i for i in open('input.txt').read().split('\n') if i.strip()]
def hand(h,part1):
    if part1: h = h.replace('J', 'X')
    h2 = ['J23456789TXQKA'.index(i)for i in h]
    ts = []
    for r in '23456789TQKA':
        c = collections.Counter(h.replace('J', r))
        p = tuple(sorted(c.values()))
        t = [(1,1,1,1,1),(1,1,1,2),(1,2,2),(1,1,3),(2,3),(1,4),(5,)].index(p)
        ts.append(t)
    return (max(ts), *h2)
for part1 in (True, False):
    h = sorted((hand(h,part1), int(b)) for h, b in (l.split() for l in lines))
    t = 0
    for i,(_,b) in enumerate(h):
        t+=i*b+b
    print('Part', 2-part1, ':', t)
