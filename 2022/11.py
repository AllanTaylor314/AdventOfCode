class Monkey:
    monkeys = []
    def __init__(self, items: list[int], operation, test, iftrue, iffalse):
        self.items = list(items)
        self.op = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.inspections = 0
    @classmethod
    def parse_block(cls, block):
        l_id, l_start, l_op, l_test, l_true, l_false = block.splitlines()
        _,items = l_start.split(": ")
        op = eval("lambda old:"+l_op.split("=")[1])
        test = lambda x: x%int(l_test.split()[-1])==0
        return cls(map(int,items.split(", ")),op,test,int(l_true.split()[-1]),int(l_false.split()[-1]))
    def turn(self):
        for item in self.items:
            self.inspections+=1
            worry = self.op(item)//3
            if self.test(worry):
                self.monkeys[self.iftrue].items.append(worry)
            else:
                self.monkeys[self.iffalse].items.append(worry)
        self.items.clear()

with open("11.txt") as file:
    blocks = file.read().split("\n\n")

Monkey.monkeys.extend(Monkey.parse_block(block) for block in blocks)

for r in range(20):
    for m in Monkey.monkeys:
        m.turn()
*_,beta,alpha=sorted(Monkey.monkeys, key=lambda m:m.inspections)
print("Part 1:",alpha.inspections*beta.inspections)
p2 = 0

print("Part 2:",p2)
