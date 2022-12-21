import sympy as sp
from sympy.parsing.sympy_parser import parse_expr
with open("21.txt") as file:
    lines = file.read().splitlines()
monkeys = {}
for line in lines:
    name,ops = line.split(": ")
    try:ops=int(ops)
    except ValueError:pass
    monkeys[name]=ops
def solve(name):
    if isinstance(monkeys[name],(int,sp.Symbol,sp.Integer)):
        return monkeys[name]
    name1, op, name2 = monkeys[name].split()
    return (parse_expr(f"({solve(name1)}) {op} ({solve(name2)})")) # THESE BRACKETS!!!!
print("Part 1:",int(solve("root")))
left,_,right = monkeys["root"].split()
monkeys["humn"]=humn=sp.Symbol("humn")
print("Part 2:",*sp.solve(solve(left)-solve(right),humn))
