# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:35:45 2020

@author: yuvra
"""

from PIL import Image #importing Image Processing Library from pillow
import numpy as np
from Crypto import Random
from struct import pack

key = b'11010011110111011101110110101110111011100001101'

im1 = Image.open("lena.png", "r")
arr = im1.load() #pixel data stored in this 2D array
w,h=im1.size #saving value of image dimension in 2 variables w,h
#print(arr)

x=list(im1.getdata())#Returns the contents of this image as a sequence object containing pixel values
print(type(x))
test=np.asarray(x)
#print(test)
x1=" ".join(str(a) for a in x)#replaces all commas with space
print(type(x1))

plaintext = bytes(x1, 'utf-8')#converting x1 into bytes from str
print(type(plaintext))
from Crypto.Cipher import Blowfish

bs = Blowfish.block_size
iv = Random.new().read(bs)

print(type(plaintext))
print(type(iv))

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg1 = iv + cipher.encrypt(plaintext + padding)

#prints encrypted data
#print(msg1)

ciphertext = msg1
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)

last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]

#prints decrypted data
print("Decryption")

msg=str(msg, 'utf-8')

#print(x2)
#print(msg)
print(type(msg))
print("Hello")
#msg=list(msg)
msg=np.asarray(msg)
np.save('geekfile', msg)
#np.reshape(msg, (1,1,1))
print(msg)
print(type(msg))

#print(msg)
#print(type(msg))
#print(type(msg))

#print(msg[0])

'''
a=ciphertext.split()#cipher text to array data
arrr=[]
for i in range(0,h):#saving data to arrr[]
    arrr.append([])
    for j in range(0,w):
        arrr[i].append(a[j])
#for i in range(0,1):
   # print(arrr[i])

#data = np.zeros((h, w, num), dtype=np.uint8)
#img = Image.fromarray(data, 'RGB')
#img.save('my.png')
#img.show()
#saving and displaying encypted image
#im1.save("newsencrypted.png")
#im1.show("newsencrypted.png")

'''