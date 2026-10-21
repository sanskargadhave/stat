import matplotlib.pyplot as plt
limit=[15,25,35,45,55,65,75]
f=[9,13,17,15,10,4]
plt.bar(limit[:-1],f,width=10,color='red',edgecolor='black')
plt.xlabel('class limit')
plt.ylabel('freq')
plt.title('histogram for equal class width')
plt.show()
