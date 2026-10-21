import matplotlib.pyplot as plt
import numpy as np
l=[20,3,40,50,70,100,140]
freq=[5,12,18,14,12,8]
widths=np.diff(l)
density=freq/widths

plt.bar(l[ :-1],density,width=widths,color='pink',edgecolor='black',align='edge')
plt.xlabel('classlimits')
plt.ylabel('frequency_density')
plt.title('histrogram for unequal class limits')
plt.show()