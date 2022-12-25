PLACES = {"2":2,"1":1,"0":0,"-":-1,"=":-2}
def snafu_to_decimal(snafu):
    if snafu:
        return 5*snafu_to_decimal(snafu[:-1])+PLACES[snafu[-1]]
    return 0
def decimal_to_snafu(decimal):
    if decimal>0:
        a,b=divmod(decimal+2,5)
        return decimal_to_snafu(a)+"=-012"[b]
    return ""
# print(*map(snafu_to_decimal,"""1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122""".splitlines()),sep="\n")
with open("25.txt") as file:
    lines = file.read().splitlines()

p1 = sum(map(snafu_to_decimal,lines))

print("Part 1:",decimal_to_snafu(p1))
p2 = 0

print("Part 2:",p2)
