def lines_from_file(filename):
    """ Returns a list of lines from the given file.
    """
    with open(filename, encoding='utf-8') as file:
        raw_data = file.read()
        lines = raw_data.splitlines()
    return lines


def supports_tls(ip):
    subnets = ip.replace("]", "[").split("[")
    support = False
    for i in range(len(subnets)):
        if is_abba(subnets[i]):
            if i % 2:
                return False
            else:
                support = True
    return support


def supports_ssl(ip):
    subnets = ip.replace("]", "[").split("[")
    supernets = subnets[0::2]
    hypernets = subnets[1::2]
    babs = []
    abas = []
    for net in supernets:
        for bab in gen_bab(net):
            babs.append(bab)
    for net in hypernets:
        for aba in gen_aba(net):
            abas.append(aba)
    overlap = set(babs) & set(abas)
    # print(overlap)
    return len(overlap) > 0
    # print(ip,supernets,hypernets)


def is_aba(s):
    """Takes string of any length. Returns true if string contains sequence
    in the form aba where a and b are any different letters
    """
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2] and\
           s[i] != s[i + 1]:
            return True
    return False


def gen_bab(s):
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2] and\
           s[i] != s[i + 1]:
            yield s[i:i + 3]


def gen_aba(s):
    for i in range(0, len(s) - 2):
        if s[i] == s[i + 2] and\
           s[i] != s[i + 1]:
            yield s[i + 1] + s[i] + s[i + 1]


def is_abba(s):
    """Takes string of any length. Returns true if string contains sequence
    in the form abba where a and b are any different letters
    """
    for i in range(0, len(s) - 3):
        if s[i] == s[i + 3] and\
           s[i + 1] == s[i + 2] and\
           not s[i] == s[i + 1]:
            return True
    return False


lines = lines_from_file('07.txt')
count = 0
for ip in lines:
    count += int(supports_ssl(ip))
print(count)
