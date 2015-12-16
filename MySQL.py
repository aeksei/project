#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import MySQLdb
sys.path.append('/home/Py/encript')
from stribog import GOST
from ECPoint import ECPoint


class DB():
	def __init__(self, host, user, db, passwd):
		self.__host    = host
		self.__user    = user
		self.__passwd  = passwd
		self.__db      = db

	def execute(self, sql):
		try:
			conn = MySQLdb.connect( host    = self.__host, 
									user    = self.__user, 
									passwd  = self.__passwd, 
									db      = self.__db,
									charset = 'utf8')
			cursor = conn.cursor()
			cursor.execute(sql)
			res = cursor.fetchone()
			conn.commit()
			
		except MySQLdb.Error, e:
			print "Error %d: %s" % (e.args[0],e.args[1])
			sys.exit(1)

		finally:
			if conn:
				conn.close()
			return res

if __name__ == '__main__':
	a  = -3
	b  = 0x64210519e59c80e70fa7e9ab72243049feb8deecc146b9b1
	x  = 0x03188da80eb03090f67cbf20eb43a18800f4ff0afd82ff1012
	y  = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
	fieldchar  = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
	d = DB('localhost','root','messenger','root')
	sql = """INSERT INTO ECPoint(login, x, y, a, b, fieldchar)
    VALUES ('%(l)s', '%(x)s', '%(y)s', '%(a)s', '%(b)s', '%(f)s')
    """%{"l":'test2',"x":hex(x), "y":hex(y), "a":hex(a), "b":hex(b), "f":hex(fieldchar)}
	#a = d.execute("INSERT INTO Users(login, passwd) VALUES ('test2', 'fdsfvsd')")
	#a = d.execute(sql)
	a = d.execute("SELECT * FROM ECPoint")
	print a
