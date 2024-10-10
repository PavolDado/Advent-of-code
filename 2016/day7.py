# https://adventofcode.com/2016/day/7

with open('/2016/day7-data.txt') as f:
    lines = f.readlines()

# -----------------------------------
#          part 1
# -----------------------------------

def abba(code):
    if len(code) > 3:
        for letter in range(3, len(code)):
            if code[letter-3] == code[letter]:
                if code[letter-2] == code[letter-1]:
                    if code[letter-1] != code[letter]:
                        return True
    return False


def data_creator(line):
    newline = line.replace(']','[')
    adress_datalist = newline.split('[')
    outer_data = []
    inner_data = []

    for i in range(len(adress_datalist)):
        if i % 2 == 0:
            outer_data.append(adress_datalist[i])
        else:
            inner_data.append(adress_datalist[i])
    return outer_data, inner_data


def conditions(line):
    outer_data, inner_data = data_creator(line)
    if any(abba(outer) for outer in outer_data) and not any(abba(inner) for inner in inner_data):
        return True
    return False


def analyze_ip_tls(lines):
    totals = 0
    for line in lines:
        if conditions(line):
            totals += 1
    return totals


# -----------------------------------
#          part 2
# -----------------------------------

def conditions_ssl(line):
    x = ','
    outer_data, inner_data = data_creator(line)
    outer_line = x.join(outer_data)
    inner_line = x.join(inner_data)

    for i in range(3, len(outer_line)):
        tmp_string = outer_line[i-3:i]
        if ',' not in tmp_string:
            if tmp_string[0] == tmp_string[-1] and tmp_string[0] != tmp_string[1]:
                searchstring = tmp_string[1] + tmp_string[0] + tmp_string[1]
                if searchstring in inner_line:
                    return True
    return False


def analyze_ip_ssl(lines):
    totals = 0
    for line in lines:
        if conditions_ssl(line):
            totals += 1
    return totals


# -------------------------------------
# USAGE
# -------------------------------------

# part 1
print(analyze_ip_tls(lines))
# part 2
print(analyze_ip_ssl(lines))
