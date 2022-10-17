import math

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0")
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

DiscR = b ** 2 - 4 * a * c

if DiscR > 0:
    x1 = (-b + math.sqrt(DiscR)) / (2 * a)
    x2 = (-b - math.sqrt(DiscR)) / (2 * a)
    print('x1 = ', x1, 'x2 = ', x2)
elif DiscR == 0:
    x = -b / (2 * a)
    print('x = ',x)
else:
    print('Корней нет.')