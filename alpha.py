import math

import random



MIN,MAX = -1000,1000

	

def minimax(currdepth,nodeIndex,maxTurn,score,alpha,beta):

	if currdepth == math.ceil(math.log(len(score),2)):

		return score[nodeIndex]

	

	if maxTurn:

		best = MIN

		

		for i in range(0, math.ceil(math.log(len(score),2)-1)):

			val = minimax(currdepth+1,nodeIndex*2+i,False,score,alpha,beta)

			best = max(best, val)

			alpha = max(alpha, best)

			

			if beta<=alpha:

				break

		return best

	else:

		best = MAX

		

		for i in range(0, math.ceil(math.log(len(score),2)-1)):

			val = minimax(currdepth+1,nodeIndex*2+i,True,score,alpha,beta)

			best = min(best,val)

			beta = min(beta,best)

			

			if alpha>=beta:

				break

		return best



score = random.sample(range(1,50),8)

print(str(score))

print("Optimal value =",minimax(0,0,True,score,MIN,MAX))
