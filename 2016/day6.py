# https://adventofcode.com/2016/day/6

with open('day6.txt') as f:
    lines = f.readlines()

# -----------------------------------
#          part 1
# -----------------------------------

def analyze(indata):
    main_dict = {}
    for line in lines:
        line = line.strip()
        for position in range(len(line)):
            if position not in main_dict.keys():
                main_dict[position] = {}
            if line[position] in main_dict[position].keys():
                main_dict[position][line[position]] += 1
            else:
                main_dict[position][line[position]] = 1
    return main_dict


def error_correction(inputdata):
    message = ''
    for letter in inputdata.values():
        max_key = [key  for (key, value) in letter.items() if value == max(letter.values())]
        message += max_key[0]
    return message


# --------------------------------------
#         part 2
# --------------------------------------

def error_correction_min(inputdata):
    message = ''
    for letter in inputdata.values():
        min_key = [key  for (key, value) in letter.items() if value == min(letter.values())]
        message += min_key[0]
    return message


# -------------------------------------
# USAGE
# -------------------------------------

# part 1
print(error_correction(analyze(lines)))
# part 2
print(error_correction_min(analyze(lines)))
