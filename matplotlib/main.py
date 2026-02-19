import matplotlib
import matplotlib.pyplot as plt
import numpy as np
print(matplotlib.__version__)

# xpoint = np.array([1, 6])
# ypoint = np.array([10, 250])
# plt.plot(xpoint, ypoint) # choziq chizadi.
# plt.plot(xpoint, ypoint, marker='o') # nuqta chizadi.

# xpt = np.array([1,3,8,7,6])
# ypt = np.array([10,250,250,120,200])
# plt.plot(xpt, ypt, marker='2')

# ypoints = np.array([10,250,250,120,200])
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'g', mfc = 'r')

ys = np.array([1,2,3,4,5,7,3,2,2,5,7,5,3])
plt.plot(ys, "-")
font1 = {"family": "serif", "color": "red", "weight": "normal", "size": 20}
plt.title("People count for lesson", fontdict=font1)
plt.xlabel("Days")
plt.ylabel("People count")

# plt.subplot(1,2,2)

plt.grid(axis= "y") #setkali ko'rinishga keltiradi.
plt.show() #chiqarish


