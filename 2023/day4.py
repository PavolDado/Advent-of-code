# https://adventofcode.com/2023/day/4

with open('day4-data.txt') as f:
    indata = f.readlines()

# -------------------------------------
# lesson 1
# -------------------------------------

def card_points(card):
    tmp_winning, having= card.split('|')
    winning = tmp_winning.split(':')
    all_winning = winning[1].split()
    all_having = having.split()
    points = 0
    for wn in all_winning:
        if wn in all_having:
            if points:
                points *= 2
            else:
                points = 1
    return points


def point_counter(inp):
    points = 0
    for card_data in inp:
        points += card_points(card_data.strip())
    return points

# -------------------------------------
# lesson 2
# -------------------------------------

def calc_copy(card):
    tmp_winning, having= card.split('|')
    winning = tmp_winning.split(':')
    all_winning = winning[1].split()
    all_having = having.split()
    wn = 0
    for i in all_winning:
        if i in all_having:
            wn += 1
    return wn


def card_counter(inp):
    shadow = [1 for x in range(len(inp))]
    pos = 0
    for pos in range(len(inp)):
        for repeating in range(shadow[pos]):
            for card in range(pos + 1, pos + 1 + calc_copy(inp[pos])):
                shadow[card] += 1
        pos += 1
    return sum(shadow)

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(point_counter(indata))
# lesson 2
print(card_counter(indata))
