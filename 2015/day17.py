from itertools import combinations

instr = '50 44 11 49 42 46 18 32 26 40 21 7 18 43 10 47 36 24 22 40'
cont = [ int(s) for s in instr.split() ]
c = 0
for i in range(len(cont)):
  c += len( [ x for x in combinations(cont, i+1) if sum(x) == 150] )
print(c, 'combinations')

for i in range(len(cont)):
  c = [ x for x in combinations(cont, i+1) if sum(x) == 150] 
  if len(c) > 0:
    print('Min container combinations:', len(c))
    break
