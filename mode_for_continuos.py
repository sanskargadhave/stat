import numpy as np
lower=np.array([5,15,25,35,45,55])
upper=np.array([15,25,35,45,55,65])
f=np.array([7,12,6,20,14,11,8,3])
mod_class_ind=np.argmax(f)
L=lower[mod_class_ind]
f1=f[mod_class_ind]
f0=f[mod_class_ind-1]
f2=f[mod_class_ind+1]
h=upper[mod_class_ind]-lower[mod_class_ind]

mode=L+((f1-f0)/(2*f1-f0-f2))*h
print('mode=',mode)
