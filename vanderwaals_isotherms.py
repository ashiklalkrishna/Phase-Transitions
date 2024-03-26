import numpy as np
import matplotlib.pyplot as plt

R = 0.083145
a = 5.537
b = 0.03049
V = np.linspace(0.04, 0.2, 100)

Tc = 8*a/(27*R*b)
T = [700, 600, 500, 400, Tc]

def van (v, t):
    p = ( (R * t) / (v - b) ) - (a / (v**2) )
    return p

for t in T:
    P = []
    for v in V:
        p = van(v, t)
        P.append(p)
    
    plt.plot(V, P, label=f'T={t:}')

plt.xlabel('Volume (V)')
plt.ylabel('Preassure (P)')
plt.ylim(-800, 1000)
plt.grid()
plt.legend()
plt.show()
