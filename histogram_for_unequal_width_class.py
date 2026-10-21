import matplotlib.pyplot as plt
import numpy as np
limit=[30,40,50,70,100,140]
f=[7,12,20,15,20]
widths=np.diff(limit)
den=f/widths
plt.bar(limit[ : -1],den,width=widths,color='red',edgecolor='black')
plt.xlabel('class limit')
plt.ylabel('freq')
plt.title('histogram for unequal class width')
plt.show()