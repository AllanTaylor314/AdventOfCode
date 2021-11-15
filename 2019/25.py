from Intcode import Intcode,load_intcode
from itertools import combinations

VERBOSE=True

CODE=load_intcode("25.txt")
LF='\n'

class Ascii(Intcode):
    def __init__(self, stdin=''):
        super().__init__(CODE)
        del self._out_q
        del self._in_q
        self.out=""
        self.stdin=list(stdin)
        self._print_input=bool(stdin)
    def _4(s):
        try:
            s.out+=chr(s._code[s.par(1)])
        except ValueError:
            print('Non ASCII Value:',s._code[s.par(1)])
        if s.out[-1:] in "\n?":
            if VERBOSE: print(s.out,end="",flush=True)
            s.out=''
        s._i+=2
    def _3(s):
        try:
            i=s.stdin.pop(0)
            s._code[s.par(1)]=ord(i)
            if s._print_input: print(i,end="")
            s._i+=2
        except IndexError:
            s.stdin.extend(input()+LF)
            s._print_input=False
            s._3()

get_all_items_and_go_to_checkpoint="""south
take festive hat
north
west
north
south
south
take pointer
east
west
south
take prime number
east
west
west
take coin
east
north
north
east
east
south
south
south
take astrolabe
north
take space heater
north
north
north
take wreath
north
west
take dehydrated water
south
north
north
east
inv
"""

items = ['wreath','space heater','coin','pointer','dehydrated water','festive hat','astrolabe','prime number']
brute_force=LF.join((f"drop {item}" for item in items))+LF  # Drop all
for r in range(1,len(items)):
    for combo in combinations(items,r):
        pre=""
        post=""
        for item in combo:
            pre+=f"take {item}\n"
            post+=f"drop {item}\n"
        brute_force+=pre+'inv\nsouth\n'+post

solution="""drop coin
drop astrolabe
drop festive hat
drop prime number
south
"""

short_solution="""west
south
take pointer
north
east
east
south
south
take space heater
north
north
north
take wreath
north
west
take dehydrated water
north
east
south
"""

# Items in your inventory:
# - wreath
# - space heater
# - pointer
# - dehydrated water

#droid = Ascii(get_all_items_and_go_to_checkpoint+solution)
droid = Ascii(short_solution)
droid.run()

"""
+--------+--------+--------+--------+--------+
|        |        |        |        |        |
|        |        |        |        |        |
|        |        |        |        |        |
|        |        |        |        |        |
+--------+--------+--------+--------+--------+
|        |        |         Security|        |
|        |        |  Warp  |---__---|        |
|        |        |  Drive |        |        |
|        |        |        |        |        |
+--------+--------+---  ---+--------+--------+
|        |        |        |        |        |
|        |        | Hallway Observ- |        |
|        |        |           atory |        |
|        |        |        |        |        |
+--------+--------+---  ---+---  ---+--------+
|        |        |        |        |        |
|        | Stable |Corridor|  Gift  |        |
|        |        |        |  Wrap  |        |
|        |     inf|        |  wreath|        |
+--------+---  ---+--------+---  ---+--------+
|        |        |        |        |        |
|        | Arcade    Hull    Kitchen|        |
|        |          Breach          |        |
|        |        |        |        |        |
+--------+---  ---+---  ---+---  ---+--------+
|        |        |passages|        |        |
|        | Storage|--------|  Sick  |        |
|        |            Nav  |  Bay   |        |
|        |     ptr|        |        |        |
+--------+---  ---+--------+---  ---+--------+
|        |        |        |        |        |
| SciLab    Hot      ENGR  |  Crew  |        |
|           Choc           | Quarts |        |
|    coin|   prime|        |    heat|        |
+--------+--------+--------+---  ---+--------+
|        |        |        |        |        |
|        |        |        |Holodeck|        |
|        |        |        |        |        |
|        |        |        |      al|        |
+--------+--------+--------+--------+--------+
"""