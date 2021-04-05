def lines_from_file(filename):
    """ Returns a list of lines from the given file."""
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


file = "".join(lines_from_file('09.txt'))
#file = "(3x3)XYZ"


def main(file):
    out = ""
    i = 0
    while i < len(file):
        c = file[i]
        if c == '(':
            marker = ""
            i += 1
            while file[i] != ')':
                marker += file[i]
                i += 1
            i += 1
            chars, reps = marker.split('x')
            out += file[i:i + int(chars)] * int(reps)
            i += int(chars)
        else:
            out += c
            i += 1
    return out


while '(' in file:
    file = main(file)
    print(len(file), '(', file.count('('), ')')
# print(out)
print(len(out))
