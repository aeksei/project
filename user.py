#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
sys.path.append('/home/Py/encript')
from ECPoint import ECPoint
from DSGost import DSGost
from stribog import GOST
from MySQL import DB


class User():
	RSALenghtKey = 2048

	def __init__(self, login, port):
		self.login    = login
		self.port     = port
		sql = """SELECT passwd from Users
		WHERE login='%(l)s'
		"""%{"l":self.login}

		d = DB('localhost','root','messenger','root')
		q = d.execute(sql)
		print q

   		if q is None:
   			self.password = q
   		else:
   			self.password = q[0]
   			self.__pswd   = hex(GOST(256).hash(self.password.encode('hex')))[:32]

   		self.signature()

	def signature(self):
		p  = 6277101735386680763835789423207666416083908700390324961279
		a  = -3
		b  = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
		xG = '03188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012'
		n  = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
		#n  = primeNum().get() 
		self.DS = DSGost(p, a, b, n, xG)

		self.b  = ECPoint(1791047505851178572875763820410146702188686496182717679368L, 3671238363959597127547523270057700245059762540500241556950L, -3, 2455155546008943817740293915197451784769108058161191238065L, 6277101735386680763835789423207666416083908700390324961279L)

	def start(self):
		self.setPort(self.port)
   		self.decriptRSAKey()
   		self.decriptDSKey()


	def reg(self, p):
		self.password = hex(GOST(256).hash(p.encode('hex') + self.login.encode('hex')))
		self.__pswd   = hex(GOST(256).hash(self.password.encode('hex')))[:32]
		sql = """INSERT INTO Users(login, passwd)
		VALUES ('%(l)s', '%(p)s')
		"""%{"l":self.login, "p": self.password}
		d = DB('localhost','root','messenger','root')		
   		d.execute(sql)

   		self.genRSAKey()
   		self.genDSKey()

   		return self.password


	def genRSAKey(self):
		key  = RSA.generate(self.RSALenghtKey)
		pub  = key.publickey().exportKey()
		priv = key.exportKey()
		AES.block_size = 32
		iv   = os.urandom(8).encode('hex')
		# Encryption
		cipher = AES.new(self.__pswd, AES.MODE_CFB, iv)
		priv   = cipher.encrypt(priv)

		sql = """INSERT INTO RSA(login, pub, priv, iv)
  		VALUES ('%(l)s', '%(pub)s', '%(priv)s', '%(iv)s')
   		"""%{"l":self.login,"pub":pub.encode('hex'), "priv":priv.encode('hex'), "iv":iv.encode('hex')}

   		d = DB('localhost','root','messenger','root')
   		d.execute(sql)

	def updateRSAKey(self):
		key  = RSA.generate(self.RSALenghtKey)
		pub  = key.publickey().exportKey()
		priv = key.exportKey()
		AES.block_size = 32
		iv   = os.urandom(8).encode('hex')
		# Encryption
		cipher = AES.new(self.__pswd, AES.MODE_CFB, iv)
		priv   = cipher.encrypt(priv)

		sql = """UPDATE RSA
   		SET pub='%(pub)s', priv='%(priv)s', iv='%(iv)s'
  		WHERE login = '%(l)s'
   		"""%{"l":self.login,"pub":pub.encode('hex'), "priv":priv.encode('hex'), "iv":iv.encode('hex')}

   		d = DB('localhost','root','messenger','root')
   		d.execute(sql)

	def genDSKey(self):
		priv = self.DS.GenPrivateKey()
		pub  = self.DS.GenPublicKey(priv)
		pub  = pub.getAttr()
		
		AES.block_size = 32
		iv   = os.urandom(8).encode('hex')
		# Encryption
		cipher = AES.new(self.__pswd, AES.MODE_CFB, iv)
		priv   = cipher.encrypt(hex(priv))

		sql = """INSERT INTO DS(login, x, y, a, b, fieldchar, priv, iv)
  		VALUES ('%(l)s', '%(x)s', '%(y)s', '%(a)s', '%(b)s', '%(f)s', '%(priv)s', '%(iv)s')
   		"""%{"l":self.login,"x":hex(pub[0]), "y":hex(pub[1]), "a":hex(pub[2]), "b":hex(pub[3]), "f":hex(pub[4]), "priv":priv.encode('hex'), "iv":iv.encode('hex')}
		
		d = DB('localhost','root','messenger','root')
   		d.execute(sql)

   	def updateDSKey(self):
		priv = self.DS.GenPrivateKey()
		pub  = self.DS.GenPublicKey(priv)
		pub  = pub.getAttr()
		
		AES.block_size = 32
		iv   = os.urandom(8).encode('hex')
		# Encryption
		cipher = AES.new(self.__pswd, AES.MODE_CFB, iv)
		priv   = cipher.encrypt(hex(priv))

   		sql = """UPDATE DS
   		SET x='%(x)s', y ='%(y)s', priv='%(priv)s', iv='%(iv)s'
  		WHERE login = '%(l)s'
   		"""%{"x":hex(pub[0]), "y":hex(pub[1]), "priv":priv.encode('hex'), "iv":iv.encode('hex')}

   		d = DB('localhost','root','messenger','root')
   		d.execute(sql)

   	def checkSign(self, login):


		sql = """SELECT x, y from DS
		WHERE login='%(l)s'
		"""%{"l":login}

		d = DB('localhost','root','messenger','root')
   		E = d.execute(sql)

   		E = map(lambda h: int(h[2:-1], 16), E)
   		Q = ECPoint(E[0], E[1], a, b, p)



   		DS.SingVer(H, sign, Q)
   		print Q.getAttr()
   		#print map(lambda b: int(b, 16), E)

	def decriptDSKey(self):
		sql = """SELECT priv, iv from DS
		WHERE login='%(l)s'
		"""%{"l":self.login}

		d       = DB('localhost','root','messenger','root')
		key, iv = d.execute(sql)
		
		key    = key.decode('hex')
		iv     = iv.decode('hex')
		cipher = AES.new(self.__pswd, AES.MODE_CFB, iv)
		key    = cipher.decrypt(key)
		self.__PrivDSKey = key


	def decriptRSAKey(self):
		sql = """SELECT priv, iv from RSA
		WHERE login='%(l)s'
		"""%{"l":self.login}

		d       = DB('localhost','root','messenger','root')
		key, iv = d.execute(sql)
		
		key    = key.decode('hex')
		iv     = iv.decode('hex')
		cipher = AES.new(self.__pswd, AES.MODE_CFB, iv)
		key    = cipher.decrypt(key)
		self.__PrivRSAKey = RSA.importKey(key)

	def encryptMsg(self, login, msg):
		sql = """SELECT pub from RSA
		WHERE login='%(l)s'
		"""%{"l":login}

		d   = DB('localhost','root','messenger','root')
		key = d.execute(sql)[0]
		key = key.decode('hex')
		PubKey = RSA.importKey(key)		
		iv  = os.urandom(4).encode('hex')
		H  = GOST(256).hash(msg.encode('hex'))
		print self.__PrivDSKey
		self.DS.GenPublicKey(self.__PrivDSKey,self.b)
		sign = self.DS.SingGen(32, self.__PrivDSKey)

		pack = "#---#".join(msg, sign)
		print pack

		cipher_text = ''.join(PubKey.encrypt(pack, iv)).encode('hex')

		print 'messenge encrypt'

		return 

	def decryptMsg(self, msg):
		cipher_text = str(msg).decode('hex')
		msg = self.__PrivRSAKey.decrypt(cipher_text)

		print 'messenge decrypt'

		return msg

	def setPort(self, port):
		sql = """UPDATE Users
   		SET port='%(port)s'
  		WHERE login = '%(l)s'
   		"""%{"l":self.login,"port":port}

   		d = DB('localhost','root','messenger','root')
   		d.execute(sql)



if __name__ == '__main__':
	login = 'user'
	password = 'password'
	password = hex(GOST(256).hash(password.encode('hex') + login.encode('hex')))
	sql = """INSERT INTO Users(login, passwd)
	VALUES ('%(l)s', '%(p)s')
	"""%{"l":login, "p": password}

	d = DB('localhost','root','messenger','root')
   	d.execute(sql)
	#Q = newUser.genRSAKey()
	#newUser.genRSAKey()
	#newUser.decriptDSKey()
	#print Q
	#print Q.decode('hex')
		

