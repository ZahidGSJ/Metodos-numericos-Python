import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from PIL._imaging import display

sp.init_printing(use_latex=True)

def ImplicitEulerMethod(fp, x0, h, t0, tmax):
  n = int((tmax - t0)/h + 1)
  xtable = [0 for i in range(n)]
  xtable[0] = x0
  x = sp.symbols('x')
  for i in range(1,n):
    s = sp.nsolve(x - xtable[i - 1] - h*fp(x, t0 + i*h), x, xtable[i - 1])
    xtable[i] = s
  Data = [[t0 + i*h, xtable[i]] for i in range(n)]
  return Data

x = sp.Function('x')
t = sp.symbols('t')
sol = sp.dsolve(x(t).diff(t) - t*x(t)**2 - 2*x(t), ics={x(0): -5})
print(sol)
def fp(x, t): return t*x**2 + 2*x
Data = ImplicitEulerMethod(fp, -5.0, 0.1, 0, 5)
x_val = np.arange(0,5,0.01)
plt.plot(x_val, [sol.subs(t, i).rhs for i in x_val])
plt.scatter([point[0] for point in Data],[point[1] for point in Data],c='k')
plt.xlabel("t"); plt.ylabel("x")
plt.grid(); plt.show()
print(["t_i", "x_i"],"\n",np.vstack(Data))