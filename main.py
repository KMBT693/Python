#Задание №1
my_f = open('my_test.txt', 'w')
line = input('Введите текст: \n')
while line:
    my_f.writelines(line)
    line = input('Введите текст: \n')
    if not line:
        break
my_f.close()
my_f = open('my_test.txt', 'r')
content = my_f.readlines()
print(content)
my_f.close()


# #Задание №2
my_f = open('my_test2.txt', 'r')
content = my_f.read()
print(f'Содержимое файла:\n{content}')

my_f = open('my_test2.txt', 'r')
content = my_f.readlines()
print(f'Количество строк в файле - {len(content)}')

my_f = open('my_test2.txt', 'r')
content = my_f.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1}-ой строки {len(content[i])}')

my_f = open('my_test2.txt', 'r')
content = my_f.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')

my_f.close()


#Задание №3
my_f = open('my_test3.txt', 'r', encoding='utf-8')
poor = []
sal = []
for i in my_f:
    i = i.split()
    if int(i[1]) < 20000:
        poor.append(i[0])
    sal.append(i[1])
print(f'Оклад меньше 20000 {poor}, средний оклад сотрудников {sum(map(int, sal))/10}')
my_f.close()


#Задание №4
rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
new_fl = []
with open('my_test4.txt', 'r', encoding='utf-8') as file_obj:
    for i in file_obj:
        i = i.split(" ", 1)
        new_fl.append(rus[i[0]] + " " + i[1])
    print(new_fl)

with open('my_test4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(new_fl)


#Задание №5
with open('my_test5.txt', 'w+') as file_obj:
    line = input('Введите числа через пробел: ')
    file_obj.writelines(line)
    my_numb = line.split()
print({sum(map(int, my_numb))})


#Задание №6
subj = {}
with open('my_test6.txt', 'r', encoding='utf-8') as init_f:
    for line in init_f:
        subject, lecture, practice, lab = line.split()
        subj[subject] = int(lecture) + int(practice) + int(lab)
    print(f'Общее количество часов по предмету: {subj}')


#Задание №7
import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('my_test7.txt', 'r', encoding='utf-8') as file_object:
    for line in file_object:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'Прибыль средняя - {prof_aver:.2f}')
    else:
        print(f'Прибыль отсутствует. Все работают в убыток')
    pr = {"Средняя прибыль": round(prof_aver)}
    profit.update(pr)
    print(f'Прибыль каждой компании: {profit}')

with open('my_test7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'Создан файл с расширением json со следующим содержимым:\n {js_str}')