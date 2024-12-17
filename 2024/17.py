from itertools import count
import os
from pathlib import Path
from time import perf_counter
import re
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
DIRECTIONS = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,1)][::2]
def add(*ps): return tuple(map(sum,zip(*ps)))
timer_parse_start=perf_counter()
############################## PARSER ##############################
with open(INPUT_PATH) as file:
    data = file.read()
RegisterA,RegisterB,RegisterC,*Program = map(int,re.findall(r"\d+",data))
# RegisterA, Program = 729, [0,1,5,4,3,0]

timer_parse_end=timer_part1_start=perf_counter()
############################## PART 1 ##############################

def run_program(A=RegisterA, B=0, C=0):
    def get_combo_operand(operand):
        if operand < 4:
            return operand
        if operand == 4:
            return A
        if operand == 5:
            return B
        if operand == 6:
            return C
        raise ValueError(f"Invalid {operand = }")
    ip = 0
    Output = []
    while 0 <= ip < len(Program):
        opcode = Program[ip]
        operand = Program[ip+1]
        if opcode == 0: # adv
            A >>= get_combo_operand(operand)
        elif opcode == 1: # bxl
            B ^= operand # literal
        elif opcode == 2: # bst
            B = get_combo_operand(operand) % 8
        elif opcode == 3: # jnz
            if A != 0:
                ip = operand
                continue
        elif opcode == 4: # bxc
            B ^= C
        elif opcode == 5: # out
            Output.append(get_combo_operand(operand) % 8)
            if len(Output) > len(Program):
                return
        elif opcode == 6: # bdv
            B = A >> get_combo_operand(operand)
        elif opcode == 7: # cdv
            C = A >> get_combo_operand(operand)
        ip += 2
    return ",".join(map(str,Output))

p1 = run_program()
print("Part 1:",p1) # not 0,5,1,2,5,0,2,3,1
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
# target = ",".join(map(str,Program))
# for p2 in count(): # just a casual 10**14 iterations...
#     print(p2,end="\r")
#     if run_program(p2) == target:
#         break
# print("Part 2:",p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
