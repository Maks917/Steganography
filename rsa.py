from random import choice

# Вычисление простых чисел
def getPrime(minN, maxN, flag = False, primes = []):
	for num in range(minN, maxN):
		for get in range(2,num):
			if num % get == 0:
				flag = True
				break
		if not flag:
			primes.append(num)
		flag = False
	return primes

# Подбор открытой экспоненты
def getPubExp(minN, maxN, Fn, pubExp = []):
	for e in range(minN, maxN):
		d = int((1 + 2 * Fn) / e)
		if d * e == 1 + 2 * Fn:
			pubExp.append(e)
	return pubExp

# Подбор натурального числа k
def getNumK(minN, maxN, Fn, e, numK = []):
	for k in range(minN, maxN):
		d = int((1 + k * Fn) / e)
		if d * e == 1 + k * Fn:
			numK.append(k)
	return numK

# Получение приватной экспоненты
def getPrivExp(e, n, Fn, k):
	d = int((1 + k * Fn) / e)
	if d * e != 1 + k * Fn:
		raise SystemExit
	return d

# Генерация ключей
def generateKeys(minP, maxP, maxN):
	primes = getPrime(minP,maxP)
	
	p, q = choice(primes), choice(primes)
	if p == q: return generateKeys(minP, maxP, maxN)

	n, Fn = p*q, (p-1)*(q-1)
	try:
		pubExp = choice(getPubExp(2, maxN, Fn))
		numK = choice(getNumK(2, maxN, Fn, pubExp))
		privExp = getPrivExp(pubExp, n, Fn, numK)

	except: return generateKeys(minP, maxP, maxN)

	if pubExp > privExp: return generateKeys(minP, maxP, maxN)

	return ([pubExp,n], [privExp,n])

# Шифрование / Расшифрование
def encryptDecrypt(message, key):
	return message ** key[0] % key[1]

# Вывод ключей персонажа
def getKeys(name, pub, priv):
	return '''%s's keys:
- Public_key: [%d.%d]
- Private_key: [%d.%d]\n'''%\
	(name, pub[0], pub[1], priv[0], priv[1])
"""
'''
# Передача открытого сообщения и цифровой подписи #

# Алиса генерирует ключи
pubA, privA = generateKeys(125,250,50)

# Вывод публичных и приватных ключей
print(getKeys("Alice", pubA, privA))

# Создание сообщения со стороны Алисы
mAlice = 111

# Создание цифровой подписи со стороны Алисы
sAlice = encryptDecrypt(mAlice, privA) 

# Создание прообраза сообщения публичным ключом Алисы
_mAlice = encryptDecrypt(sAlice, pubA)
print(" m = %s : _m = %s"%(mAlice, _mAlice))

# Проверка цифровой подписи
if mAlice == _mAlice: print("Signature is True")
'''

#'''
# Передача зашифрованного сообщения и цифровой подписи #

# Алиса и Боб генерируют ключи
pubA, privA = generateKeys(50,150,50)
pubB, privB = generateKeys(150,30,50)

# Вывод публичных и приватных ключей
print(getKeys("Alice", pubA, privA))
print(getKeys("Bob", pubB, privB))

# Создание сообщения со стороны Алисы
keys = [784,795]
mAlice1 = 784
mAlice2 = 795

mAlice = [mAlice1, mAlice2]
# Создание цифровой подписи со стороны Алисы
sAlice1 = encryptDecrypt(mAlice1, privA)
sAlice2 = encryptDecrypt(mAlice2, privA)

# Передача публичного ключа от Боба Алисе
pubB = [pubB[0], pubB[1]]

# Шифрование сообщения и подписи публичным ключом Боба
CmAlice1 = encryptDecrypt(mAlice1, pubB)
CsAlice1= encryptDecrypt(sAlice1, pubB)
CmAlice2 = encryptDecrypt(mAlice2, pubB)
CsAlice2 = encryptDecrypt(sAlice2, pubB)

# Передача зашифрованного сообщения и подписи Бобу
CsmAlice = [[CmAlice1, CsAlice1], [CmAlice2, CsAlice2]]

# Расшифрование сообщения и подписи Алисы
DmBob1 = encryptDecrypt(CsmAlice[0][0], privB)
DsBob1 = encryptDecrypt(CsmAlice[0][1], privB)

DmBob2 = encryptDecrypt(CsmAlice[1][0], privB)
DsBob2 = encryptDecrypt(CsmAlice[1][1], privB)


# Создание прообраза сообщения публичным ключом Алисы
_mAlice1 = encryptDecrypt(DsBob1, pubA)
_mAlice2 = encryptDecrypt(DsBob2, pubA)
print(" m = %s : _m = %s"%(DmBob1, _mAlice1))
print(" m = %s : _m = %s"%(DmBob2, _mAlice2))

# Проверка цифровой подписи
if _mAlice1 == DmBob1 and mAlice2 == DmBob2: print("Signature is True")
#'''
"""







