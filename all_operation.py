import numpy as np
from scipy import stats
data=np.array([6,7,6,8,4,6,5,5,8,7,6,5,4,6,3,9,7,8,8,7,6,5,4,6,9,3])
am=np.mean(data)
me=np.median(data)
mo=stats.mode(data)
 
q1=np.quantile(data,0.25)
q2=np.quantile(data,0.75)
d3=np.quantile(data,0.3)
p71=np.quantile(data,0.71)
 
sd=np.std(data)
var=np.var(data)
cv=(sd/abs(am))*100
l=np.max(data)
s=np.min(data)
range=l-s
coeff_range=(l-s)/(l+s)
  
print("AM=",am,"\nMedian=",me,"\nMode=",mo[0])
print("\nq1=",q1,"\nq2=",q2,"\nd3=",d3,"\np71=",p71)
print("\nvar=",var,"\nsd=",sd,"\ncv=",cv)
  
 
 
 
 
 