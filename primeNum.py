#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as r
import math as m
import os
class primeNum:
	P = [  2,  3,  5,  7, 11, 13, 17, 19, 23, 29,
	      31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
	      73, 79, 83, 89, 97,101,103,107,109,113,
	     127,131,137,139,149,151,157,163,167,173,
	     179,181,191,193,197,199,211,223,227,229,
	     233,239,241,251,257,263,269,271,277,281]

	def __init__(self, n=256, rounds=100):
		self.__n      = n/4
		self.__rounds = rounds

	def __str__(self):
		return str(self.__p)+ '\n'

	def calculate(self):
		p = int(os.urandom(self.__n).encode('hex'), 16)
		while (True):
			prime = False
			while True:
				if ((p % 6 == 1) or (p % 6 == 5)):
					for d in self.P:
						if (p % d == 0):
							p += 1
							prime = False
						else:
							prime = True					
					if prime == True: 
						break				
				else: 
					p += 1
			if (self.test_MR(p,self.__rounds)):
				self.__p = p
				break
			else:
				p+=1

	def test_MR(self,p,rounds):
		prime = True
		t = p-1
		s = 0
		while True:
			if(t%2 == 0):
				t = t/2
				s += 1
			else:
				break
		#r = int(m.log(m,2))
		while rounds != 0:
			rounds -= 1
			a = r.randint(2, p-2)
			x = pow(a,t,p)
			if (x == 1 or x == p-1):
				continue			
			for i in range(1, s-1):
				x = pow(x,2,p)
				if x == 1:
					return False
				if x == p-1:
					break
			if x == p-1:
				continue
			return False

		return True

	def get(self):
		self.calculate()
		return self.__p

if __name__ == '__main__':
	num1 = primeNum(256).get()
	print num1

