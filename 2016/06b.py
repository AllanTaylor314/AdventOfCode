def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


lines = lines_from_file('06.txt')
message_length = len(lines[0])
letter_freqs = [{} for i in range(message_length)]
for line in lines:
    for i in range(message_length):
        letter_freqs[i][line[i]] = letter_freqs[i].get(line[i], 0) + 1
print(letter_freqs)
for dictionary in letter_freqs:
    search = min(dictionary.values())
    for key, val in dictionary.items():
        if val == search:
            print(key, end="")
            break
