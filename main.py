#Задание №1
x = "Hello"
y = 22
z = 34.5
print(x, y, z)

x = input() #Запрос строки
y = int(input()) #Запрос числа
print(x, y)

#Задание №2
x = int(input())
a = x // 3600
b = (x - a * 3600)
c = b // 60
d = b - c * 60
print(f'{a}:{c}:{d}')

#Задание №3
n = int(input())
print(n + n**2 + n**3)

#Задание №4
x = int(input())
m = x % 10
x = x // 10
while x > 0:
    if x % 10 > m:
        m = x % 10
    x = x // 10
print(m)

#Задание №5 - 6
x = int(input("Введите значение выручки фирмы:"))
y = int(input("Введите значение издержек фирмы:"))
if x > y:
    x = x - y
    print("Фирма приносит прибыль равную", x)
    z = int(input("Введите количество сотрудников фирмы:"))
    print("Прибыль фирмы в расчёте на одного сотрудника состовляет:", x / z)
elif y < x:
    y = y - x
    print("Фирма приносит убыток равный", y)

#Задание №7
a = int(input())
b = int(input())
z = 1
#print(f'{z}-й день:{a}')
while a < b:
    a = a + a * 0.1
    a = round(a, 2)
    z = z+1
    #print(f'{z}-й день:{a}')
    if a >= b:
        print(f'На {z}-й день спортсмен достиг результата не менее: {a} км')