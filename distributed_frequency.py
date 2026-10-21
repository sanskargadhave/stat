import numpy as np
x=np.array([14,15,17,20,22,23,27])
F=np.array([7,11,16,20,17,12,8])
n=np.sum(F)
s1=np.sum(F*x)
s2=np.sum(F*x*x)
l=np.max(x)
s=np.min(x)

am=s1/n
var=(s2/n)-(am*am)
sd=np.sqrt(var)
cv=(sd/abs(am))*100
r=l-s
cr=(l-s)/(l+s)

print("A.M=",am,"\nvar=",var,"\nSD=",sd,"\nc.v=",cv)
print("\nRange=",r,"\nceff.of range=",cr)