#Задание №1
class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for row in self.my_list:
            for i in row:
                print(f'{i:3}', end="")
            print()
        return ""
    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

m = Matrix([[-1, 0, 1], [-1, 0, -1], [0, 1, -1]])
new_m = Matrix([[-2, 0, 2], [-2, 0, 2], [0, 2, -2]])
print(m.__add__(new_m))


#Задание №2
from abc import ABC, abstractmethod

class Clothes():

    def __init__(self, param):
        self.param = param


    def expenses(self):
        return f'Сумма затраченной ткани равна: {self.param / 6.5 + 0.5 + 2 * self.param + 0.3 :.2f}'

class Coat(Clothes):
    @property
    def expenses(self):
        return f'Для пошива пальто необходимо: {self.param / 6.5 + 0.5 :.2f} ткани'

class Suit(Clothes):
    @property
    def expenses(self):
        return f'Для пошива костюма необходимо: {2 * self.param + 0.3 :.2f} ткани'

summ = Clothes(164)
print(summ.expenses())
coat = Coat(140)
suit = Suit(24)

print(coat.expenses)
print(suit.expenses)


#Задание №3
class Cell:
    def __init__(self, param):
        self.param = int(param)

    def __add__(self, other):
        return f'Объединение двух клеток даёт: {self.param + other.param}'


    def __sub__(self, other):
        sub = self.param - other.param
        return f'Вычитание двух клеток даёт: {sub}'

    def __mul__(self, other):
        return f'Перемножение двух клеток даёт: {self.param * other.param}'


    def __truediv__(self, other):
        return f'Деление двух клеток даёт: {self.param // other.param}'

    def make_order(self, row):
        result = ""
        for i in range(int(self.param / row)):
            result += "*" * row + '\n'
        result += "*" * (self.param % row) + '\n'
        return result

cell = Cell(15)
cell_2 = Cell(5)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print("Организация ячеек по рядам:")
print(cell.make_order((5)))