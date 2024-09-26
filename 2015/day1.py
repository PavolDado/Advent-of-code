# https://adventofcode.com/2015/day/1

inpfile = 'input1.txt'

# -------------------------------------
# lesson 1
# -------------------------------------

def load_file(infile):
    with open(infile) as infile:
        return infile.readlines()


def counter(infile):
    floor = 0
    lines = load_file(infile)
    for line in lines:
        for char in line:
            if char in '()':
                if char == '(':
                    floor += 1
                else:
                    floor -= 1
    return floor

# -------------------------------------
# lesson 2
# -------------------------------------

def counter2(infile):
    floor = 0
    lines = load_file(infile)
    for line in lines:
        for i in range(len(line)):
            if line[i] in '()':
                if line[i] == '(':
                    floor += 1
                else:
                    floor -= 1
                if floor == -1:
                    return i + 1

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(counter(inpfile))
# lesson 2
print(counter2(inpfile))
