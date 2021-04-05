def lines_from_file(filename):
    """ Returns a list of lines from the given file."""
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


commands = lines_from_file('10.txt')
bots = {}  # [a,b]
comps = {}
# bot#:('o/b low',ob_low_id,'o/b high',ob_high_id)
outs = {}
for instruction in commands:
    cmd = instruction.split(" ")
    if cmd[0] == 'value':
        bots[int(cmd[-1])] = bots.get(int(cmd[-1]), []) + [int(cmd[1])]
    else:
        comps[int(cmd[1])] = (cmd[5], int(cmd[6]), cmd[10], int(cmd[11]))

while True:
    ids = list(bots.keys())
    for bot_id in ids:
        bot_chips = bots.get(bot_id, [])
        if len(bot_chips) == 2:
            if 61 in bot_chips and 17 in bot_chips:
                print(bot_id, "compares 61 and 17")
                quit()
            comp = comps[bot_id]
            if comp[0] == 'bot' and len(bots.get(comp[1], [])) == 2:
                # Skip this bot (for now) if the target already has two
                continue
            if comp[2] == 'bot' and len(bots.get(comp[3], [])) == 2:
                # Skip this bot (for now) if the target already has two
                continue
            if comp[0] == 'bot':
                bots[comp[1]] = bots.get(comp[1], []) + [min(bot_chips)]
            else:
                outs[comp[1]] = outs.get(comp[1], []) + [min(bot_chips)]
            if comp[2] == 'bot':
                bots[comp[3]] = bots.get(comp[3], []) + [max(bot_chips)]
            else:
                outs[comp[3]] = outs.get(comp[3], []) + [max(bot_chips)]
            bots[bot_id] = []
    # print(bots)
