import re, json
with open('12.txt') as file:
    data = file.read()

print('Part 1:',sum(map(int,re.findall("[\-0-9]+", data))))

jdata = json.loads(data)

def sum_non_red(j):
    """Returns 0 if dict contains red"""
    if isinstance(j,int):
        return j
    if isinstance(j,str):
        return 0
    if isinstance(j,list):
        return sum(map(sum_non_red,j))
    if isinstance(j,dict):
        if 'red' in j.values():
            return 0
        return sum(map(sum_non_red,j.values()))
    else:
        raise TypeError(f"Type {type(j)} unhandled")

print('Part 2:',sum_non_red(jdata))

assert sum_non_red([1,2,3])==6
assert sum_non_red([1,{"c":"red","b":2},3])==4
assert sum_non_red({"d":"red","e":[1,2,3,4],"f":5})==0
assert sum_non_red([1,"red",5])==6

assert sum_non_red(
    {
        "a":"red",
        "b":100
    }
)==0