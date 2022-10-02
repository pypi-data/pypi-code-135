# Imports
import random, sys, os, rabinMiller, theMath

# FUNCTIONS
def generateKey(keyBuffer):
   p = rabinMiller.genLargePrime(keyBuffer)
   q = rabinMiller.genLargePrime(keyBuffer)
   n = p * q
	
   while True:
      e = random.randrange(2 ** (keyBuffer - 1), 2 ** (keyBuffer))
      if theMath.gcd(e, (p - 1) * (q - 1)) == 1:
         break
   
   d = theMath.modInverse(e, (p - 1) * (q - 1))
   pubKey = (n, e)
   privKey = (n, d)
   print('Public key:\n', pubKey)
   print()
   print('Private key:\n', privKey)
   return (pubKey, privKey)

def makeKeyFiles(filename, keyBuffer):
    if os.path.exists('%s_pubKey.txt' % (filename)) or os.path.exists('%s_privKey.txt' % (filename)):
      sys.exit('These files already exist, please input a different name on next attempt.')

    else:
        pubKey, privKey = generateKey(keyBuffer)
   
    print()
    print('The public key is a %s and a %s digit number.' % (len(str(pubKey[0])), len(str(pubKey[1])))) 
    print('Writing public key to file.')
    
    outfile = open('%s_pubKey.txt' % (filename), 'w')
    outfile.write('%s,%s,%s' % (keyBuffer, pubKey[0], pubKey[1]))
    outfile.close()
    print()

    print('The private key is a %s and a %s digit number.' % (len(str(pubKey[0])), len(str(pubKey[1]))))
    print('Writing private key to file.\n')
    
    outfile = open('%s_privkey.txt' % (filename), 'w')
    outfile.write('%s,%s,%s' % (keyBuffer, privKey[0], privKey[1]))
    outfile.close()

    print("Public and private keys files successfully created.")