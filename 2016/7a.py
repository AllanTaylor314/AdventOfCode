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


lines = lines_from_file('7.txt')
count = 0
for ip in lines:
    count += int(supports_tls(ip))
print(count)
