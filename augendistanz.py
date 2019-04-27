import numpy as np

c1 = 1532
c2 = 2500
c3 = 1410

t1 = 15.8 * 10**(-4)
t2 = 23.5 * 10**(-4)
t5 = 72.9 * 10**(-4)

s1 = 0.5 * c1 * t1
s2 = 0.5 * c2 * t2 + s1
s3 = 0.5 * c3 * t5 + s2

print(s1) #cm
print(s2)
print(s3)