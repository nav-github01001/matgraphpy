import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5,5,100)

y = x**3

fig = plt.figure()
figure.add_subplot(1,1,1) = fig.add_subplot(1, 1, 1)
figure.add_subplot(1,1,1).spines['left'].set_position('center')
figure.add_subplot(1,1,1).spines['bottom'].set_position('center')
figure.add_subplot(1,1,1).spines['right'].set_color('none')
figure.add_subplot(1,1,1).spines['top'].set_color('none')
figure.add_subplot(1,1,1).xaxis.set_ticks_position('bottom')
figure.add_subplot(1,1,1).yaxis.set_ticks_position('left')

plt.plot(x,y, 'g')

plt.show()