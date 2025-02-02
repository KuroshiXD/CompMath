import math


# Определение функции f(x)
def f(x):
    return x ** 3 - x ** 2 + 2


# Определение производной функции f(x)
def df(x):
    return 3 * x ** 2 - 2 * x


# Определение эквивалентной функции
def g(x):
    return (x - 2) / (x ** 2 - x + 1)


# Метод дихотомии для нахождения корня уравнения f(x) = 0
def bisection(f, a, b, tol=1e-6):
    # Проверка знаков на концах интервала
    if f(a) * f(b) > 0:
        print("Нет корня в данном интервале.")
        return
    # Итерационный процесс
    # Цикл до достижения заданной точности.
    while (b - a) / 2 > tol:
        # Нахождение середины интервала.
        c = (a + b) / 2
        # Если функция обращается в 0 на точке c, то корень найден
        if f(c) == 0:
            break
        # Если знаки на концах интервала разные, корень находится слева от середины.
        elif f(a) * f(c) < 0:
            # Обновление правой границы интервала.
            b = c
        # В противном случае, корень находится справа от середины.
        else:
            # Обновление левой границы интервала.
            a = c
    # Возврат приближенного значения корня.
    return (a + b) / 2


# Метод простых итераций для нахождения корня уравнения f(x) = 0
def simple_iteration(g, x0, tol=1e-6):
    # Итерационный процесс
    x1 = g(x0)
    # Цикл до достижения заданной точности.
    while abs(x1 - x0) > tol:
        # Обновление приближений.
        x0 = x1
        x1 = g(x1)
    # Возврат приближенного значения корня.
    return x1


# Метод Ньютона для нахождения корня уравнения f(x) = 0
def newton(f, df, x0, tol=1e-6):
    # Итерационный процесс
    # Вычисление следующего приближения методом Ньютона.
    x1 = x0 - f(x0) / df(x0)
    # Цикл до достижения заданной точности.
    while abs(x1 - x0) > tol:
        # Обновление приближений.
        x0 = x1
        x1 = x1 - f(x1) / df(x1)
    # Возврат приближенного значения корня.
    return x1


# Использование методов для нахождения корня уравнения f(x) = 0
print("Метод дихотомии: ", bisection(f, -200, 200))
print("Метод простых итераций: ", simple_iteration(g, 5))
print("Метод Ньютона: ", newton(f, df, 5))
