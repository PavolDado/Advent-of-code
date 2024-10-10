# https://adventofcode.com/2016/day/5
import hashlib

door_id = 'cxdnnyjw'
index = 0

# -----------------------------------
#          part 1
# -----------------------------------

def hashing(door_id, index):
    not_found = True

    while not_found:
        tmp_pwd = door_id + str(index)
        password = hashlib.md5(tmp_pwd.encode()).hexdigest()
        if password.startswith('00000'):
            return password[5], index
        index += 1


def password_generator(door_id, index):
    final_password = ''

    for i in range(8):
        letter, index = hashing(door_id, index + 1)
        final_password += letter

    return final_password


# -----------------------------------------------------
#                part 2
# -----------------------------------------------------

def hashing_p2(door_id, index):
    not_found = True

    while not_found:
        tmp_pwd = door_id + str(index)
        password = hashlib.md5(tmp_pwd.encode()).hexdigest()
        if password.startswith('00000'):
            return password[5], password[6], index
        index += 1


def generator_p2(door_id, index):
    password_matrix = '________'
    list_password_matrix = list(password_matrix)

    while '_' in list_password_matrix:
        position, letter, index = hashing_p2(door_id, index + 1)
        if position.isnumeric():
            if int(position) in range(len(list_password_matrix)) and list_password_matrix[int(position)] == '_':
                list_password_matrix[int(position)] = str(letter)

    password_matrix = ''.join(list_password_matrix)
    return password_matrix


# -------------------------------------
# USAGE
# -------------------------------------

# part 1
print(password_generator(door_id, index))
# part 2
print(generator_p2(door_id, index))
