# https://adventofcode.com/2015/day/2

inpfile = 'input1.txt'

# -------------------------------------
# lesson 1
# -------------------------------------

def load_file(infile):
    with open(infile) as infile:
        return infile.readlines()


def paper_counter(line):
    tmp_line = line.strip()
    length, width, height = tmp_line.split('x')
    side_l = int(length) * int(width)
    side_w = int(width) * int(height)
    side_h = int(height) * int(length)
    total_present_paper = 2 * side_h + 2* side_l + 2* side_w + min(side_w, side_h, side_l)
    return total_present_paper


def sorted_sides(l, h, w):
    return sorted([l, h, w])


def total(infile):
    total_paper = 0
    lines = load_file(infile)
    for line in lines:
        total_paper += paper_counter(line)
    return total_paper

# -------------------------------------
# part 2
# -------------------------------------

def ribbon_counter(line):
    tmp_line = line.strip()
    length, width, height = tmp_line.split('x')
    side_l = int(length)
    side_w = int(width)
    side_h = int(height)
    smallest = sorted_sides(side_l, side_h, side_w)
    total_present_ribbon = side_l * side_h * side_w + (2 * smallest[0] + 2 * smallest[1])
    return total_present_ribbon


def total2(infile):
    total_ribbon = 0
    lines = load_file(infile)
    for line in lines:
        total_ribbon += ribbon_counter(line)
    return total_ribbon

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(total(inpfile))
# lesson 2
print(total2(inpfile))
