# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

def pearson_correlation(array_1, array_2):
    if len(array_1) == len(array_2):
        n = len(array_1)
        average_x = sum(array_1) / n
        average_y = sum(array_2) / n
        x = sum([(x_i - average_x)**2 for x_i in array_1]) / n
        y = sum([(y_i - average_y)**2 for y_i in array_2]) / n
        covariance = sum([(x_i - average_x) * (y_i - average_y) for x_i, y_i in zip(array_1, array_2)]) / n
        correlation = covariance / (x * y)**0.5
        return correlation
    else:
        print('Массивы должны быть одинаковой длины')
        quit()

array_1 = [1, 2, 3, 4, 5, 7,]
array_2 = [8, 9, 10, 11, 12, 13,]

correlation = pearson_correlation(array_1, array_2)
print(f'Корреляция Пирсона: {correlation}')