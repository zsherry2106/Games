"""Solve Equations"""

import matplotlib.pyplot as plt
import numpy as np
import sympy

figure1, ax = plt.subplots()

x = sympy.Symbol('x')
y = sympy.Symbol('y')

xpoints = np.arange(-7, 5.1, 0.1)

f = sympy.solve((x-3)/2+(y+5)/3-11/6, y)
g = sympy.solve((x+3)/3-5/12-(y+3)/4, y)


ffunc = sympy.lambdify(x, f[0], 'numpy')
gfunc = sympy.lambdify(x, g[0], 'numpy')

ypoints1 = ffunc(xpoints)
ypoints2 = gfunc(xpoints)

ax.plot(xpoints, ypoints1, color = 'paleturquoise')
ax.plot(xpoints, ypoints2, color = 'aquamarine')

for i in range(len(xpoints)):
    if abs(ypoints1[i]-ypoints2[i]) < 0.00001:
        ax.plot(xpoints[i], ypoints1[i], marker = "o")
        countx = round(xpoints[i])
        county = round(ypoints1[i])
        print(f"{countx, county}")

plt.grid(True, which='both')

plt.show()
