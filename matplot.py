import matplotlib.pyplot as plt
import math
import random


x = []
y = []

for i in range (0,6,1):
    x.append(i)
for i in range(0,6,1):
    y.append(random.randrange(0,6))

plt.plot(x,y)
plt.show()
