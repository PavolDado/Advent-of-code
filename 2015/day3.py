# https://adventofcode.com/2015/day/3

inpfile = 'input.txt'
inpfile2 = 'input2.txt'

# -------------------------------------
# lesson 1
# -------------------------------------

def load_file(infile):
    with open(infile) as infile:
        return infile.readlines()


def coord_translator(lines):
    x = 0
    y = 0
    houses = {0:{0:1}}

    for line in lines:
        for letter in line:
            if letter in '^v><':
                if letter == '^':
                    y += 1
                if letter == 'v':
                    y -= 1
                if letter == '>':
                    x += 1
                if letter == '<':
                    x -= 1
                if y in houses:
                    if x in houses[y]:
                        houses[y][x] += 1
                    else:
                        houses[y].update({x:1})  
                else:
                    houses.update({y:{x:1}})
    return houses


def counter(infile):
    lines = load_file(infile)
    sum_of_gifts = 0
    visited_houses = coord_translator(lines)
    # print(visited_houses)
    for houses in visited_houses.values():
        for gift in houses.values():
            sum_of_gifts += 1
    return sum_of_gifts

# -------------------------------------
# lesson 2
# -------------------------------------

def coord_translator_robo_santa(lines):
    coord_counter = 0
    x = 0
    y = 0
    santa_x = 0
    santa_y = 0
    robo_santa_x = 0
    robo_santa_y = 0
    santa_houses = {0:{0:1}}
    robo_santa_houses = {0:{0:1}}

    for line in lines:
        for letter in line:
            if letter in '^v><':
                if letter == '^':
                    y += 1
                if letter == 'v':
                    y -= 1
                if letter == '>':
                    x += 1
                if letter == '<':
                    x -= 1

                if coord_counter % 2 == 0:
                    santa_x += x
                    santa_y += y
                    if santa_y in santa_houses:
                        if santa_x in santa_houses[santa_y]:
                            santa_houses[santa_y][santa_x] += 1
                        else:
                            santa_houses[santa_y].update({santa_x:1})  
                    else:
                        santa_houses.update({santa_y:{santa_x:1}})
                else:
                    robo_santa_x += x
                    robo_santa_y += y
                    if robo_santa_y in robo_santa_houses:
                        if robo_santa_x in robo_santa_houses[robo_santa_y]:
                            robo_santa_houses[robo_santa_y][robo_santa_x] += 1
                        else:
                            robo_santa_houses[robo_santa_y].update({robo_santa_x:1})  
                    else:
                        robo_santa_houses.update({robo_santa_y:{robo_santa_x:1}})
                x = 0
                y = 0
                coord_counter += 1
    return {0:santa_houses, 1:robo_santa_houses}


def counter_robo_santa(infile):
    lines = load_file(infile)
    sum_of_gifts = 0
    visited_houses = coord_translator_robo_santa(lines)

    for houses in visited_houses[0].values():
        for gift in houses.values():
            sum_of_gifts += 1

    for house_k in visited_houses[1].keys():
        if house_k not in visited_houses[0].keys():
            for gift_k in visited_houses[1][house_k]:
                sum_of_gifts += 1
        else:
            for gift_k in visited_houses[1][house_k]:
                if gift_k not in visited_houses[0][house_k]:
                    sum_of_gifts += 1

    return sum_of_gifts

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(counter(inpfile))
# lesson 2
print(counter_robo_santa(inpfile))
