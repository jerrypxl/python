def createAlphabet():
    charString = ''
    for i in range(32,127):
        charString += chr(i)

    return charString




def createBinKeyFromKey(key):
    s = bin(key)
    return s[2:]



def encryptCS8Cipher(plainText,key):
    encryptedString = ''
    alphabet = createAlphabet()
    binaryKey = createBinKeyFromKey(key)
    for i in range(0, len(plainText)):
        if binaryKey[i%len(binaryKey)]=='1':
            y = alphabet.find(plainText[i]) - key
            encryptedString = encryptedString + alphabet[y%len(alphabet)]
        else:
            encryptedString = encryptedString + alphabet[(alphabet.find(plainText[i])+key)%len(alphabet)]
            
    return encryptedString



def decryptCS8Cipher(plainText,key):
    decryptedString = ''
    alphabet = createAlphabet()
    binaryKey = createBinKeyFromKey(key)
    for i in range(0, len(plainText)):
        if binaryKey[i%len(binaryKey)]=='1':
            y = alphabet.find(plainText[i]) + key
            decryptedString = decryptedString + alphabet[y%len(alphabet)]
        else:
            decryptedString = decryptedString + alphabet[(alphabet.find(plainText[i])-key)%len(alphabet)]
            
    return decryptedString
            
        
    











    



                
            
        
        
    
