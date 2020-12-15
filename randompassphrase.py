import random

lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPRSTUVWXYZ"
numbers='0123456789'
symbols='*&^%$#@!,.'
all = lower + upper + numbers + symbols
length= int(16)
passphrase =''.join(random.sample(all, length))
print(passphrase)
