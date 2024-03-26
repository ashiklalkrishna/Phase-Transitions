import numpy as np
from numpy import tanh
import matplotlib.pyplot as plt

def bisection(y, a, b): 
    for i in range(50):
            x = (a + b) /2
            if y(x)* y(a) < 0:
                b = x
            if y(x) * y(a) > 0:
                a=x
    return x

J = 1
Kb = 1
d = 2

B = np.arange(-3, 3, 0.0250)
T = [3, 4, 5] 

M_B = []

for t in T:
    mag = []
    for b in B: 
        def y(m):
            return tanh(((2*d*J*m)/(Kb*t)+(b/(Kb*t)))) - m  
        m = bisection(y, 2, -2) 

        mag.append(m)
    M_B.append(mag)

m_subc = M_B[0]
m_c = M_B[1]
m_supc = M_B[2]

plt.plot(B, m_subc, label='$T<T_c$', color ='navy', marker='s', markevery=5, markersize=5, markerfacecolor='none', markeredgecolor='navy', markeredgewidth=1, alpha=0.5)
plt.plot(B, m_c, label='$T=T_c$', color ='red', marker='o', markevery=5, markersize=5, markerfacecolor='none', markeredgecolor='red', markeredgewidth=1, alpha=0.5)
plt.plot(B, m_supc, label='$T>T_c$', color ='green', marker='^', markevery=5, markersize=5, markerfacecolor='none', markeredgecolor='green', markeredgewidth=1, alpha=0.5)

plt.xlabel('Magnetic field (B)')
plt.ylabel('Magnetisation (M)')
plt.legend()
plt.grid()
plt.show()