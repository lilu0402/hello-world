import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0,20,100)
plt.plot(x, np.sin(x),'b+', x, np.cos(x)**5, 'ro', linewidth=2)
plt.grid(axis='both')
plt.show()