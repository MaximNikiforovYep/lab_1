from tasks.task0 import find_distance
from tasks.task1 import circle_area
from tasks.task1 import is_point_inside_circle
from tasks.task2 import exp_find_main
from tasks.task3 import find_films
from tasks.task4 import get_family_member_height
from tasks.task4 import get_total_height
from tasks.task5 import Zoo
from tasks.task6 import find_total_play_time_of_songs_list
from tasks.task6 import find_total_play_time_of_songs_dict
from tasks.task7 import decryption_sec_mess
from tasks.task8 import Flowers
from tasks.task9 import find_best_shops
from tasks.task10 import find_cost_for_goods

def choose_task():
    print("Выберите действие (введите нужную цифру):\n"
          "1: Поиск расстояния между городами\n"
          "2: Опредение того, лежит ли точка внутри круга, а также площади круга \n"
          "3: Вывод формулы для получения введённого числа\n"
          "4: Вывод первого, последнего, второго и предпоследнего фильма из списка\n"
          "5: Вывод роста отца и суммарного роста всей семьи\n"
          "6: Система управления зоопарком\n"
          "7: Поиск общего времени звучания песен\n"
          "8: Расшифровка секретного сообщения\n"
          "9: Исследование цветов с луга и сада\n"
          "10: Поиск магазинов с минимальными ценами на продукты \n"
          "11: Вывод стоимости каждого вида товара на складе \n"
          "12: Завершить работу\n")

    number = try_input_num(1, 12)

    if number == 1:
        task_1()
    elif number == 2:
        task_2()
    elif number == 3:
        task_3()
    elif number == 4:
        task_4()
    elif number == 5:
        task_5()
    elif number == 6:
        task_6()
    elif number == 7:
        task_7()
    elif number == 8:
        task_8()
    elif number == 9:
        task_9()
    elif number == 10:
        task_10()
    elif number == 11:
        task_11()
    elif number == 12:
        return
    choose_task()


def try_input_num(range_first, range_second):
    try:
        number = int(input())
        if number < range_first or number > range_second:
            raise ValueError("Num out range")
        return number
    except ValueError as ex:
        if "Num out range" in str(ex):
            print("Число вне диапазона.")
        else:
            print("Ошибка: введено не число.")
        return try_input_num(range_first, range_second)


def task_1():
    print("Выберите действие:\n"
          "1: Ввод координат городов \n"
          "2: Использовать значение по умолчанию: \n"
          " сites = {\n"
          "     \'Moscow\': (550, 370),\n"
          "     \'London\': (510, 510),\n"
          "     \'Paris\': (480, 480),\n"
          " }\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        cities = {}
        print("Введите число городов:")
        cities_cnt = try_input_num(1, 2667417)
        print("Введите через запятую для каждого из " + str(cities_cnt) +
              " : название города, первую его координату, вторую координату")
        for i in range(cities_cnt):
            print(str(i+1) + " город: ")
            city_data = input()
            city, x_str, y_str = map(str.strip, city_data.split(','))
            x = int(x_str)
            y = int(y_str)
            cities[city] = (x, y)
        print(find_distance(cities))
        print()
    elif number == 2:
        cities = {
            'Moscow': (550, 370),
            'London': (510, 510),
            'Paris': (480, 480),
        }
        print(find_distance(cities))
        print()
    elif number == 3:
        return


def task_2():
    print("Выберите действие:\n"
          "1: Ввод радиуса и точек\n"
          "2: Использовать значение по умолчанию: \n"
          " radius = 42\n"
          " point_1 = (23, 34)\n"
          " point_2 = (30, 30)\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        print("Введите радиус:")
        radius = try_input_num(0, 10**100)
        print("Введите количество точек")
        points_cnt = try_input_num(0, 10**100)
        print("Введите через запятую координаты каждой из " + str(points_cnt) +
              " точек: первая координата, вторая координата")
        points = []
        for i in range(points_cnt):
            print(str(i + 1) + " точка: ")
            point_data = input()
            x_str, y_str = map(str.strip, point_data.split(','))
            x = int(x_str)
            y = int(y_str)
            points.append((x, y))
        i = 0
        for point in points:
            i += 1
            print("Точка " + str(i) + " " + str(is_point_inside_circle(point, radius)))
        print()
    elif number == 2:
        radius = 42
        point_1 = (23, 34)
        point_2 = (30, 30)
        print("Площадь круга равна " + str(circle_area(radius)))
        print("Точка 1: " + str(is_point_inside_circle(point_1, radius)))
        print("Точка 2: " + str(is_point_inside_circle(point_2, radius)))
        print()
    elif number == 3:
        return


def task_3():
    print("Выберите действие:\n"
          "1: Ввод выражения и целевого числа: \n"
          "2: Использовать значение по умолчанию: \n"
          " numbers = [1, 2, 3] \n"
          " target = 9 \n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        numbers = input("Введите числа через пробел: ").split()
        numbers = list(map(int, numbers))
        target = int(input("Введите целевое число: "))
        exp_find_main(numbers, target)
        print()
    elif number == 2:
        numbers = [1, 2, 3]
        target = 9
        exp_find_main(numbers, target)
        print()
    elif number == 3:
        return


def task_4():
    print("Выберите действие:\n"
          "1: Ввод списка фильмов\n"
          "2: Использовать значение по умолчанию: \n"
          " movies = \'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее\'\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        print("Введите список фильмов через запятую:")
        movies = input()
        films = find_films(movies)
        print("Первый фильм:", films[0])
        print("Последний фильм:", films[1])
        print("Второй фильм:", films[2])
        print("Второй с конца фильм:", films[3])
        print()
    elif number == 2:
        movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'
        films = find_films(movies)
        print("Первый фильм:", films[0])
        print("Последний фильм:", films[1])
        print("Второй фильм:", films[2])
        print("Второй с конца фильм:", films[3])
        print()
    elif number == 3:
        return


def task_5():
    print("Выберите действие:\n"
          "1: Ввод роста семьи\n"
          "2: Использовать значение по умолчанию: \n"
          " my_family_height = [\n"
          "   ['мама', 165],\n"
          "   ['папа', 180],\n"
          "   ['бабушка', 155],\n"
          " ]\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        print("Введите количество членов семьи:")
        members_cnt = try_input_num(0, 10*100)
        my_family_height = []
        print("Введите " + str(members_cnt) + " членов семьи (с маленькой буквы) и их рост через запятую")
        for i in range(members_cnt):
            print(str(i + 1) + " член семьи: ")
            family_member_data = input()
            family_member, height_str = map(str.strip, family_member_data.split(','))
            height = int(height_str)
            my_family_height.append([family_member, height])

        if (get_family_member_height(my_family_height, "папа") == "Error") and (get_family_member_height(my_family_height, "отец") == "Error"):
            print("Ошибка, в вашей семье нет отца")
        else:
            print("Рост отца: " + str(get_family_member_height(my_family_height, "папа")))
        print("Суммарный рост членов семьи" + str(get_total_height(my_family_height)))
        print()
    elif number == 2:
        my_family_height = [
           ['мама', 165],
           ['папа', 180],
           ['бабушка', 155],
        ]
        print("Рост отца: " + str(get_family_member_height(my_family_height, "папа")))
        print("Суммарный рост членов семьи: " + str(get_total_height(my_family_height)))
        print()
    elif number == 3:
        return


def task_6():
    print("Выберите действие:\n"
          "1: Управление зоопарком\n"
          "2: Пример управления зопарка: \n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        sub_task_6()
    elif number == 2:
        zoo = Zoo(['lion', 'kangaroo', 'elephant', 'monkey'])
        print("Дан список животных: ")
        zoo.print()

        print("Посадим медведя (bear) между львом и кенгуру")
        zoo.insert(1, 'bear')
        zoo.print()

        print("Добавим птиц из списка birds в последние клетки зоопарка (birds = ['rooster', 'ostrich', 'lark', ])")
        birds = ['rooster', 'ostrich', 'lark', ]
        zoo.extend(birds)
        zoo.print()

        print("Уберём слона")
        zoo.remove('elephant')
        zoo.print()

        print("Выведём на консоль в какой клетке сидит лев (lion) и жаворонок (lark).")
        lion_index = zoo.find_pos('lion')
        lark_index = zoo.find_pos('lark')

        print(f'Лев сидит в клетке номер {lion_index}')
        print(f'Жаворонок сидит в клетке номер {lark_index}')

        print()
    elif number == 3:
        return


def sub_task_6(zoo_arg=None):
    if zoo_arg is None:
        zoo_arg = Zoo([])
    print("Выберите действие:\n"
          "1: Обнуление списка животных и ввод нового:\n"
          "2: Добавление животного на определённую позицию:\n"
          "3: Добавление подсписка животных в конец основного списка:\n"
          "4: Удаление животного:\n"
          "5: Поиск позиции на которой находится животное:\n"
          "6: Вывод списка животных:\n"
          "7: Выход\n")

    number = try_input_num(1, 7)
    zoo = zoo_arg
    if number == 1:
        animals = input("Введите животных через пробел: ").split()
        zoo = Zoo(animals)
        print()
        sub_task_6(zoo)
    elif number == 2:
        number = int(input("Введите позицию: "))
        animal = input("Введите животное: ")
        zoo.insert(number, animal)
        print()
        sub_task_6(zoo)
    elif number == 3:
        animals = input("Введите животных через пробел: ").split()
        zoo.extend(animals)
        print()
        sub_task_6(zoo)
    elif number == 4:
        animal = input("Введите животное: ")
        zoo.remove(animal)
        print()
        sub_task_6(zoo)
    elif number == 5:
        animal = input("Введите животное: ")
        print(zoo.find_pos(animal))
        print()
        sub_task_6(zoo)
    elif number == 6:
        zoo.print()
        print()
        sub_task_6(zoo)
    elif number == 7:
        return


def task_7():
    print("Выберите действие:\n"
          "1: Ввод списка песен, их временя звучания, ввод песен для поиска общего звучания\n"
          "2: Использовать значение по умолчанию: \n"
          " violator_songs_list = [\n"
          "     ['World in My Eyes', 4.86],\n"
          "     ['Sweetest Perfection', 4.43],\n"
          "     ['Personal Jesus', 4.56],\n"
          "     ['Halo', 4.9],\n"
          "     ['Waiting for the Night', 6.07],\n"
          "     ['Enjoy the Silence', 4.20],\n"
          "     ['Policy of Truth', 4.76],\n"
          "     ['Blue Dress', 4.29],\n"
          "     ['Clean', 5.83],\n"
          " ]\n"
          "\n"
          " songs_to_calculate = [\n"
          "     ['Halo'], \n"
          "     ['Enjoy the Silence'],\n"
          "     ['Clean']\n"
          " ]\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        violator_songs_list = eval(
            input("Введите список песен в формате [['Название1', длительность1], ['Название2', длительность2], ...]: "))
        user_input = input("Введите названия песен для определения их общего звучания через запятую: ")
        song_names = [name.strip() for name in user_input.split(',')]
        print(find_total_play_time_of_songs_list(violator_songs_list, song_names))
        print()
    elif number == 2:
        violator_songs_list = [
                 ['World in My Eyes', 4.86],
                 ['Sweetest Perfection', 4.43],
                 ['Personal Jesus', 4.56],
                 ['Halo', 4.9],
                 ['Waiting for the Night', 6.07],
                 ['Enjoy the Silence', 4.20],
                 ['Policy of Truth', 4.76],
                 ['Blue Dress', 4.29],
                 ['Clean', 5.83],
        ]
        song_names = ['Halo', 'Enjoy the Silence', 'Clean']
        print(find_total_play_time_of_songs_list(violator_songs_list, song_names))
        print()
        print()
    elif number == 3:
        return


def task_8():
    print("Выберите действие:\n"
          "1: Расшифровать сообщение:\n"
          " secret_message = [\n"
          "   'квевтфпп6щ3стмзалтнмаршгб5длгуча',\n"
          "   'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',\n"
          "   'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',\n"
          "   'ьд5фму3ежородт9г686буиимыкучшсал',\n"
          "   'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',\n"
          " ]\n"
          "2: Назад\n")

    number = try_input_num(1, 2)
    if number == 1:
        print("Секретное сообщение:" + decryption_sec_mess())
        print()
    elif number == 2:
        return


def task_9():
    print("Выберите действие:\n"
          "1: Ввод цветов\n"
          "2: Пример исследования\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        sub_task_9()
    elif number == 2:
        flowers_garden = Flowers(('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', ))
        print("Дан список цветов в саду: ")
        flowers_garden.print()

        flowers_meadow = Flowers(('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', ))
        print("Дан список цветов на лугу: ")
        flowers_meadow.print()

        print("Все виды цветов:")
        print(flowers_garden.union_flowers(flowers_meadow.get_flowers()))

        print("Те цветы, которые растут и там и там: ")
        print(flowers_garden.intersection_flowers(flowers_meadow.get_flowers()))

        print("Те цветы, которые растут в саду, но не растут на лугу")
        print(flowers_garden.difference_flowers(flowers_meadow.get_flowers()))

        print("Те цветы, которые растут на лугу, но не растут в саду")
        print(flowers_meadow.difference_flowers(flowers_garden.get_flowers()))
        print()
    elif number == 3:
        return


def sub_task_9(garden_flowers_arg=None, meadow_flowers_arg=None):
    if garden_flowers_arg is None:
        garden_flowers_arg = Flowers(())
        meadow_flowers_arg = Flowers(())
    print("Выберите действие:\n"
          "1: Обнуление списков цветов и ввод новых\n"
          "2: Вывод списков\n"
          "3: Вывод всех видов цветов\n"
          "4: Вывод тех, которые растут и там и там\n"
          "5: Вывод тех, которые растут в саду, но не растут на лугу\n"
          "6: Вывод тех, которые растут на лугу, но не растут в саду\n"
          "7: Выход\n")

    number = try_input_num(1, 7)
    flowers_garden = garden_flowers_arg
    flowers_meadow = meadow_flowers_arg
    if number == 1:
        garden_input = input("Введите названия цветов в саду через запятую: ")
        garden = [flow.strip() for flow in garden_input.split(',')]
        flowers_garden = Flowers(garden)
        meadow_input = input("Введите названия цветов на лугу через запятую: ")
        meadow = [flow.strip() for flow in meadow_input.split(',')]
        flowers_meadow = Flowers(meadow)
        print()
        sub_task_9(flowers_garden, flowers_meadow)
    elif number == 2:
        flowers_garden.print()
        flowers_meadow.print()
        print()
        sub_task_9(flowers_garden, flowers_meadow)
    elif number == 3:
        print(flowers_garden.union_flowers(flowers_meadow.get_flowers()))
        print()
        sub_task_9(flowers_garden, flowers_meadow)
    elif number == 4:
        print(flowers_garden.intersection_flowers(flowers_meadow.get_flowers()))
        print()
        sub_task_9(flowers_garden, flowers_meadow)
    elif number == 5:
        print(flowers_garden.difference_flowers(flowers_meadow.get_flowers()))
        print()
        sub_task_9(flowers_garden, flowers_meadow)
    elif number == 6:
        print(flowers_meadow.difference_flowers(flowers_garden.get_flowers()))
        print()
        sub_task_9(flowers_garden, flowers_meadow)
    elif number == 7:
        return


def task_10():
    print("Выберите действие:\n"
          "1: Ввод магазинов, товаров и цен:\n"
          "2: Пример работы на значении по умолчанию:\n"
          " shops = {\n"
          "     'ашан':\n"
          "         [\n"
          "             {'name': 'печенье', 'price': 10.99},\n"
          "             {'name': 'конфеты', 'price': 34.99},\n"
          "             {'name': 'карамель', 'price': 45.99},\n"
          "             {'name': 'пирожное', 'price': 67.99}\n"
          "         ],\n"
          "     'пятерочка':\n"
          "         [\n"
          "             {'name': 'печенье', 'price': 9.99},\n"
          "             {'name': 'конфеты', 'price': 32.99},\n"
          "             {'name': 'карамель', 'price': 46.99},\n"
          "             {'name': 'пирожное', 'price': 59.99}\n"
          "         ],\n"
          "     'магнит':\n"
          "         ["
          "             {'name': 'печенье', 'price': 11.99},\n"
          "             {'name': 'конфеты', 'price': 30.99},\n"
          "             {'name': 'карамель', 'price': 41.99},\n"
          "             {'name': 'пирожное', 'price': 62.99}\n"
          "         ],\n"
          " }\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        shops = {}
        while True:
            shop_name = input("Введите название магазина (или 'stop' для завершения): ").strip()
            if shop_name.lower() == 'stop':
                break
            products = []
            while True:
                product_name = input(
                    f"Введите название товара для магазина '{shop_name}' (или 'stop' для завершения ввода товаров): ").strip()
                if product_name.lower() == 'stop':
                    break
                try:
                    product_price = float(input(f"Введите цену для товара '{product_name}': ").strip())
                except ValueError:
                    print("Цена должна быть числом. Попробуйте еще раз.")
                    continue
                products.append({'name': product_name, 'price': product_price})
            shops[shop_name] = products

        print("Введенные данные о магазинах:")
        print(shops)
        print(find_best_shops(shops))
        print()
    elif number == 2:
        shops = {
            'ашан':
                [
                    {'name': 'печенье', 'price': 10.99},
                    {'name': 'конфеты', 'price': 34.99},
                    {'name': 'карамель', 'price': 45.99},
                    {'name': 'пирожное', 'price': 67.99}
                ],
            'пятерочка':
                [
                    {'name': 'печенье', 'price': 9.99},
                    {'name': 'конфеты', 'price': 32.99},
                    {'name': 'карамель', 'price': 46.99},
                    {'name': 'пирожное', 'price': 59.99}
                ],
            'магнит':
                [
                    {'name': 'печенье', 'price': 11.99},
                    {'name': 'конфеты', 'price': 30.99},
                    {'name': 'карамель', 'price': 41.99},
                    {'name': 'пирожное', 'price': 62.99}
                ],
        }
        print(find_best_shops(shops))
        print()
    elif number == 3:
        return


def task_11():
    print("Выберите действие:\n"
          "1: Ввод кодов товаров, списка количества товаров на складе и их цен:\n"
          "2: Пример работы на значении по умолчанию:\n"
          " goods = {\n"
          "    'Лампа': '12345',\n"
          "    'Стол': '23456',\n"
          "    'Диван': '34567',\n"
          "    'Стул': '45678',\n"
          " }\n\n"
          " store = {\n"
          "     '12345': [\n"
          "         {'quantity': 27, 'price': 42},\n"
          "     ],\n"
          "     '23456': [\n"
          "         {'quantity': 22, 'price': 510},\n"
          "         {'quantity': 32, 'price': 520},\n"
          "     ],\n"
          "     '34567': [\n"
          "         {'quantity': 2, 'price': 1200},\n"
          "         {'quantity': 1, 'price': 1150},\n"
          "     ],\n"
          "     '45678': [\n"
          "         {'quantity': 50, 'price': 100},\n"
          "         {'quantity': 12, 'price': 95},\n"
          "         {'quantity': 43, 'price': 97},\n"
          "     ],\n"
          " }\n"
          "3: Назад\n")

    number = try_input_num(1, 3)
    if number == 1:
        goods = {}
        store = {}

        # Ввод данных о товарах и их кодах
        print("Введите данные о товарах (название и код). Введите 'stop' для завершения ввода.")
        while True:
            product_name = input("Введите название товара (или 'stop' для завершения): ").strip()
            if product_name.lower() == 'stop':
                break

            product_code = input(f"Введите код для товара '{product_name}': ").strip()
            goods[product_name] = product_code

        # Ввод данных о количестве и цене товаров на складе
        print("\nВведите данные о наличии товаров на складе.")
        for product_name, product_code in goods.items():
            print(f"\nТовар: {product_name} (код: {product_code})")
            store[product_code] = []

            while True:
                try:
                    quantity = int(input(
                        f"Введите количество для товара '{product_name}' (или '0' для завершения ввода): ").strip())
                    if quantity == 0:
                        break
                    price = float(input(f"Введите цену за единицу для товара '{product_name}': ").strip())
                except ValueError:
                    print("Неправильный ввод. Попробуйте еще раз.")
                    continue

                # Добавляем запись о наличии на складе
                store[product_code].append({'quantity': quantity, 'price': price})

        # Выводим введенные данные для проверки
        print("\nВведенные данные о товарах:")
        print("goods =", goods)
        print("\nВведенные данные о наличии на складе:")
        print("store =", store)
        find_cost_for_goods(goods, store)
        print()
    elif number == 2:
        goods = {
            'Лампа': '12345',
            'Стол': '23456',
            'Диван': '34567',
            'Стул': '45678',
        }

        store = {
            '12345': [
                {'quantity': 27, 'price': 42},
            ],
            '23456': [
                {'quantity': 22, 'price': 510},
                {'quantity': 32, 'price': 520},
            ],
            '34567': [
                {'quantity': 2, 'price': 1200},
                {'quantity': 1, 'price': 1150},
            ],
            '45678': [
                {'quantity': 50, 'price': 100},
                {'quantity': 12, 'price': 95},
                {'quantity': 43, 'price': 97},
            ],
        }

        find_cost_for_goods(goods, store)
        print()
    elif number == 3:
        return


if __name__ == '__main__':
    choose_task()
