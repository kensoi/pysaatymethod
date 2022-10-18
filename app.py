"""
Лабораторная работа № 6
Выполнил Прокофьев Андрей Фт-210008
"""


def convert_to_int(value):
    """
    Вспомогательная функция для определения целочисленности
    """

    try:
        return int(value)

    except ValueError:
        return -1


def input_matrix(kritery_const):
    """
    Ввод отношений критериев в матрицу n*n
    """

    matrix = [[0] * kritery_const for i in range(kritery_const)]

    # Ввод отношений для верхней половины матрицы, считая от главной диагонали
    for i in range(kritery_const):
        for j in range(kritery_const):
            if i == j:
                matrix[i][j] = 1 # Элементы главной диагонали равны единице

            if i < j:
                while matrix[i][j] == 0:
                    # Для выхода из цикла ввода элемента ожидается верный ввод
                    temp = convert_to_int(
                        input(f"Введите отношение критерия {i+1} к критерию {j+1} >> "))

                    if (temp == -1) or (1 <= temp <= 9) is False:
                        # Проверка на соответствие условиям
                        print('Отношение должно быть целым числом от 1 до 9')

                    else:
                        matrix[i][j] = temp

    # Отражение матрицы по главной диагонали и возведение её элементов в -1 степень
    for i in range(len(kritery_const)):
        for j in range(len(kritery_const)):
            if i > j:
                matrix[i][j] = 1/matrix[j][i]

    return matrix


def output_matrix_precise(matrix):
    """
    Вывод матрицы попарных сравнений
    """

    print("Матрица попарного сравнения: ")
    print()

    for i in enumerate(matrix):
        for j in enumerate(matrix):
            print(f"{matrix[i][j]:.4f}", end="")

        print()


def count_weight_coefficients(matrix, sum_const):
    """
    Расчёт весовых коэффициентов
    """

    sum_column = 0
    response = []

    # расчёт суммы отношений для каждого критерия
    for i in enumerate(matrix):
        for j in enumerate(matrix):
            sum_column += matrix[j][i]

        response.append(sum_column/sum_const)

    return response


def main(kritery_count:int):
    """
    Главная функция программы
    """

    # Создание двумерного массива n*n
    matrix = input_matrix(kritery_count)
    output_matrix_precise(matrix)
    matrix_summed = sum(map(sum, matrix))

    print(f"Сумма элементов матрицы: {matrix_summed:.4f}")
    print()

    # Создание массива, хранящего весовые коэффициенты
    weight_coefficients = count_weight_coefficients(matrix, matrix_summed)
    weight_coefficients.reverse()

    print("Весовые коэффициенты:", end=" ")
    print()

    # Форматирование вывода для соответствия условиям задачи
    for i in weight_coefficients:
        print(f"{i:.2f}", end="")

    return 0


if __name__ == "__main__":
    N = 0

    while N == 0:
        # Цикл будет запрашивать ввод, пока количество не будет положительным целым числом

        N = convert_to_int(
            input("Введите количество критериев >> "))

        print()

        if (N == -1) or (N < 1):
            print("Количество критериев должно быть положительным целым числом")
            print()
            N = 0

    main(N)
