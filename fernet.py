from cryptography.fernet import Fernet
from tkinter import *
from tkinter import filedialog

privkey = Fernet.generate_key()
print("the private key for your encryption and decryption is")
print(privkey)

with open('pkey.key', 'wb') as keynote:
    keynote.write(privkey)

def encrypt():
    with open('pkey.key', 'rb') as keynote:
        key = keynote.read()
        keynote.close()
    fer = Fernet(key)
    
    
    filepath = filedialog.askopenfilename()
    #infile = open(filepath, 'rt')
    with open(filepath, 'rb') as inpt:
        fileread = inpt.read()
    
    encrypt = fer.encrypt(fileread)
    with open(filepath, 'wb') as enc:
        enc.write(encrypt)
def decrypt():      
    with open('pkey.key', 'rb') as keynote:
        key = keynote.read()
        #keynote.close()
    fer = Fernet(key)
    
    filepath = filedialog.askopenfilename()
    with open(filepath, 'rb') as enc:
        read = enc.read()
    
    decrypt = fer.decrypt(read)
    filepath = filedialog.askopenfile()
    with open(filepath, 'wb') as encr:
        encr.write(decrypt)
        
choice = str(input("do you want to initiate the encryption >. "))
if choice == 'yes':
    encrypt()

choice2 = str(input("do u want to decrypt this file >. "))
if choice == 'yes':
    decrypt()

 