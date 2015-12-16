#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('/home/Py/encript')
from ECPoint import ECPoint
from stribog import GOST
from primeNum import primeNum

class DSGost():
	__G  = None
	
	def __init__(self, p, a, b, n, xG, versionHash=256):
		self.__a  = a
		self.__b  = b
		self.__n  = n
		self.__p  = p
		self.__xG = xG
		self.__lenght  = versionHash/4

	def GenPrivateKey(self):
		while True:
			d = int(os.urandom(self.__lenght/2).encode('hex'), 16)
			if (d > 0) and (d > self.__n):
				break			
		return d

	def GenPublicKey(self, d, Q=None):
		G = self.GDecompress()
		if Q is None:
			Q = G.multiply(d)
		return Q

	def GDecompress(self):
		y = int(self.__xG[:2], 16)
		xCord = int(self.__xG[2:], 16)
		tmp = (pow(xCord, 3) + self.__a * xCord + self.__b) % self.__p
		beta = self.ModSqrt(tmp, self.__p)
		if (beta % 2) == (y % 2):
			yCord = beta
		else:
			yCord = self.__p - beta

		G = ECPoint(xCord, yCord, self.__a, self.__b, self.__p)
		self.__G = G
		return G

	def ModSqrt(self, a, q):
		r = None
		while True:
			b = int(os.urandom(self.__lenght/2).encode('hex'), 16)
			b = b >> 1
			if self.Legendre(b, q) != 1: break
		s = 0
		t = q - 1
		while (t & 1) != 1:
			s += 1
			t = t >> 1
		invA = pow(a, q-2, q)
		if invA == 0: print 'ERROR'
		c = pow(b, t, q)
		r = pow(a, ((t+1)/2), q)
		for i in xrange(1,s):
			tmp = 2
			tmp = pow(tmp, (s-i-1), q)
			if d == (q-1):
				r = (r * c) % q
			c = pow(c, 2, q)
		return r

	def Legendre(self, a, q):
		return pow(a, ((q-1)/2),q)

	def SingGen(self, h, d):
		pre = GOST().prepareHex
		e = h % self.__n 
		if (e == 0): e = 1
		while True:
			while True:
				k = int(os.urandom(self.__lenght).encode('hex'), 16)
				if (d > 0) and (d > self.__n):
					break
			C = self.__G.multiply(k)
			r = C.x % self.__n
			s = long(long(r * d) + long(k * e)) % self.__n
			if (r != 0) and (s != 0):
				break
		
		return self.addZero(pre(hex(r))) + self.addZero(pre(hex(s)))
	
	def SingVer(self, H, sing, Q):
		l = self.__lenght
		r = int(sing[:l], 16)
		s = int(sing[l:], 16)
		if (r < 1) or (r > (n-1)) or (s < 1) or (s > (n-1)):
			return False
		e = H % self.__n 
		if (e == 0): e = 1
		self.__n = n
		v = pow(e, n-2, n)
		z1 = (s * v) % n
		z2 = n + ((-(r * v)) % n)
		self.__G = self.GDecompress()
		A = self.__G.multiply(z1)
		B = Q.multiply(z2)
		C = A + B
		R = C.x % n

		if R == r:
			return True
		else:
			return False


	def addZero(self, s):
		l = self.__lenght
		return '0'*(l - len(s)) + s



if __name__ == '__main__':	
	p  = 6277101735386680763835789423207666416083908700390324961279
	a  = -3
	b  = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
	xG = '03188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012'
	n  = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
	#n  = primeNum().get() 
	DS = DSGost(p, a, b, n, xG)
	DS1 = DSGost(p, a, b, n, xG)
	#d  = DS.GenPrivateKey()
	d = 455936492118208185633529824744099308609971985548110823845416075281514783794554940847204837985404159395183992688471117829511560920881728804447455326114292L
	b  = ECPoint(1791047505851178572875763820410146702188686496182717679368L, 3671238363959597127547523270057700245059762540500241556950L, -3, 2455155546008943817740293915197451784769108058161191238065L, 6277101735386680763835789423207666416083908700390324961279L)
	Q = DS.GenPublicKey(d,b)
	print Q.getAttr()
	g  = GOST(512)
	msg = 'jkjkjkgergergergrodhfevihbdfiovbdifvbidfvbikdbokivjhdddddddnffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
	H  = g.hash(msg.encode('hex'))

	sign = DS.SingGen(H, d)
	print DS1.SingVer(H, sign, Q)
	
	


		