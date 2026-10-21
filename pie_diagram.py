import matplotlib.pyplot as plt
x=['arts','compu','BA','Datasci','science']
value=[400,500,300,200,300]
plt.pie(value,labels=x,autopct='%1.1f%%')
plt.title('pie diagram')
plt.show()