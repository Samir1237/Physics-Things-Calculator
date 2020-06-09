# OBJETIVO: Calculadora de Figuras e Sólidos Geométricos
import math

pi = 3.14
resp = str(input("Put the name of the figure (ex.: Square): "))

f1 = ['Square', 'Retangule', 'Quadrilateral', 'Paralelogram']
f2 = ['Triangule']
f3 = ['Trapeze']
# f4 = ['Circle', 'Semicircle']

h = 10
w = 1
a = 10


class Figure():
    height = 1
    width = 1
    area = 1

    def __init__(self, height, width, area):
        self.height = height
        self.width = width
        self.area = area

    def display(self):
        print("Height = " + str(self.height))
        print("Width = " + str(self.width))
        print("Area = " + str(self.area))

    def calculate(self):
        pass


#criar classe de tipos de figura#
class FigureType:

if resp in f1:
    def calculate(self):
        self.area = self.width * self.height


    obj = Figure(w, h)  # test
    obj.calculate()
    obj.display()
elif resp in f2:
    def calculate(self):
        self.area = (self.width * self.height) / 2

    obj = Figure(w, h)  # test
    obj.calculate()
    obj.display()

elif resp in f3:
    def calculate(self):
        self.area = (self.width * self.height) / 2

    obj = Figure(w, h)  # test
    obj.calculate()
    obj.display()
