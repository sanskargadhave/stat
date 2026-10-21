
import matplotlib.pyplot as plt
import numpy as np
limits=[20,30, 40,50,60,70,80,90]
freq=[5,13,21,29,21,14,8]
lcf=np.cumsum(freq)
new_lcf=np.insert(lcf,0,0)
plt.plot(limits,new_lcf,marker='o',linestyle='-',color='red')

plt.xlabel('class limits')
plt.ylabel("less than cumulative frequency")

plt.title("less than ogive")
plt.grid(True)
plt.show()

