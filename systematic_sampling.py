import numpy as np
p=np.arange(1,100)
N=len(p)
n=int(input('enter the sample size:'))
k=N//n
s1=np.random.randint(0,k)
sample=p[s1: :k]
print('population:',p)
print('a.m of population:',np.mean(p))
print('systematic sampling:',sample)