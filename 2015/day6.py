# https://adventofcode.com/2015/day/6

with open('ziarovky.txt') as f:
    testlist = f.readlines()

# -------------------------------------
# lesson 1
# -------------------------------------

size = 1000
matrix = [[0 for x in range(size)] for y in range(size) ]

def switcher(testlist, matrix) :
    for line in testlist :
        a = line.split()
        start_x , start_y = a[-3].split(',')
        end_x, end_y = a[-1].split(',')
        
        if int(start_x) > int(end_x):
            end_x, start_x = start_x, end_x
        if int(start_y) > int(end_y):
            end_y, start_y = start_y, end_y
        
        for x_coord in range(int(start_x), int(end_x)+1):
            for y_coord in range(int(start_y), int(end_y)+1):
                if 'urn on' in line:
                    matrix[x_coord][y_coord] = 1
                elif 'urn off' in line:
                    matrix[x_coord][y_coord] = 0
                elif 'oggle' in line:
                    if matrix[x_coord][y_coord] == 1:
                        matrix[x_coord][y_coord] = 0
                    else:
                        matrix[x_coord][y_coord] = 1
    return matrix

    
def counter(matrix):
    total = 0
    for i in matrix:
        a = i.count(1)
        total += a
    return total

# -------------------------------------
# lesson 2
# -------------------------------------

matrix = [[0 for x in range(size)] for y in range(size)]

def increaser(testlist, matrix) :
    for line in testlist :
        a = line.split()
        start_x , start_y = a[-3].split(',')
        end_x, end_y = a[-1].split(',')
        
        if int(start_x) > int(end_x):
            end_x, start_x = start_x, end_x
        if int(start_y) > int(end_y):
            end_y, start_y = start_y, end_y
        
        for x_coord in range(int(start_x), int(end_x)+1):
            for y_coord in range(int(start_y), int(end_y)+1):
                if 'urn on' in line:
                    matrix[x_coord][y_coord] += 1
                elif 'urn off' in line:
                    matrix[x_coord][y_coord] -= 1
                    if matrix[x_coord][y_coord] < 0:
                        matrix[x_coord][y_coord] = 0
                elif 'oggle' in line:
                    matrix[x_coord][y_coord] += 2
    return matrix


def increaser_counter(matrix):
    total = 0
    for i in matrix:
        total += sum(i)
    return total

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(counter(switcher(testlist, matrix)))
# lesson 2
print(increaser_counter(increaser(testlist, matrix)))
