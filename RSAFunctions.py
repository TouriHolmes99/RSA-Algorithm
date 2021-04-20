def isPrime(n):
  if (n <= 1):
    return False
  for i in range(2, n):
    if (n % i == 0):
      return False
  return True
  
def modulus(p, q):
  return p * q
  
def eulerTotient(p, q):
  return (p - 1) * (q - 1)
  
def findFactors(x):
  factorList = []
  for i in range(1, x + 1):
    if x % i == 0:
      factorList.append(i)
  return factorList
  
def publicKeyCheck(eulerlist, keylist):
  for num in keylist:
    if num in eulerlist:
      if num != 1:
        print('invalid public key')
    else:
      print('public key is valid')
      break

def egcd(a, b):
  s = 0; Os = 1
  t = 1; Ot = 0
  r = b; Or = a

  while r != 0:
      quotient =  Or // r
      Or, r = r, Or - quotient * r
      Os, s = s, Os - quotient * s
      Ot, t = t, Ot - quotient * t

  return Or, Os, Ot

def modularInv(a, b):
  gcd, x, y = egcd(a, b)

  if x < 0:
      x += b

  return x

def encrypt(e, N, msg):
  cipher = ""

  for c in msg:
      m = ord(c)
      cipher += str(pow(m, e, N)) + " "

  return cipher

def decrypt(d, N, cipher):
  msg = ""

  parts = cipher.split()
  for part in parts:
      if part:
          c = int(part)
          msg += chr(pow(c, d, N))

  return msg

def privateKeyCheck(public, private, euler):
  if public * private % euler != 1:
    print('invalid private key') 
  
  else: 
    print('private key is valid')

print('Welcome to the RSA Algorithm Simulator.')
print('First you will need to select two Prime numbers.')

#step one generate two prime numbers
p = int(input('\nEnter a prime number (p): '))
q = int(input('Enter a prime number (q): '))

print("\nChecking to see if inputs are valid: ")
print(isPrime(p))
print(isPrime(q))

print("\nNow printing the Modulus (n):")
print(modulus(p, q))

print("\nNow printing the eulerTotient:")
print(eulerTotient(p, q))

publicKey = int(input("\nPlease Enter a number that has no common factors with EulerTotient: "))
print('This will be your public key (e).')

factorsEuler = findFactors(eulerTotient(p,q))

factorsKey = findFactors(publicKey)

print('\nVeryifying public Key:')

publicKeyCheck(factorsEuler, factorsKey)

print('\nGenerating and verifying private Key...')

d = modularInv(publicKey, eulerTotient(p, q) ) 
print('Private Key Successfully Generated.')

privateKeyCheck(publicKey, d, eulerTotient(p, q))

message = input('\nPlease enter a message to be encrypted.')

cipher = encrypt(publicKey, modulus(p, q) , message)

print('\nNow printing your encrypted message:')

print(encrypt(publicKey, modulus(p, q) , message))

print('\nNow printing your decrypted message:')

print(decrypt(d, modulus(p, q) , cipher))


