import numpy as np

import math



th = 1

Epochs = 3





class Perceptron:



	def __init__(self,no_of_inputs,alpha=0.2):

		self.alpha = alpha

		self.weights = np.zeros(no_of_inputs+1)

	

	def net_input(self,inputs):

		

		yin = np.dot(inputs,self.weights[1:])+self.weights[0]

		return yin

	

	def train(self,training_inputs,t,weights):

		

		for inputs,target in zip(training_inputs,t):

			yin = self.net_input(inputs)

			

			if yin > th:

				Y = 1

			elif yin > -th:

				Y = 0

			else:

				Y = -1

			

			if target!=Y:

				self.weights[1:]+=self.alpha*target*inputs

				self.weights[0]+=self.alpha*target

			

			print(inputs," ",target,"\t%.2f"%yin,"\t",Y,"\t",self.weights)

	

training_inputs = []

training_inputs.append(np.array([1,1]))

training_inputs.append(np.array([1,-1]))

training_inputs.append(np.array([-1,1]))

training_inputs.append(np.array([-1,-1]))



t = np.array([1,-1,-1,-1])



percep = Perceptron(2)



for i in range(Epochs):



	print("Epochs :",i)

	weights = percep.weights

	print("Initial weights :",weights)

	print("x1 x2 t\t Yin \t Yout    B w1 w2")

	percep.train(training_inputs,t,weights)
