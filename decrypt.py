from PIL import Image #importing Image Processing Library from pillow
import math

from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack
from numpy import asarray
# load the image
image = Image.open('new.png')
# convert image to numpy array
data = asarray(image)
#print(data)
'''
im1 = Image.open("new.png", "r")
arr = im1.load() #pixel data stored in this 2D array
w,h=im1.size #saving value of image dimension in 2 variables w,h



xres = w
yres = h

arr1=im1.load()
print(arr1)


x=list(im1.getdata())#Returns the contents of this image as a sequence object containing pixel values

x1=" ".join(str(a) for a in x)#replaces all commas with space



INPUT_SIZE = 120*120#defining block size


def pad_string(str):#fucntion for making all input bits equal to block size

	new_str = str
	pad_chars = INPUT_SIZE - (len(str) % INPUT_SIZE)

	if pad_chars != 0:
		for x in range(pad_chars):
			new_str += " "
		

	return new_str
'''
plaintext = data
#print(type(plaintext))
list1=plaintext.tolist()
#print(type(list1))
#print(list1)


#setting parameters for encryption initialization
#crypt_obj = Blowfish.new('11010011110111011101110110101110111011100001101', Blowfish.MODE_ECB)

bs = Blowfish.block_size
key = b'11010011110111011101110110101110111011100001101'
iv = Random.new().read(bs)
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg1 = cipher.encrypt(plaintext)
#print(msg1)

ciphertext = msg1

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)

print(msg)

#ciphertext = crypt_obj.encrypt(pad_string(plaintext))#encrypting scrambled image pixel data

#print ("PlainText:")
#print (plaintext)
#print ("CipherText:")


