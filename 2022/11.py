from math import lcm
PART2 = True

class Monkey:
    monkeys = []
    modulo = 1 # This is the clever trick for part 2
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
        test = int(l_test.split()[-1])
        cls.modulo = lcm(cls.modulo,test)
        return cls(map(int,items.split(", ")),op,test,int(l_true.split()[-1]),int(l_false.split()[-1]))
    def turn(self):
        for item in self.items:
            self.inspections+=1
            worry = self.op(item)
            if not PART2:worry//=3
            worry%=self.modulo
            if worry%self.test==0:
                self.monkeys[self.iftrue].items.append(worry)
            else:
                self.monkeys[self.iffalse].items.append(worry)
        self.items.clear()
    def __repr__(self):
        return f"<%{self.test}: t->{self.iftrue}, f->{self.iffalse} {self.items}>"

with open("11.txt") as file:
    blocks = file.read().split("\n\n")

Monkey.monkeys.extend(Monkey.parse_block(block) for block in blocks)
for r in range(10_000 if PART2 else 20):
    for m in Monkey.monkeys:
        m.turn()
*_,beta,alpha=sorted(Monkey.monkeys, key=lambda m:m.inspections)
print(f"Part {1+PART2}:",alpha.inspections*beta.inspections)
