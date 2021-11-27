class Conway:
    def __init__(self, board):
        self._board = [list(line) for line in board.splitlines()]
    def __repr__(self):
        return '\n'.join(''.join(line) for line in self._board)
    def _neighbours(self,x,y):
        self._board[y][x]  # Just check
        out=''
        for dy in [-1,0,1]:
            for dx in [-1,0,1]:
                if dx==0==dy: continue
                if 0<=y+dy<len(self._board) and 0<=x+dx<len(self._board[y]):
                    out+=self._board[y+dy][x+dx]
        return out
    def step(self):
        new_board=[]
        for y in range(len(self._board)):
            new_board.append([])
            for x in range(len(self._board[y])):
                new_board[-1].append(
                    self._outcome(
                        self._board[y][x],
                        self._neighbours(x,y)
                    )
                )
        self._board=new_board
    def _outcome(self, current, neighbours):
        num_trees = neighbours.count('|')
        num_lumber = neighbours.count('#')
        if current=='.':
            if num_trees>=3:
                return '|'
            return current
        if current=='|':
            if num_lumber>=3:
                return '#'
            return current
        if current=='#':
            if num_lumber>=1 and num_trees>=1:
                return '#'
            return '.'
    def value(self):
        s = repr(self)
        return s.count('|')*s.count('#')

with open('18.txt') as file:
    data = file.read()

forest = Conway(data)
for i in range(10):
    forest.step()
    print(f"After {i+1} minutes:\n{forest}",flush=True)
pt1 = forest.value()
print('Part 1:', pt1,flush=True)
# Part 1: 605154

states = {}
history = {}
BILLION=1_000_000_000
for i in range(10,BILLION):
    if i%100==0:
        print(f"t={i}, value is {forest.value()}")
    forest.step()
    if (r:=repr(forest)) not in states:
        states[r]=i
        history[i]=r
    else:
        print(f"State at {i} is state at {states[r]}")
        history[i]=r
        break
else:
    print('No break value:',forest.value())
for _ in range((BILLION-i)%(i-states[r])-1):
    print(forest.value())
    forest.step()
print('Part 2:',forest.value())

# Part 2: 200364