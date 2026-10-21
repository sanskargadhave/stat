import matplotlib.pyplot as plt
import numpy as np
limits=[20,30, 40,50,60,70,80,90]
freq=[5,13,21,29,21,14,8]

reversefreq=list(reversed(freq))
gcf=np.cumsum(reversefreq)

new_gcf=np.insert(gcf,0,0)
reverse_newgcf=list(reversed(new_gcf))
plt.plot(limits,reverse_newgcf,marker='o',linestyle='-',color='red')

plt.xlabel('class limits')
plt.ylabel("greter than cumulative frequency")

plt.title("greter than ogive")
plt.grid(True)
plt.show()

