def choose_task():
    print("Выберите задачу (введите нужную цифру):")
    print("1: Поиск расстояния между городами")
    print("2: Опредение того, лежит ли точка внутри круга")
    print("3: Вывод формулы для получения введённого числа")
    print("4: Вывод первого, последнего, второго и предпоследнего фильма из списка")
    print("5: Вывод роста отца и суммарного роста всей семьи")
    print("6: ")
    print("7: ")
    print("8: ")
    print("9: ")
    print("10: ")
    print("11: ")
    number = try_input_num()


def try_input_num():
    try:
        number = int(input())
        return number
    except ValueError:
        print("Ошибка: введено не число!")
        try_input_num()


if __name__ == '__main__':
    choose_task()









