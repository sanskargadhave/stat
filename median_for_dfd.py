import numpy as np
x=np.array([7,8,9,10,11,12])
f=np.array([3,7,10,8,4,2])
data=np.repeat(x,f)
me=np.median(data)
 
q1=np.quantile(data,0.25)
q3=np.quantile(data,0.75)
d7=np.quantile(data,0.7)
p33=np.quantile(data,0.33)
 
print("\nMedian=",me)
print("\nFirst quantile=",q1,"\nThird quantile=",q3)
print("\nSeventh decile=",d7)
print("\nThirty three precentile=",p33)
 
 
 
 
 