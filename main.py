from math import sin, pi
import matplotlib.pyplot as plt
from random import randint
import numpy as np
N = int(input('input size population '))+1
y = [[j for j in range(0, N)], [sin(5 * pi * (randint(0,101) / 100 ** 0.75) - 0.05) ** 6 for i in range(0, N)]]
# y2 = [[j for j in range(0, 101)], [sin(5 * pi * (i / 100 ** 0.75) - 0.05) ** 6 for i in range(0, 101)]]

for i in range(len(y[0])):
    print(y[0][i], y[1][i])

plt.plot(y[0],y[1])
plt.grid()
plt.show()

#Мера расстояния между особями популяции с1 с2
# save best kids
# Произвести М потомков
# Выбрать случайных Cf родителей
# Сравнить М потомков с Cf родителями
# М и Cf определяются пользователем
# Каждый потомок заменяет индивида из группы Cf
# М = N/10
# Cf = 3
# Где N - численность популяции