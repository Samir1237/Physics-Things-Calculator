# OBJECTIVE: Calculadora de Figuras e Sólidos Geométricos
pi = 3.14

# square-retangule-quadrilateral-figure
def Quadrilateral (h, w):
    area = (h * w)
    print("Area: ", area," m²")

def Triangule (h, w):
    area = h * w / 2
    print("Area: ", area," m²")

def Trapeze (h, m_base, l_base):
    area = (h * (m_base + l_base))/ 2
    print("Area: ", area, " m²")

def Circle (r):
    area = (4)*(pi)*((r)**2)
    print("Area: ", area, " m²")

option = int(input('''
1- Quadrilateral
2- Triangule
3- Trapeze
4- Circle
     
Insert the option(only one number): '''))
if option == 1:
    h = float(input("Put the value of height(meters): "))
    w = float(input("Put the value of width(meters): "))
    Quadrilateral(h, w)

elif option == 2:
    h = float(input("Put the value of height(meters): "))
    w = float(input("Put the value of width(meters): "))
    Triangule(h, w)

elif option == 3:
    h = float(input("Put the value of height(meters): "))
    m_base = float(input("Put the value of minor base(meters): "))
    l_base = float(input("Put the value of larger base(meters): "))
    Trapeze(h, m_base, l_base)

elif option == 4:
    r = float(input("Put the value of radius(meters): "))
    Circle(r)

else:
    print("Try again :/")