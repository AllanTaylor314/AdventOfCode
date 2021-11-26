### INPUT ###
players = 400
final = 71864
#############

class CdllNode:
    """Circular doubly linked list Node"""
    def __init__(self, value):
        self.value=value
        self.next=self
        self.prev=self
    def pop(self):
        """Remove from list and return the value"""
        self.next.prev=self.prev
        self.prev.next=self.next
        return self.value
    def insert(self, value):
        """Insert right of the current node"""
        new = CdllNode(value)
        new.next=self.next
        new.prev=self
        new.next.prev=new
        new.prev.next=new
    def __iadd__(self, steps):
        """Step forward through the list"""
        for _ in range(steps):
            self=self.next
        return self
    def __isub__(self, steps):
        """Step backwards through the list"""
        for _ in range(steps):
            self=self.prev
        return self
    def __repr__(self):
        return f"{self.prev.value} <= {self.value} => {self.next.value}"

################## PART 1 ##################
marble_list = CdllNode(0)
p=-1  # Player - 0 to players-1
scoreboard=[0]*players
for marble_score in range(1,final+1):
    p+=1
    p%=players
    if marble_score%23==0:
        scoreboard[p]+=marble_score
        marble_list-=7
        scoreboard[p]+=marble_list.pop()
    else:
        marble_list+=1
        marble_list.insert(marble_score)
    marble_list+=1

print('Part 1:',max(scoreboard), flush=True)

################## PART 2 ##################
marble_list2 = CdllNode(0)
p2=-1  # Player - 0 to players-1
scoreboard2=[0]*players
for marble_score2 in range(1,final*100+1):
    p2+=1
    p2%=players
    if marble_score2%23==0:
        scoreboard2[p2]+=marble_score2
        marble_list2-=7
        scoreboard2[p2]+=marble_list2.pop()
    else:
        marble_list2+=1
        marble_list2.insert(marble_score2)
    marble_list2+=1

print('Part 2:',max(scoreboard2))
