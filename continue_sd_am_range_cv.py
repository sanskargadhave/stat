import numpy  as np
lower =np.array([5,10,15,20,25,30,35])
upper=np.array([10,15,20,25,30,35,40])
f=np.array([7,11,14,17,16,2,5])
m=(upper+lower)/2
N=np.sum(f)
s1=np.sum(f*m)
s2=np.sum(f*m*m)
L=np.max(upper)
s=np.min(lower)
am=(s1/N)
var=(s2/N)-(am*am)
sd=np.sqrt(var)
cv=(sd/abs(am))*100
R=L-s
c_r=(L-s)/(L+s)
print('am=',am,'var=',var,'sd=',sd,'cv=',cv,'Range=',R,'coef_range=',c_r)