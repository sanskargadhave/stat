import numpy as np

# Class intervals
lower = np.array([14,21,28,35,42,49,56,63])
upper = np.array([21,28,35,42,49,56,63,70])
freq  = np.array([7,11,14,24,22,16,10,4])

# Total frequency
N = np.sum(freq)

# Cumulative frequency
lcf = np.cumsum(freq)

# Find median class index
me_class_index = np.where(lcf >= N/2)[0][0]

# Extract values
L  = lower[me_class_index]                           # lower boundary of median class
h  = upper[me_class_index] - lower[me_class_index]   # class width
f  = freq[me_class_index]                            # frequency of median class
CF = lcf[me_class_index-1] 

# Median formula
median = L + (((N/2) - CF) / f) * h
print("Median =", median)