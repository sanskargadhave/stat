#to find median for continuous frequency distribution
import numpy as np

lower=np.array([10,15,20,25,30,35,40,45])
upper=np.array([15,20,25,30,35,40,45,50])
freq=np.array([7,11,18,22,20,14,10,4])

N=np.sum(freq)
lcf=np.cumsum(freq)
me_class_index=np.where(lcf>=N/2)[0][0]
L=lower[me_class_index]
cf=lcf[me_class_index-1]
f=freq[me_class_index]
h=upper[me_class_index]-lower[me_class_index]

median=L+((N/2-cf)/f)*h
print("Median=",median)

