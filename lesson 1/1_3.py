# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
# +33 + 333 = 369.

number = input("Введите число ")
n_1 = int(number)
n_2 = int(f"{number}{number}")
n_3 = int(f"{number}{number}{number}")

print(f"{n_1} + {n_2} + {n_3} =", n_1 + n_2 + n_3)