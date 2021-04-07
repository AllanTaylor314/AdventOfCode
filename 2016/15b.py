def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def disc_pos(disc_id, time):
    """Returns position of disc after time seconds"""
    positions, start = disc_info[disc_id]
    return (start + time) % positions


lines = lines_from_file('15.txt')
# lines = ["Disc #1 has 5 positions; at time=0, it is at position 4.",
#         "Disc #2 has 2 positions; at time=0, it is at position 1."]
disc_info = {}
for line in lines:
    data = line.split()
    disc_info[int(data[1][1:])] = (int(data[3]), int(data[-1][:-1]))

disc_info[max(disc_info.keys()) + 1] = (11, 0)
initial_time = -1
is_solved = False
max_key = max(disc_info.keys())
while not is_solved:
    initial_time += 1
    positions = 0
    for disc_id in disc_info.keys():
        if disc_pos(disc_id, initial_time + disc_id) == 0:
            positions += 1
    # print(initial_time, positions)
    if positions == max_key:
        is_solved = True
    if initial_time % 10000 == 0:
        print(initial_time)

print(f"Starting at time={initial_time}:")
for disc_id in disc_info.keys():
    time = initial_time + disc_id
    print(f"#{disc_id} is at {disc_pos(disc_id, time)} (time={time})")
