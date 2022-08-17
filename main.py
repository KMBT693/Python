# # #Задание №1
from sys import argv
payday, output_in_hours, rate_per_hour, prize = argv
print("Наименование скрипта", payday)
print("\n << Программа рассчета заработной платы сотрудника >> ")
print("Выработка в часах:", output_in_hours)
print("Ставка в час:", rate_per_hour)
print("Премия:", prize)
print("Сотрудник должен получить:", (float(output_in_hours) * float(rate_per_hour)) + float(prize))

# #Задание №2
my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f"Исходный список: {my_list}")
new_list = []
for el in range(len(my_list) - 1):
    n = my_list[el]
    el += 1
    m = my_list[el]
    if m > n:
        new_list.append(m)
print("Новый список:", new_list)

# #Задание №3
my_list = list(range(20, 240))
new_list = [el for el in my_list if el % 20 == 0 or el % 21 == 0]
print(new_list)

# #Задание №4
my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)

# #Задание №5
from functools import reduce
my_list = list(range(100, 1001))
new_list = [el for el in my_list if el%2==0]
all_comp = reduce(lambda x,y: x*y, new_list)
print(all_comp)

# Задание №6
from itertools import count, cycle

for el in count(3):
     if el > 10:
         break
     print(el)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
c = 0
for el in cycle(my_list):
    if c > 25:
        break
    print(el, end =' ')
    c += 1

# Задание №7
from math import factorial

def func(n):
    for el in range(1, n+1):
        print(el, end='! = ')
        yield factorial(el)
        yield el

for el in func(5):
    print(el)

