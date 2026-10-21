import numpy as np
p=np.random.uniform(500,550,size=50)
n=int(input("enter sample size="))
N=len(p)
k=N//n

s1=np.random.randint(1,k)
s=p[s1: :k]

print("\npopulation=",p)
print("\nsystematic samples=",s)

print("\nam of population=",np.mean(p))

print("\nam of stratified sample =",np.mean(s))