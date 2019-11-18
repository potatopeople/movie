import random
a = '2530047598'
c = ''
b = random.sample('!@#$%^&*!@#$%^&*',10)
for x,item in enumerate(b):
    c += b[x]+a[x]
print(c)