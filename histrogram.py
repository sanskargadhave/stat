import matplotlib.pyplot as plt
l=[15,25,35,45,55,65,75]
freq=[11,17,21,18,12,8]

plt.bar(l[ :-1],freq,width=10,color='pink',edgecolor='black',align='center')
plt.xlabel('classlimits')
plt.ylabel('frequency')
plt.title('histrogram for equal class es')
plt.show()