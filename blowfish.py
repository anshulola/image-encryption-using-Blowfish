from Crypto.Cipher import Blowfish
from Crypto import Random
from struct import pack

bs = Blowfish.block_size
key = b'11010011110111011101110110101110111011100001101'
iv = Random.new().read(bs)
cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
plaintext = b'(207, 96, 87) (197, 85, 81)'
plen = bs - divmod(len(plaintext),bs)[1]
padding = [plen]*plen
padding = pack('b'*plen, *padding)
msg1 = iv + cipher.encrypt(plaintext + padding)
print(msg1)

ciphertext = msg1
iv = ciphertext[:bs]
ciphertext = ciphertext[bs:]

cipher = Blowfish.new(key, Blowfish.MODE_CBC, iv)
msg = cipher.decrypt(ciphertext)

last_byte = msg[-1]
msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
print(repr(msg))