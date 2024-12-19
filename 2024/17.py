from itertools import count
import os
from pathlib import Path
from time import perf_counter
import re
import z3
timer_script_start=perf_counter()
SCRIPT_PATH=Path(os.path.realpath(__file__))
INPUT_PATH=SCRIPT_PATH.parent.parent/"inputs"/Path(SCRIPT_PATH.parent.name,SCRIPT_PATH.stem+".txt")
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
print("Part 1:",p1)
timer_part1_end=timer_part2_start=perf_counter()
############################## PART 2 ##############################
s = z3.Solver()
original_A = A = z3.BitVec("A",len(Program)*3+7)
X, Y = (b for a,b in zip(Program[::2],Program[1::2]) if a == 1)
for target_out in Program:
    C = A >> (A & 0b111 ^ X)
    B = A ^ X ^ Y ^ C
    s.add(B & 0b111 == target_out)
    A >>= 3
s.add(A==0)
while s.check() == z3.sat:
    p2 = s.model()[original_A].as_long()
    s.add(original_A < p2)
print("Part 2:", p2)
timer_part2_end=timer_script_end=perf_counter()
print(f"""Execution times (sec)
Parse: {timer_parse_end-timer_parse_start:3.3f}
Part1: {timer_part1_end-timer_part1_start:3.3f}
Part2: {timer_part2_end-timer_part2_start:3.3f}
Total: {timer_script_end-timer_script_start:3.3f}""")
