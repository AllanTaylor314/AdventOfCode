def print_boolmap():
    global bool_map
    print('                                1111111111')
    print('                      01234567890123456789')
    for field,valids in bool_map.items():
        print(f"{field:20}: {''.join(map(' #@'.__getitem__,valids))}")

def try_horiz():
    global bool_map
    global field_index
    solved_something = False
    for field,valids in bool_map.items():
        if sum(valids)==1:
            solved_something = True
            new_index = valids.index(1)
            valids[new_index]=2
            field_index[field]=new_index
            for other_field in bool_map:
                if other_field!=field:
                    bool_map[other_field][new_index]=0
    return solved_something

with open('16.txt', encoding='utf-8') as file:
    raw_data = file.read()
    rules,my_ticket_str,other_tickets = raw_data.split("\n\n")

ruleset_dict = {}
global_ruleset = set()  # Valid field values
for rule in rules.splitlines():
    key,cond = rule.split(':')
    a_range,_,b_range = cond.split()
    a0,a1 = a_range.split('-')
    b0,b1 = b_range.split('-')
    ruleset = set(range(int(a0),int(a1)+1))|set(range(int(b0),int(b1)+1))
    global_ruleset|=ruleset
    ruleset_dict[key] = ruleset

my_ticket = list(map(int,my_ticket_str.splitlines()[1].split(',')))
all_tickets = [my_ticket]
for ticket in other_tickets.splitlines()[1:]:
    all_tickets.append(list(map(int,ticket.split(','))))

valid_tickets = []

invalids = 0
for ticket in all_tickets:
    invalid_set = set(ticket)-global_ruleset
    if invalid_set:
        invalids+=sum(invalid_set)
    else:
        valid_tickets.append(ticket)
print("Part 1:",invalids)

columns = list(map(set,zip(*valid_tickets)))
bool_map = {field:[1]*len(my_ticket) for field in ruleset_dict}
for i,column in enumerate(columns):
    for field,valid_values in ruleset_dict.items():
        if column-valid_values:
            bool_map[field][i]=0

print_boolmap()

field_index = {}  # Definitive solutions
while try_horiz():
    pass

print_boolmap()

solution = 1
for field in field_index:
    if field.startswith('departure'):
        solution*=my_ticket[field_index[field]]
print('Part 2:',solution)