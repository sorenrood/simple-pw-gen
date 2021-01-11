import random
char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

num = input('How many passwords would you like?\n')
num = int(num)
length = input('What about the length?\n')
length = int(length)

for p in range(num):
  password = ''
  for c in range(length):
    password += random.choice(char)
  print(password)