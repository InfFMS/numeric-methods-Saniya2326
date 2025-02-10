import matplotlib.pyplot as plt

import numpy as np

import random
from random import randint

x = np.linspace(-50, 50, 100)
y = x**3-x+1
plt.plot(x, y)
plt.show()