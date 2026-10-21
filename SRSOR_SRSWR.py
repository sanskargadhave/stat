import numpy as np
p1=np.random.uniform(40,50,size=30)
p2=np.arange(1,41)
p3=np.array([1,2,3,4,5,6,7,19,23,12,4,5,27])
#SRSWR
s1=np.random.choice(p1,size=6)
s2=np.random.choice(p2,size=8)
s3=np.random.choice(p3,size=4)
#SRSWOR
s4=np.random.choice(p1,size=6,replace=False)
s5=np.random.choice(p2,size=8,replace=False)
s6=np.random.choice(p3,size=4,replace=False)

print('population p1:',p1)
print('arithmatic mean:',np.mean(s1))
print('SRSWR from p1:',s1)
print('arithmatic mean of srswor:',np.mean(s4))
print('SRSWOR from p1:',s4)

print('population p2:',p2)
print('arithmatic mean:',np.mean(s2))
print('SRSWR from p1:',s2)
print('arithmatic mean of srswor:',np.mean(s5))
print('SRSWOR from p1:',s5)

print('population p3:',p3)
print('arithmatic mean:',np.mean(s3))
print('SRSWR from p1:',s3)
print('arithmatic mean of srswor:',np.mean(s6))
print('SRSWOR from p1:',s6)

