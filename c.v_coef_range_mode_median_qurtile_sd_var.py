import numpy as np

data=np.array([1,2,2,3,4,5,6,7,3,4,5,7,5])
Am=np.mean(data)
me=np.median(data)
q1=np.quantile(data,0.25)
q3=np.quantile(data,0.75)
p71=np.quantile(data,0.71)
var=np.var(data)
sd=np.std(data)
cv=(sd/abs(Am))*100
l=np.max(data)
s=np.min(data)
r=l-s
cofr=(r/(l+s))
print('Ari m:',Am,'median:',me)
print('q1:',q1,'q3:',q3,'p71',p71)
print('sd',sd,'variance',var,'coef_range',cofr)
print('range:',r,'\n','coefi of variance',cv)
