PLACES = {"2":2,"1":1,"0":0,"-":-1,"=":-2}
def snafu_to_decimal(snafu):
    if snafu:
        return 5*snafu_to_decimal(snafu[:-1])+PLACES[snafu[-1]]
    return 0
def decimal_to_snafu(decimal,_root_call=True):
    if decimal:
        a,b=divmod(decimal+2,5)
        return decimal_to_snafu(a,False)+"=-012"[b]
    return "0" if _root_call else ""
with open("25.txt") as file:
    lines = file.read().splitlines()
p1 = sum(map(snafu_to_decimal,lines))
print("Part 1:",decimal_to_snafu(p1))
