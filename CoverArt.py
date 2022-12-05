ESC = "\033"
K,R,G,O,B,P,C,LGR = (f"{ESC}[0;{i}m" for i in range(30,38))
_,LR,LG,Y,LB,LP,LC,W = (f"{ESC}[1;{i}m" for i in range(30,38))
BY = f"{ESC}[1;93m"
BRN = f"{ESC}[0;43m"
RED = f"{ESC}[1;91m"
E = END = f"{ESC}[0;0m"
header_text = """
    A      DDDD    V       V   EEEEE   N   N  TTTTT       OOO    FFFFF       CCC     OOO    DDDD    EEEEE
   A A     D   D    V     V    E       NN  N    T        O   O   F          C   C   O   O   D   D   E    
  AAAAA    D   D     V   V     EEEE    N N N    T        O   O   FFF        C       O   O   D   D   EEE  
 A     A   D   D      V V      E       N  NN    T        O   O   F          C   C   O   O   D   D   E          
A       A  DDDD        V       EEEEE   N   N    T         OOO    F           CCC     OOO    DDDD    EEEEE
"""

# Each line will be handled separately
# Each line must be the same length and each image the same height
images = {
    2015:f"""
    {BY}*{E}    
   {G}>{LG}2{G}<{E}   
  {G}>{B}O{LG}0{G}<<{E}  
 {G}>>{R}@{LG}1{B}o{G}<<{E} 
{G}>{Y}o{G}>>{LG}5{Y}*{G}<<<{E}
    {BRN}H{E}    
""",2016:f"""
   +----+ 
  /    /| 
 +----+ | 
 |{LG}2016{E}| //
 |::{LG}::{E}|// 
======//==
""",2017:f"""
┌┴┴┴┴┴┴┐
┤ {LG}2{E}    ├
┤  {LG}0{E}   ├
┤   {LG}1{E}  ├
┤    {LG}7{E} ├
└┬┬┬┬┬┬┘
""",2018:f"""
     {BY}*{E}     
    {RED}/{LG}2{RED}\{E}    
   {RED}/ {LG}0 {RED}\{E}   
  {RED}/  {LG}1  {RED}\{E}  
 {RED}/{W}___{LG}8{W}___{RED}\{E} 
(~~~~~~~~~)
""",2019:f"""
   ''..  
'''..  ' 
{LG}2019{E}'   '
''.     :
{BY}*{E}  :   . 
..'  .'  
""",2020:fr"""
{G}.''{W}\{G}'..{E} 
{G}.'{W}^ []{G}.'{E}
{G}:{W}^{G} , :{W}\{E} 
 {G}'..'  {W}\{E}
 {P}_{LG}202{P}0>{E} 
{P}/ \ /{P}   
""",2021:f"""
{C}~~~~~~~~~{E}
 {C}.{LG}2{C} ~  {O}.'{E}
  {B}.{LG}0{B} '{O}.:{E} 
 {B}. `{LG}2{O}. '.{E}
{O}:{B} .'{O}.{LG}1{O}:{E}  
 {O}:.:{E}     
""",2022:f"""






"""
}
LPAD = 12
ISPACE = 3
rows = [" "*LPAD]*7
for year,image in images.items():
    for i,row in enumerate(image.splitlines()[1:]):
        rows[i]+=row+" "*ISPACE

print(G+header_text+E)
for row in rows: print(row)
