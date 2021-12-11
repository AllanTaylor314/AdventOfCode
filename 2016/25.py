class Assembunny:
    def __init__(self,code,a=0):
        self.reg={'a':a,'b':0,'c':0,'d':0}
        self.code=code.copy()
        self.i=0
    def val(self,x):
        if x in self.reg: return self.reg[x]
        return int(x)
    def cpy(self,x,y):
        self.reg[y]=self.val(x)
        self.i+=1
    def inc(self,x):
        self.reg[x]+=1
        self.i+=1
    def dec(self,x):
        self.reg[x]-=1
        self.i+=1
    def jnz(self,x,y):
        self.i+=self.val(y) if self.val(x) else 1
    def run(self):
        while self.i<len(self.code):
            ins,*pars=self.code[self.i]
            getattr(self,ins)(*pars)

class TransmitterAssembunny(Assembunny):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.a = self.reg['a']
        self.output=[]
        self.recent_out=1
    def out(self,x):
        val=self.val(x)
        self.output.append(val)
        if self.recent_out==val: raise ValueError(f"{self.a} is not the right a")
        if len(self.output)>100: raise RecursionError(f"{self.a} is lasting a while")
        self.recent_out=val
        self.i+=1

with open('25.txt') as file:
    data=file.read()

instructions = list(map(str.split,data.splitlines()))
n=0
while True:
    computer=TransmitterAssembunny(instructions,n)
    try:
        computer.run()
    except ValueError:
        print(f"{computer.a:3d}: {''.join(map(str,computer.output))}")
    except RecursionError:
        print("Part 1:",computer.a)
        break
    n+=1
