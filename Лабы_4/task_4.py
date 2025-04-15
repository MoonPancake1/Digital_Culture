"""
Задача 4:

Напишите программу, которая строит график функции y=sin(x) на интервале от −2π
до 2π, используя библиотеку matplotlib. Добавьте сетку и подписи осей. График
должен отображаться в отдельном окне.
"""

import matplotlib.pyplot as plt
import numpy as np


plt.style.use('_mpl-gallery')

x = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y = np.sin(x)
x2 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y2 = np.sin(x2)

fig, ax = plt.subplots()

fig.subplots_adjust(
    left=0.2,
    right=0.8,
    bottom=0.2,
    top=0.8,
)

ax.plot(x, y, linewidth=2.0)

ax.set( 
        xlim=(-2 * np.pi - 1, 2 * np.pi + 1), 
        xticks=np.arange(int(-2 * np.pi) - 1, int(2 * np.pi) + 2),
        ylim=(-2, 2), yticks=np.arange(-2, 3),
        xlabel='Ось X',
        ylabel='Ось Y',
        
    )

plt.show()

