#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Matrix A for __L function
A=[
	0x8e20faa72ba0b470,
	0x47107ddd9b505a38,
	0xad08b0e0c3282d1c,
	0xd8045870ef14980e,
	0x6c022c38f90a4c07,
	0x3601161cf205268d,
	0x1b8e0b0e798c13c8,
	0x83478b07b2468764,
	0xa011d380818e8f40,
	0x5086e740ce47c920,
	0x2843fd2067adea10,
	0x14aff010bdd87508,
	0x0ad97808d06cb404,
	0x05e23c0468365a02,
	0x8c711e02341b2d01,
	0x46b60f011a83988e,
	0x90dab52a387ae76f,
	0x486dd4151c3dfdb9,
	0x24b86a840e90f0d2,
	0x125c354207487869,
	0x092e94218d243cba,
	0x8a174a9ec8121e5d,
	0x4585254f64090fa0,
	0xaccc9ca9328a8950,
	0x9d4df05d5f661451,
	0xc0a878a0a1330aa6,
	0x60543c50de970553,
	0x302a1e286fc58ca7,
	0x18150f14b9ec46dd,
	0x0c84890ad27623e0,
	0x0642ca05693b9f70,
	0x0321658cba93c138,
	0x86275df09ce8aaa8,
	0x439da0784e745554,
	0xafc0503c273aa42a,
	0xd960281e9d1d5215,
	0xe230140fc0802984,
	0x71180a8960409a42,
	0xb60c05ca30204d21,
	0x5b068c651810a89e,
	0x456c34887a3805b9,
	0xac361a443d1c8cd2,
	0x561b0d22900e4669,
	0x2b838811480723ba,
	0x9bcf4486248d9f5d,
	0xc3e9224312c8c1a0,
	0xeffa11af0964ee50,
	0xf97d86d98a327728,
	0xe4fa2054a80b329c,
	0x727d102a548b194e,
	0x39b008152acb8227,
	0x9258048415eb419d,
	0x492c024284fbaec0,
	0xaa16012142f35760,
	0x550b8e9e21f7a530,
	0xa48b474f9ef5dc18,
	0x70a6a56e2440598e,
	0x3853dc371220a247,
	0x1ca76e95091051ad,
	0x0edd37c48a08a6d8,
	0x07e095624504536c,
	0x8d70c431ac02a736,
	0xc83862965601dd1b,
	0x641c314b2b8ee083
]

# Constant values for KeySchedule function
C = [
	0xb1085bda1ecadae9ebcb2f81c0657c1f2f6a76432e45d016714eb88d7585c4fc4b7ce09192676901a2422a08a460d31505767436cc744d23dd806559f2a64507,
	0x6fa3b58aa99d2f1a4fe39d460f70b5d7f3feea720a232b9861d55e0f16b501319ab5176b12d699585cb561c2db0aa7ca55dda21bd7cbcd56e679047021b19bb7,
	0xf574dcac2bce2fc70a39fc286a3d843506f15e5f529c1f8bf2ea7514b1297b7bd3e20fe490359eb1c1c93a376062db09c2b6f443867adb31991e96f50aba0ab2,
	0xef1fdfb3e81566d2f948e1a05d71e4dd488e857e335c3c7d9d721cad685e353fa9d72c82ed03d675d8b71333935203be3453eaa193e837f1220cbebc84e3d12e,
	0x4bea6bacad4747999a3f410c6ca923637f151c1f1686104a359e35d7800fffbdbfcd1747253af5a3dfff00b723271a167a56a27ea9ea63f5601758fd7c6cfe57,
	0xae4faeae1d3ad3d96fa4c33b7a3039c02d66c4f95142a46c187f9ab49af08ec6cffaa6b71c9ab7b40af21f66c2bec6b6bf71c57236904f35fa68407a46647d6e,
	0xf4c70e16eeaac5ec51ac86febf240954399ec6c7e6bf87c9d3473e33197a93c90992abc52d822c3706476983284a05043517454ca23c4af38886564d3a14d493,
	0x9b1f5b424d93c9a703e7aa020c6e41414eb7f8719c36de1e89b4443b4ddbc49af4892bcb929b069069d18d2bd1a5c42f36acc2355951a8d9a47f0dd4bf02e71e,
	0x378f5a541631229b944c9ad8ec165fde3a7d3a1b258942243cd955b7e00d0984800a440bdbb2ceb17b2b8a9aa6079c540e38dc92cb1f2a607261445183235adb,
	0xabbedea680056f52382ae548b2e4f3f38941e71cff8a78db1fffe18a1b3361039fe76702af69334b7a1e6c303b7652f43698fad1153bb6c374b4c7fb98459ced,
	0x7bcd9ed0efc889fb3002c6cd635afe94d8fa6bbbebab076120018021148466798a1d71efea48b9caefbacd1d7d476e98dea2594ac06fd85d6bcaa4cd81f32d1b,
	0x378ee767f11631bad21380b00449b17acda43c32bcdf1d77f82012d430219f9b5d80ef9d1891cc86e71da4aa88e12852faf417d5d9b21b9948bc924af11bd720
]


# Substitution for __S function 
Sbox=[
	0xFC, 0xEE, 0xDD, 0x11, 0xCF, 0x6E, 0x31, 0x16, 0xFB, 0xC4, 0xFA, 0xDA, 0x23, 0xC5, 0x04, 0x4D,
	0xE9, 0x77, 0xF0, 0xDB, 0x93, 0x2E, 0x99, 0xBA, 0x17, 0x36, 0xF1, 0xBB, 0x14, 0xCD, 0x5F, 0xC1,
	0xF9, 0x18, 0x65, 0x5A, 0xE2, 0x5C, 0xEF, 0x21, 0x81, 0x1C, 0x3C, 0x42, 0x8B, 0x01, 0x8E, 0x4F,
	0x05, 0x84, 0x02, 0xAE, 0xE3, 0x6A, 0x8F, 0xA0, 0x06, 0x0B, 0xED, 0x98, 0x7F, 0xD4, 0xD3, 0x1F,
	0xEB, 0x34, 0x2C, 0x51, 0xEA, 0xC8, 0x48, 0xAB, 0xF2, 0x2A, 0x68, 0xA2, 0xFD, 0x3A, 0xCE, 0xCC,
	0xB5, 0x70, 0x0E, 0x56, 0x08, 0x0C, 0x76, 0x12, 0xBF, 0x72, 0x13, 0x47, 0x9C, 0xB7, 0x5D, 0x87,
	0x15, 0xA1, 0x96, 0x29, 0x10, 0x7B, 0x9A, 0xC7, 0xF3, 0x91, 0x78, 0x6F, 0x9D, 0x9E, 0xB2, 0xB1,
	0x32, 0x75, 0x19, 0x3D, 0xFF, 0x35, 0x8A, 0x7E, 0x6D, 0x54, 0xC6, 0x80, 0xC3, 0xBD, 0x0D, 0x57,
	0xDF, 0xF5, 0x24, 0xA9, 0x3E, 0xA8, 0x43, 0xC9, 0xD7, 0x79, 0xD6, 0xF6, 0x7C, 0x22, 0xB9, 0x03,
	0xE0, 0x0F, 0xEC, 0xDE, 0x7A, 0x94, 0xB0, 0xBC, 0xDC, 0xE8, 0x28, 0x50, 0x4E, 0x33, 0x0A, 0x4A,
	0xA7, 0x97, 0x60, 0x73, 0x1E, 0x00, 0x62, 0x44, 0x1A, 0xB8, 0x38, 0x82, 0x64, 0x9F, 0x26, 0x41,
	0xAD, 0x45, 0x46, 0x92, 0x27, 0x5E, 0x55, 0x2F, 0x8C, 0xA3, 0xA5, 0x7D, 0x69, 0xD5, 0x95, 0x3B,
	0x07, 0x58, 0xB3, 0x40, 0x86, 0xAC, 0x1D, 0xF7, 0x30, 0x37, 0x6B, 0xE4, 0x88, 0xD9, 0xE7, 0x89,
	0xE1, 0x1B, 0x83, 0x49, 0x4C, 0x3F, 0xF8, 0xFE, 0x8D, 0x53, 0xAA, 0x90, 0xCA, 0xD8, 0x85, 0x61,
	0x20, 0x71, 0x67, 0xA4, 0x2D, 0x2B, 0x09, 0x5B, 0xCB, 0x9B, 0x25, 0xD0, 0xBE, 0xE5, 0x6C, 0x52,
	0x59, 0xA6, 0x74, 0xD2, 0xE6, 0xF4, 0xB4, 0xC0, 0xD1, 0x66, 0xAF, 0xC2, 0x39, 0x4B, 0x63, 0xB6
]



# Substitution for __P function
Tau=[
	0,  8, 16, 24, 32, 40, 48, 56,
	1,  9, 17, 25, 33, 41, 49, 57,
	2, 10, 18, 26, 34, 42, 50, 58,
	3, 11, 19, 27, 35, 43, 51, 59,
	4, 12, 20, 28, 36, 44, 52, 60,
	5, 13, 21, 29, 37, 45, 53, 61,
	6, 14, 22, 30, 38, 46, 54, 62,
	7, 15, 23, 31, 39, 47, 55, 63
]

class GOST:
	__h             = None
	__N             = None
	__Sigma         = None
	__message       = None
	__lengthMessage = None
	__version       = None
	def __init__(self, version=512):
		if version == 512:
			self.__version = version
			#print self.Iv
		elif version == 256:
			self.__version = version
			#print self.Iv
		else:
			print "Не допустимая длина хеша"

	@staticmethod
	def intToBin(n):
		B = bin(n)
		if B[:2] == "0b":
			return bin(n)[2:]
		else:
			raise TypeError("Not bin string")

	@staticmethod
	def prepareHex(h):
		Hex = h
		if (Hex[-1] == 'L'):
			Hex = Hex[:-1]
		if Hex[:2] == '0x':
			Hex = Hex[2:]
		return Hex
		

	def hexArrayToInt(self, Hex):
		Result = ''
		for h in Hex:
			k = self.prepareHex(hex(h))		
			if len(k) == 2:
				Result += k
			else:
				Result += ('0'+k)
		return int(Result,16)


	def toHexArray(self, n):
		Hex = self.prepareHex(hex(n))
		Hex = '0'*(128-len(Hex)) + Hex
		Result = []
		for i in xrange(64):
			Result.append(int('0x'+Hex[2*i]+Hex[2*i+1],16))
		return Result

	def S(self, n):
		State = self.toHexArray(n)
		Result = []
		for i in xrange(64):
			Result.append(Sbox[State[i]])

		return self.hexArrayToInt(Result)

	
	def P(self, n):
		State = self.toHexArray(n)
		State = [State[Tau[i]] for i in xrange(64)]
		
		return self.hexArrayToInt(State)

	def L(self, n):
		t = 0
		Result = ''
		Bin = self.intToBin(n)
		Bin = '0'*(512-len(Bin)) + Bin
		Bin = [i for i in Bin]
		Bin.reverse()
		for i in xrange(8):
			for j in xrange(64):
				if Bin[64*i+j] == '1':
					t = t ^ A[63-j] << 64*i
		return t

	def KeySchedule(self, K, i):
		Ki = K ^ C[i]
		Ki = self.S(Ki)
		Ki = self.P(Ki)
		Ki = self.L(Ki)
		return Ki

	def E(self, K, m):
		Ki    = K
		state = m ^ Ki
		
		for i in xrange(12):
			state = self.S(state)
			state = self.P(state)
			state = self.L(state)
			Ki 	  = self.KeySchedule(Ki,i)
			state = state ^ Ki
			
		return state

	def compress(self, N, h, m):
		K    = h ^ N
		K    = self.S(K)
		K    = self.P(K)
		K    = self.L(K)
		t    = self.E(K, m)
		t    = t ^ h
		newh = t ^ m
		return newh

	def setMessage(self, Msg):

		self.__message       = int(self.prepareHex(Msg),16)
		self.__lengthMessage = len(self.prepareHex(Msg))*4


	def stage1(self):
		#initialization
		if self.__version == 512:
			self.__h = 0
		else:
			self.__h = int('00000001'*64,2)
		self.__M      = self.__message
		self.__length = self.__lengthMessage
		self.__N      = 0
		self.__Sigma  = 0
		
		
	def stage2(self):
		while self.__length >= 512:
			self.__m       = self.__M & ((1<<512) - 1)
			self.__h       = self.compress(self.__N, self.__h, self.__m)
			self.__N       = (self.__N + 512) % pow(2,512)
			self.__Sigma   = (self.__Sigma + self.__m) % pow(2,512)
			self.__M     >>= 512
			self.__length -= 512

	def stage3(self):

		self.__m     = self.__M ^ (1 << self.__length)
		self.__h     = self.compress(self.__N, self.__h, self.__m)
		self.__N     = (self.__N + self.__length) % pow(2,512)
		self.__Sigma = (self.__Sigma + self.__m)  % pow(2,512)
		self.__h     = self.compress(0, self.__h, self.__N)				
		self.__h     = self.compress(0, self.__h, self.__Sigma)

		if self.__version == 256:
			self.__h >>= 256

	def hash(self,m):
		self.setMessage(m)
		
		self.stage1()
		self.stage2()
		self.stage3()

		return self.__h

	def selfTesting(self):
		
		M1 = '0x323130393837363534333231303938373635343332313039383736353433323130393837363534333231303938373635343332313039383736353433323130'
		M2 = '0xfbe2e5f0eee3c820fbeafaebef20fffbf0e1e0f0f520e0ed20e8ece0ebe5f0f2f120fff0eeec20f120faf2fee5e2202ce8f6f3ede220e8e6eee1e8f0f2d1202ce8f0f2e5e220e5d1'

		H1_512 = 0x486f64c1917879417fef082b3381a4e211c324f074654c38823a7b76f830ad00fa1fbae42b1285c0352f227524bc9ab16254288dd6863dccd5b9f54a1ad0541b
		H1_256 = 0x00557be5e584fd52a449b16b0251d05d27f94ab76cbaa6da890b59d8ef1e159d

		H2_512 = 0x28fbc9bada033b1460642bdcddb90c3fb3e56c497ccd0f62b8a2ad4935e85f037613966de4ee00531ae60f3b5a47f8dae06915d5f2f194996fcabf2622e6881e
		H2_256 = 0x508f7e553c06501d749a66fc28c6cac0b005746d97537fa85d9e40904efed29d

		
		print hex(self.hash(M2))

if __name__ == '__main__':
	
	M1 = '0x323130393837363534333231303938373635343332313039383736353433323130393837363534333231303938373635343332313039383736353433323130'
	M = 0x01323130393837363534333231303938373635343332313039383736353433323130393837363534333231303938373635343332313039383736353433323130
	G = GOST()
	G256 = GOST(256)

	print hex(G.hash(M1))
	print hex(G256.hash(M1))


