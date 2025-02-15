"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    __color = 'красный'

    def running(self):
        """Переключает сигнал светофора"""
        print(self.__color)  # вывод на экран начального сигнала
        cycle = ['красный', 'желтый', 'зеленый']  # список с порядком сигналов для проверки
        i = 0  # начальное значение счетчика
        while True:
            if self.__color == 'красный':
                time.sleep(7)
                self.__color = 'желтый'
            elif self.__color == 'желтый':
                time.sleep(2)
                self.__color = 'зеленый'
            elif self.__color == 'зеленый':
                time.sleep(5)
                self.__color = 'красный'
            i += 1  # увеличение счетчика
            if i >= len(cycle):  # если счетчик превысил длину списка сигналов
                i = 0  # обнуление счетчика
            if self.__color == cycle[i]:  # проверка правильности последовательности переключния сигналов
                print(self.__color)  # вывод текущего сигнала на экран
            else:
                break  # прерывание, при несоблюдении последовательности


tl = TrafficLight()
tl.running()
