import numpy as np
x=np.array([10,11,12,13,14,15,16,17])
f=np.array([7,12,16,20,14,11,8,3])
mode_val_index=np.argmax(f)
mode=x[mode_val_index]
print('mode=',mode)