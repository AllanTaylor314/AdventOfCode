### PUZZLE INPUT ###
num_recipes = 320851
####################

scores = [3,7]
elf1 = 0
elf2 = 1
def create_new():
    scores.extend(map(int,str(scores[elf1]+scores[elf2])))
def step_elves():
    global elf1,elf2
    elf1+=1+scores[elf1]
    elf1%=len(scores)
    elf2+=1+scores[elf2]
    elf2%=len(scores)

while len(scores)<num_recipes+10:
    create_new()
    step_elves()
print('Part 1:',end=" ")
print(*scores[num_recipes:num_recipes+10],sep='',flush=True)

#################### Part 2 ####################
target_sublist = list(map(int,str(num_recipes)))
i=0
search = True
while search:
    while i+len(target_sublist)<len(scores):
        if scores[i:i+len(target_sublist)]==target_sublist:
            print('Part 2:',i)
            search=False
            break
        i+=1
    create_new()
    step_elves()