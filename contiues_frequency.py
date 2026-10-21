import numpy as np
lower=np.array([6,12,18,24,30,36,42])
upper=np.array([12,18,24,30,36,42,48])
f=np.array([11,14,18,21,20,17,9])

m=(lower+upper)/2
n=np.sum(f)
s1=np.sum(f*m)
s2=np.sum(f*m*m)
l=np.max(upper)
s=np.min(lower)

am=s1/n
var=(s2/n)-(am*am)
sd=np.sqrt(var)
cv=sd/abs(am)*100
r=l-s
coff_r=(l-s)/(l+s)

print("\nMean=",am,"\nVar=",var,"\nSd=",sd)
print("\nCv=",cv)
print("\nRange=",r,"\nCoefficient_Range=",coff_r)
