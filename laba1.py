import random


# Функция решения системы линейных алгебраических уравнений методом Гаусса
def gauss_elimination(matrix):
    n = len(matrix)  # Определение размера матрицы (количество уравнений)

    # Прямой ход метода Гаусса
    for i in range(n):  # Итерация по каждой строке
        # Проверка наличия нулевого элемента на диагонали
        if matrix[i][i] == 0:
            # Поиск строки с ненулевым элементом в текущем столбце
            for k in range(i + 1, n):
                if matrix[k][i] != 0:  # Если найден ненулевой элемент
                    # Меняем местами текущую строку и строку с ненулевым элементом
                    matrix[i], matrix[k] = matrix[k], matrix[i]
                    break
            else:
                # Если весь столбец нулевой, то система не имеет единственного решения
                raise ValueError("Система не имеет единственного решения")

        # Приведение к верхнетреугольному виду
        for j in range(i + 1, n):  # Итерация по строкам ниже текущей
            factor = matrix[j][i] / matrix[i][i]  # Вычисление коэффициента
            for k in range(i, n + 1):  # Итерация по элементам в строке и правой части
                matrix[j][k] -= factor * matrix[i][k]  # Обнуление элементов

    # Обратный ход метода Гаусса
    x = [0] * n  # Инициализация списка для хранения решений
    for i in range(n - 1, -1, -1):  # Итерация в обратном порядке по строкам
        x[i] = matrix[i][n] / matrix[i][i]  # Вычисление значения переменной
        for j in range(i - 1, -1, -1):  # Итерация в обратном порядке по строкам выше текущей
            matrix[j][n] -= matrix[j][i] * x[i]  # Обновление правой части

    return x  # Возвращение списка значений переменных (решения СЛАУ)


# Запрос пользователя на ввод размерности матрицы
size = int(input("Введите размерность матрицы NxN: "))
# Генерация двумерного массива, т.е. самой матрицы
matrix = [[_ for _ in range(size + 1)] for _ in range(size)]

# Заполнение матрицы случайными значениями
for i in range(size):
    for j in range(len(matrix[size - 1])):
        rand = random.randint(0, 20)
        matrix[i][j] = rand

# Вывод матрицы по строкам
for i in matrix:
    print(i)

# Решение СЛАУ методом Гаусса
solution = gauss_elimination(matrix)
print("Решение СЛАУ:", solution)
