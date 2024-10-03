# https://adventofcode.com/2023/day/1

infile = 'input.txt'
infile2 = 'input2.txt'

# -------------------------------------
# lesson 1
# -------------------------------------

def load_file(infile):
    with open(infile) as infile:
        return infile.readlines()


def find_line_value(line):
    matrix = '0123456789'
    value = ''
    for i in line:
        if i in matrix:
            value += i
            break
    for i in line[::-1]:
        if i in matrix:
            value += i
            break
    return value


def calculate_result(infile):
    result = 0
    result_array = [find_line_value(line) for line in load_file(infile)]
    for i in result_array:
        result += int(i)
    return result
    
# -------------------------------------
# lesson 2
# -------------------------------------

def value_search(line):
    a = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    matrix = '123456789'
    number_index = [letter for letter in range(len(line)) if line[letter] in matrix]
    word_index = {}
    first = ''
    second = ''
    for lett in range(len(line)):
        for k, v in a.items():
            l = line.find(k)
            r = line.rfind(k)
            if l >= 0:
                word_index[l] = v
            if r >= 0:
                word_index[r] = v
    sorted_word_index = dict(sorted(word_index.items()))
    # print(line, number_index, sorted_word_index)
    if number_index and word_index:
        if number_index[0] < list(sorted_word_index)[0]:
            first = line[number_index[0]]
        else:
            first = list(sorted_word_index.values())[0]
        if number_index[-1] > list(sorted_word_index)[-1]:
            second = line[number_index[-1]]
        else:
            second = list(sorted_word_index.values())[-1]
    elif number_index and not word_index:
        first = line[number_index[0]]
        second = line[number_index[-1]]
    elif not number_index and word_index:
        first = list(sorted_word_index.values())[0]
        second = list(sorted_word_index.values())[-1]        
    else:
        first = 0
        second = 0
    # print(str(first) + str(second))
    return str(first) + str(second)


def word_to_digit(infile):
    lines = load_file(infile)
    result = 0
    for line in lines:
        value = value_search(line)
        result += int(value)
    return result

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(calculate_result(infile))
# lesson 2
print(word_to_digit(infile2))
