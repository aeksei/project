#!/usr/bin/env python
# -*- coding: utf-8 -*-

class ECPoint():
	x         = None
	y         = None
	a         = None
	b         = None
	FieldChar = None

	def __init__(self, x, y, a, b, FieldChar):
		self.x         = x
		self.y         = y
		self.a         = a
		self.b         = b
		self.FieldChar = FieldChar

	def getAttr(self):
		return (self.x, self.y, self.a, self.b, self.FieldChar)

	def __add__(self, other):
		p3 = ECPoint(None, None, self.a, self.b, self.FieldChar)

		dy = other.y - self.y
		dx = other.x - self.x

		if dx < 0: dx += self.FieldChar
		if dy < 0: dy += self.FieldChar

		m = (dy*pow(dx,self.FieldChar-2,self.FieldChar)) % self.FieldChar
		if m < 0: m += self.FieldChar
		p3.x = (m * m - self.x - other.x)     % self.FieldChar
		p3.y = (m * (self.x - p3.x) - self.y) % self.FieldChar

		if p3.x < 0: p3.x += self.FieldChar
		if p3.y < 0: p3.y += self.FieldChar

		return p3

	def Double(self):
		p2 = ECPoint(None, None, self.a, self.b, self.FieldChar)

		dy = 3 * self.x * self.x + self.a
		dx = 2 * self.y

		if dx < 0: dx += self.FieldChar
		if dy < 0: dy += self.FieldChar

		m = (dy*pow(dx,self.FieldChar-2,self.FieldChar)) % self.FieldChar

		p2.x = (m * m - self.x - self.x)      % self.FieldChar
		p2.y = (m * (self.x - p2.x) - self.y) % self.FieldChar

		if p2.x < 0: p2.x += self.FieldChar
		if p2.y < 0: p2.y += self.FieldChar

		return p2

	def multiply(self, k):
		p = self
		tmp = self
		k -= 1
		while k != 0:
			if (k % 2) != 0:
				if (tmp.x == p.x) or (tmp.y == p.y):
					tmp = tmp.Double()
				else:
					tmp = tmp + p
				k -= 1
			k = k / 2
			p = p.Double()

		return tmp








