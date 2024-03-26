import numpy as np
import matplotlib.pyplot as plt

n = 10
site_count = n*n
x_pos = np.zeros(site_count)
y_pos = np.zeros(site_count)
y = 0
i=0

for row in range(0, n):
    if row % 2 == 0:
        x = 0
    else:
        x = 0.5

    for col in range(0, n):
        x_pos[i] = x
        y_pos[i] = y
        x += 1
        i += 1
    y += 0.5

plt.scatter (x_pos, y_pos)
plt.show()
    
