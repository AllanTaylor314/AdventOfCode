a2z = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()


def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def gen_checksum(room):
    cs = ""
    d = {}
    for c in room:
        d[c] = d.get(c, 0) + 1
    e = {}
    for key, val in d.items():
        if val in e:
            e[val].append(key)
        else:
            e[val] = [key]
    out = ""
    for i in range(max(e.keys()), 0, -1):
        if i in e:
            e[i].sort()
            out += "".join(e[i])
        if len(out) > 5:
            break
    # print(e)
    return out[0:5]


def decrypt(room, sector):
    shift = sector
    cypher = {"-": " "}
    for i in range(0, 26):
        cypher[a2z[i]] = a2z[(i + shift) % 26]
    out = ""
    for c in room:
        out += cypher[c]
    return out


lines = lines_from_file('4.txt')
data = []
for line in lines:
    a = line.split("-")
    sector, checksum = a.pop(-1).split("[")
    sector = int(sector)
    checksum = checksum[:-1]
    room = "-".join(a)
    data.append((room, sector, checksum))

sector_sum = 0
for room, sector, checksum in data:
    if checksum == gen_checksum(room) or True:
        name = decrypt(room, sector)
        if name == "northpole object storage":
            answer = sector
        print(name, sector)
print("The answer is", answer)
# print(sector_sum)
