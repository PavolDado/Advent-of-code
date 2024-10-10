# https://adventofcode.com/2016/day/12

with open('day12-data.txt') as f:
    instructions = f.readlines()

# -------------------------------------
# lesson 1 + lesson 2
# -------------------------------------

def operations(instructionlist: list, registers: dict) -> int:
    instruction = 0

    while instruction in range(len(instructionlist)):
        instructionlist[instruction] = instructionlist[instruction].strip()
        if instructionlist[instruction][:3] == 'cpy':
            value, register = instructionlist[instruction][4:].split()
            if value.isdigit():
                registers[register] = int(value)
            else:
                registers[register] = registers[value]
            instruction += 1
        elif instructionlist[instruction][:3] == 'inc':
            registers[instructionlist[instruction][-1]] += 1
            instruction += 1
        elif instructionlist[instruction][:3] == 'dec':
            registers[instructionlist[instruction][-1]] -= 1
            instruction += 1
        elif instructionlist[instruction][:3] == 'jnz':
            register, value = instructionlist[instruction][4:].split()
            if not register.isdigit():
                if registers[register] != 0:
                    instruction += int(value)
                else:
                    instruction += 1
            else:
                instruction += int(value)
    return registers['a']


# -------------------------------------
# USAGE
# -------------------------------------

# lesson 1
print(operations(instructions, {'a': 0 , 'b':0, 'c':0, 'd':0}))
# lesson 2
print(operations(instructions, {'a': 0 , 'b':0, 'c':1, 'd':0}))
