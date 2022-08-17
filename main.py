#Задание №1
list = [1, 69, 'Hello', 25.6, 'Pyton', 4-3j]
for i in list:
    print(f'{i} is {type(i)}')

#Задание №2
s = input("Введите элементы списка через пробел: ").split()
for i in range(0, len(s)-1, 2):
    s[i], s[i+1] = s[i+1], s[i]
print(s)

#Задание №3
seasons = {'Зима': (1, 2, 12), "Весна": (3, 4, 5), "Лето": (6, 7, 8), "Осень": (9, 10, 11)}
month = int(input("Введите номер месяца: "))
if month < 1 or month > 12:
    print("Номер месяца введён неправильно!")
else:
    for key in seasons.keys():
        if month in seasons[key]:
            print(key)

#Задание №4
my_list = input("Введите слова разделяя каждое пробелом: ", )
my_list = (my_list.split())
my_list = [item[:10] for item in my_list]
for i, my_list in enumerate(my_list, 1):
    print(f'{i}. {my_list}')


#Задание №5
s = input("Введите несколько чисел через пробел: ").split()
s = [int(i) for i in s]
x = int(input("Введите новое число: "))
s.append(x)
s.sort(reverse = True)
print(f'Пользователь ввёл число {x}. Результат: {s}')


#Задание №6
s = []
i = 1
x = int(input("Сколько товаров Вы хотите завести: "))
for i in range (0, x):
    check = input("Введите данные товара через пробел: ").split(None)
    s.append((i, {"Название": check[0], "Цена": int(check[1]),"Количество": int(check[2]),"Ед.": check[3]}))
    i +=1
for W in s:
    print(W)
score = {"Название": [], "Цена": [], "Количество": [], "Ед.": []}
for el in s:
    score["Название"].append(el[1].get("Название"))
    score["Цена"].append(el[1].get("Цена"))
    score["Количество"].append(el[1].get("Количество"))
    score["Ед."].append(el[1].get("Ед."))
for key, el in score.items():
    print(key, el)