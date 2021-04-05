def lines_from_file(filename):
    """ Returns a list of lines from the given file."""
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def print_display():
    for row in screen:
        print("".join(row))


def cmd_rect(w, h):
    for i in range(min(h, len(screen))):
        for j in range(min(w, len(screen[0]))):
            screen[i][j] = '#'


def rotate_row(row, shift):
    current_row = screen[row]
    new_row = current_row[-shift:] + current_row[:-shift]
    screen[row] = new_row


def rotate_column(col, shift):
    current_col = []
    for row in screen:
        current_col.append(row[col])
    new_col = current_col[-shift:] + current_col[:-shift]
    for i in range(len(current_col)):
        screen[i][col] = new_col[i]


lines = lines_from_file('08.txt')
screen = [[' ' for i in range(50)] for j in range(6)]
for line in lines:
    cmd, *args = line.split(" ")
    if cmd == 'rect':
        w, h = args[0].split('x')
        cmd_rect(int(w), int(h))
    else:  # rotate
        rc = int(args[1].split('=')[1])
        shift = int(args[3])
        if args[0] == 'row':
            rotate_row(rc, shift)
        else:
            rotate_column(rc, shift)
    #print(cmd, args)
    # print(line)
print_display()
# print()
count = 0
for row in screen:
    count += row.count('#')
print(count)
