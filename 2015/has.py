# https://adventofcode.com/2015/day/4

import hashlib

def hashfinder(start_string, length):
    found = False
    counter = 0
    while not found:
        test_string = start_string + str(counter)
        tmp_hash = hashlib.md5(test_string.encode('utf-8')).hexdigest()
        if tmp_hash.startswith(length):
            return counter
        counter += 1

# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(hashfinder('iwrupvqb', '00000'))
# lesson 2
print(hashfinder('iwrupvqb', '000000'))
