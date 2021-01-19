# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.

# l1 = [2, 3.3, 'Hello', None, 100]
#
# for x in l1:
#     print(x, type(x))

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().

# answer = int(input("Сколько значений вы хотите ввести? "))
# l2 = []
# i = answer
# while i > 0:
#     value = int(input(f"Введите значение под номером {i} "))
#     l2.append(value)
#     print("Текущие значения: ", l2)
#     i -= 1
#
# i = 1
# while i <= answer - 1:
#     l2[i], l2[i - 1] = l2[i - 1], l2[i]
#     i += 2
#
# print("Новые значения после перестановки: ", l2)

# print("Значения после обмена:")


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

# try:
#     month = int(input("Введите номер месяца: "))
#
#     months = [["январь", "Зима"], ["февраль", "Зима"], ["март", "Весна"], ["апрель", "Весна"],
#              ["май", "Весна"], ["июнь", "Лето"], ["июль", "Лето"], ["август", "Лето"],
#              ["сентябрь", "Осень"], ["октябрь", "Осень"], ["ноябрь", "Осень"], ["декабрь", "Зима"]]
#
#     print(months[month - 1][0], "-", months[month - 1][1].lower())
#
#     months_dict = {1: ["январь", "Зима"]
#                     ,2: ["февраль", "Зима"]
#                     ,3: ["март", "Весна"]
#                     ,4: ["апрель", "Весна"]
#                     ,5: ["май", "Весна"]
#                     ,6: ["июнь", "Лето"]
#                     ,7: ["июль", "Лето"]
#                     ,8: ["август", "Лето"]
#                     ,9: ["сентябрь", "Осень"]
#                     ,10: ["октябрь", "Осень"]
#                     ,11: ["ноябрь", "Осень"]
#                     ,12: ["декабрь", "Зима"]}
#
#     print(months_dict[month][0], "-", months_dict[month][1].lower())
# except IndexError as err:
#     print("Значение вне диапозона", err)

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

# string = input("Введите строку с пробелами: ")
#
# l3 = string.split(" ")
# for i, s in enumerate(l3, 1):
#     print(i, s[0:10:1])

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
#
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. Пользователь ввел число 3.
# Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
