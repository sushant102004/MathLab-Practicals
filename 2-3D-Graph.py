import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 6)

y = x**2
z = x**3

print('X', x)
print('Y', y)
print('Z', z)

plt.xlabel('X-Lable')
plt.ylabel('Y-Lable')

plt.grid(True)

plt.plot(y, z)
plt.plot(x, y)
plt.show()