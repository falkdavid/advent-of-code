from aocd.models import Puzzle
D=Puzzle(2020,5).input_data.split('\n')
A=sorted([int(s.translate({70:'0',76:'0',66:'1',82:'1'}),2)for s in D])
print(max(A))
print(sum(range(A[0],A[-1]+1))-sum(A))