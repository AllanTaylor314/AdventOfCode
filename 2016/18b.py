NUM_ROWS = 400000
first_row = ".^^^.^.^^^.^.......^^.^^^^.^^^^..^^^^^.^.^^^..^^.^.^^..^.^..^^...^.^^.^^^...^^.^.^^^..^^^^.....^...."
#first_row = '..^^.'
# . is safe, ^ is trap
rows = [first_row]
trap_set = {'^^.', '.^^', '^..', '..^'}
total_safe = first_row.count('.')
while len(rows) < NUM_ROWS:
    current_row = '.' + rows[-1] + '.'  # imaginary safe start and end
    new_row = ''
    for i in range(1, len(current_row) - 1):
        new_row += ('^' if current_row[i - 1:i + 2] in trap_set else '.')
    rows.append(new_row)
    total_safe += new_row.count('.')

print(total_safe)
