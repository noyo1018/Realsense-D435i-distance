import numpy as np
import matplotlib.pyplot as plt

np1 = np.genfromtxt('D:\RealSense\Data\参佰mm.csv', delimiter=',')
print(np1)

Times = np1[:, 0]
distance = np1[:, 1]
plt.plot(Times, distance, label='distance')
plt.xlabel('Times')
plt.legend()
plt.show()