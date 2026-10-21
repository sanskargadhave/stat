#to find mode for distributed frequency distribution
import numpy as np

x=np.array([15,17,20,22,27,30,32,34])
f=np.array([7,14,18,24,20,14,8,2])

mode_index=np.argmax(f)
mode=x[mode_index]
print("Mode=",mode)

