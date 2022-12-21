with open("21.txt") as file:
    lines = file.read().splitlines()
monkeys = {}
for line in lines:
    name,ops = line.split(": ")
    if ops.isdigit():
        ops=int(ops)
    monkeys[name]=ops
def solve(name):
    if isinstance(monkeys[name],int):
        return monkeys[name]
    name1, op, name2 = monkeys[name].split()
    return int(eval(f"{solve(name1)} {op} {solve(name2)}"))
print("Part 1:",solve("root"))

