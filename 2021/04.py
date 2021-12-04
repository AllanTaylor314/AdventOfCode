class BingoBoard:
    called=[]
    def __init__(self, bingo_str):
        self.board=[list(map(int,_.split())) for _ in bingo_str.splitlines()]
    def __repr__(self):
        return "\n".join(" ".join(map(str,_)) for _ in self.board)
    def bingo(self):
        lines=list(map(set,self.board))+list(map(set,zip(*self.board)))
        b=set(self.called)
        return any(len(a-b)==0 for a in lines)
    def _unmarked(self):
        all_nums = set()
        for line in self.board:
            all_nums|=set(line)
        return all_nums-set(self.called)
    def score(self):
        return sum(self._unmarked())*self.called[-1]

with open('04.txt') as file:
    data = file.read().split('\n\n')

num_str,*board_strs=data

nums=list(map(int,num_str.split(',')))
boards=[BingoBoard(board) for board in board_strs]
part1=True
winners=set()
for n in nums:
    BingoBoard.called.append(n)
    for board in boards:
        if board.bingo():
            if part1:
                print('Part 1:',board.score())
                part1=False
            if board not in winners:
                last = board
                last_score = last.score()
            winners.add(board)
print('Part 2:',last_score)