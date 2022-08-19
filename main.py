#Задание №1
from time import sleep
class TrafficLight:
    _color = ["красный","жёлтый","зелёный"]

    def running(self):
        i = 0
        while i != 3:
            print(TrafficLight._color[i])
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            i += 1

t = TrafficLight()
t.running()

#Задание №2
class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def callculate(self):
        callculate = self._length * self._width * self.weight * self.height / 1000
        print(f"Для покрытия всего дорожного полотна неободимо {round(callculate)} массы асфальта")

r = Road(5000, 20)
r.callculate()


#Задание №3
class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position("Anton", "Boytsov", "PP", "50000", "20000")
print(p.get_full_name(), p.get_total_income())

#Задание №4
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police

    def go(self):
        return f'Автомобиль {self.name} движется'

    def stop(self):
        return f'Автомобиль {self.name} остановился'

    def turn(self, direction):
        return f'Автомобиль {self.name} повернул {direction}'

    def show_speed(self):
        return f'Ваша скорость {self.speed}'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Вы превысили допустимую скорость! Ваша скорость {self.speed}'
        else:
            return f'Скорость для {self.name} приемлемая'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Вы превысили допустимую скорость! Ваша скорость {self.speed}'
        else:
            return f'Скорость для {self.name} приемлемая'

class PoliceCar(Car):
    pass


town = TownCar("Kia", 50, "white", False)
print('1:' + town.go(), town.show_speed(), town.turn("Налево"), town.turn("Направо"), town.stop())

sport = SportCar("Audi", 120, "black", False)
print('2:' + sport.go(), sport.show_speed(), sport.turn("Направо"), sport.turn("Налево"), sport.stop())

work = WorkCar("Volvo", 40, "dirt", False)
print('3:' + work.go(), work.show_speed(), work.turn("Налево"), work.turn("Направо"), work.stop())

police = PoliceCar("BMW", 60, "Blue", True)
print('4:' + police.go(), police.show_speed(), police.turn("Направо"), police.turn("Налево"), police.stop())


#Задание №5
class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки"

class Pen(Stationery):
    def draw(self):
        return f'Чтобы {self.title}, Вам понадобится ручка!'

class Pencil(Stationery):
    def draw(self):
        return f'Для того, чтобы {self.title}, Вам подойдет карандаш!'

class Handle(Stationery):
    def draw(self):
        return f'Чтобы {self.title}, Вам необходим маркер!'

pen = Pen("что-то записать")
print("1:" + pen.draw())

pencil = Pencil("что-то зарисовать")
print("2:" + pencil.draw())

handle = Handle("что-то пометить")
print("3:" + handle.draw())

