import rsa
import desktop

# Алиса и Боб генерируют ключи
pubA, privA = rsa.generateKeys(75,150,25)
pubB, privB = rsa.generateKeys(150,225,25)

# Вывод публичных и приватных ключей
print(rsa.getKeys("Alice", pubA, privA))
print(rsa.getKeys("Bob", pubB, privB))

try:
    key1 = int(input("Enter first key : "))
    key2 = int(input("Enter second key : "))
except TypeError:
    raise SystemExit


# Алиса и Боб генерируют ключи
pubA, privA = rsa.generateKeys(50,500,100)
pubB, privB = rsa.generateKeys(500,900,100)

# Вывод публичных и приватных ключей
print(rsa.getKeys("Alice", pubA, privA))
print(rsa.getKeys("Bob", pubB, privB))

# Создание сообщения со стороны Алисы
mAlice1 = key1
mAlice2 = key2

mAlice = [mAlice1, mAlice2]
# Создание цифровой подписи со стороны Алисы
sAlice1 = rsa.encryptDecrypt(mAlice1, privA)
sAlice2 = rsa.encryptDecrypt(mAlice2, privA)

# Передача публичного ключа от Боба Алисе
pubB = [pubB[0], pubB[1]]

# Шифрование сообщения и подписи публичным ключом Боба
CmAlice1 = rsa.encryptDecrypt(mAlice1, pubB)
CsAlice1 = rsa.encryptDecrypt(sAlice1, pubB)
CmAlice2 = rsa.encryptDecrypt(mAlice2, pubB)
CsAlice2 = rsa.encryptDecrypt(sAlice2, pubB)

# Передача зашифрованного сообщения и подписи Бобу
CsmAlice = [[CmAlice1, CsAlice1], [CmAlice2, CsAlice2]]

# Расшифрование сообщения и подписи Алисы
DmBob1 = rsa.encryptDecrypt(CsmAlice[0][0], privB)
DsBob1 = rsa.encryptDecrypt(CsmAlice[0][1], privB)

DmBob2 = rsa.encryptDecrypt(CsmAlice[1][0], privB)
DsBob2 = rsa.encryptDecrypt(CsmAlice[1][1], privB)


# Создание прообраза сообщения публичным ключом Алисы
_mAlice1 = rsa.encryptDecrypt(DsBob1, pubA)
_mAlice2 = rsa.encryptDecrypt(DsBob2, pubA)
print(" m = %s : _m = %s"%(DmBob1, _mAlice1))
print(" m = %s : _m = %s"%(DmBob2, _mAlice2))

# Проверка цифровой подписи
if _mAlice1 == DmBob1 and mAlice2 == DmBob2: print("Signature is True")
#'''


