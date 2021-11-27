from queue import Queue

ALL_OPS = [
    'addr',
    'addi',
    'mulr',
    'muli',
    'banr',
    'bani',
    'borr',
    'bori',
    'setr',
    'seti',
    'gtir',
    'gtri',
    'gtrr',
    'eqir',
    'eqri',
    'eqrr']

def operate(ops,reg, op=None):
    """Takes a list of ints (ops) and a modifies
    a list of ints (regs)"""
    opc,a,b,c=ops
    if op is None:
        global opcode_to_op
        op = opcode_to_op[opc]
    if   op=='addr': reg[c]=reg[a]+reg[b]
    elif op=='addi': reg[c]=reg[a]+b
    elif op=='mulr': reg[c]=reg[a]*reg[b]
    elif op=='muli': reg[c]=reg[a]*b
    elif op=='banr': reg[c]=reg[a]&reg[b]
    elif op=='bani': reg[c]=reg[a]&b
    elif op=='borr': reg[c]=reg[a]|reg[b]
    elif op=='bori': reg[c]=reg[a]|b
    elif op=='setr': reg[c]=reg[a]
    elif op=='seti': reg[c]=a
    elif op=='gtir': reg[c]=int(a>reg[b])
    elif op=='gtri': reg[c]=int(reg[a]>b)
    elif op=='gtrr': reg[c]=int(reg[a]>reg[b])
    elif op=='eqir': reg[c]=int(a==reg[b])
    elif op=='eqri': reg[c]=int(reg[a]==b)
    elif op=='eqrr': reg[c]=int(reg[a]==reg[b])

with open('16.txt') as file:
    data = file.read()

part1,part2 = data.split('\n'*4)
snippets = part1.split('\n\n')
snips = []
for snipet in snippets:
    before,ops,after = snipet.splitlines()
    before_list = eval(before.split(maxsplit=1)[1])
    ops_list = list(map(int, ops.split()))
    after_list = eval(after.split(maxsplit=1)[1])
    snips.append((before_list,ops_list,after_list))

definite_no = {op:set() for op in ALL_OPS}

count_ge3 = 0
for snip in snips:
    og_reg, ops, target = snip
    count=0
    for op in ALL_OPS:
        reg = og_reg.copy()
        operate(ops, reg, op)
        if reg==target:
            count+=1
        else:
            definite_no[op].add(ops[0])
    if count>=3: count_ge3+=1
print('Part 1:',count_ge3)

all_opcodes = {snip[1][0] for snip in snips}  # set(range(16))
opcode_to_op = {}
useful_first = sorted(definite_no.items(), reverse=True, key=(lambda x: len(x[1])))
q = Queue()
for a in useful_first:
    q.put(a)
while not q.empty():
    op, not_opcode = q.get_nowait()
    candidates = all_opcodes-not_opcode
    if len(candidates)==1:
        opcode ,= candidates
        opcode_to_op[opcode]=op
        all_opcodes.discard(opcode)
    else:
        q.put((op, not_opcode))

reg = [0]*4
for line in part2.splitlines():
    ops = list(map(int,line.split()))
    operate(ops,reg)
print('Part 2:',reg[0])