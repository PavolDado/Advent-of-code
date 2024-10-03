# https://adventofcode.com/2023/day/2

infile = 'input1.txt'

# -------------------------------------
# lesson 1
# -------------------------------------

def load_file(infile):
    with open(infile) as infile:
        return infile.readlines()


def parse_line(line):
    game_name, games = line.split(':')
    return game_name, games.strip()


def parse_game(games):
    game = games.split(';')
    return game


def grab(game):
    grab_counter = len(game)
    tmp_counter = 0
    for grab in game:
        tmp_grabs = 0
        cubes = grab.split(',')
        for cube in cubes:
            count, colour = cube.split()
            if colour in ['red', 'green', 'blue']:
                if colour == 'red' and int(count) <= 12:
                    tmp_grabs += 1
                elif colour == 'green' and int(count) <= 13:
                    tmp_grabs += 1
                elif colour == 'blue' and int(count) <= 14:
                    tmp_grabs += 1
                else:
                    tmp_grabs = 0
            if tmp_grabs == len(cubes):
                tmp_counter += 1
    return tmp_counter == grab_counter


def main_loop(infile):
    result = 0
    for line in load_file(infile):
        game_name, games = parse_line(line)
        game = parse_game(games)
        if grab(game):
            id_name, id_num = game_name.split()
            result += int(id_num)
    return result

# -------------------------------------
# lesson 2
# -------------------------------------

def counter(game):
    red, green, blue = 0,0,0
    for grab in game:
        cubes = grab.split(',')
        for cube in cubes:
            count, colour = cube.split()
            if colour == 'red':
                if red < int(count):
                    red = int(count)
            if colour == 'green':
                if green < int(count):
                    green = int(count)
            if colour == 'blue':
                if blue < int(count):
                    blue = int(count)
    return red * green * blue


def main_loop2(infile):
    result = 0
    for line in load_file(infile):
        game_name, games = parse_line(line)
        game = parse_game(games)
        result += counter(game)
    return result

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(main_loop(infile))
# lesson 2
print(main_loop2(infile))
