import math
import random

def minmax(currdepth,nodeIndex,maxTurn,score,tardepth):
	if currdepth==tardepth:
		return score[nodeIndex]
		
	if maxTurn:
		return max(minmax(currdepth+1,nodeIndex*2,False,score,tardepth),
				   minmax(currdepth+1,nodeIndex*2+1,False,score,tardepth)
	else:
		
		return min(minmax(currdepth+1,nodeIndex*2,True,score,tardepth),
				   minmax(currdepth+1,nodeIndex*2+1,True,score,tardepth)

score = random.sample(range(1,50),4)
print(str(score))
treedepth = math.log(len(score),2)
print("The Optimal value = ",minmax(0,0,True,score,treedepth)
