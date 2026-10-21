import numpy as np
p1=np.arange(1,21)
p2=np.random.uniform(50,60,size=30)
p3=np.array([60,62,64,57,71,74,38,55,67,61.5,64.5,58.2,91,3,72])
#SRSWR
s1=np.random.choice(p1,size=5)
s2=np.random.choice(p2,size=7)
s3=np.random.choice(p3,size=4)

#SRSWOR
s4=np.random.choice(p1,size=5,replace=False)
s5=np.random.choice(p2,size=7,replace=False)
s6=np.random.choice(p3,size=4,replace=False)

print(" \npopulation p1=",p1)
print("\nam of  population p1=",np.mean(p1))
print("\nsrswr  from population p1=",s1)
print("\nam of srswr p1=",np.mean(s1))
print("\nsrswor  from population p1=",s4)
print("\nam of srswor p1=",np.mean(s4))

print("\npopulation p2=",p2)
print("\nam of  population p2=",np.mean(p2))
print("\nsrswr  from population 2=",s2)
print("\nam of srswr p2=",np.mean(s2))
print("\nsrswor  from population p2=",s5)
print("\nam of srswor p2=",np.mean(s5))

print("\npopulation p3=",p3)
print("\nam of  population p3=",np.mean(p3))
print("\nsrswr  from population p3=",s3)
print("\nam of srswr p3=",np.mean(s3))
print("\nsrswor  from population p3=",s6)
print("\nam of srswor p3=",np.mean(s6))