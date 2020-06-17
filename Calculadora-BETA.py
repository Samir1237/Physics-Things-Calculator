# OBJECTIVE: Calculadora de Figuras e Sólidos Geométricos
import PySimpleGUI as sg
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

class Screen:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('Select form:', size=(10,0)),sg.Input(size=(15,0),key='form')],
            [sg.Text('Put the value(m):', size=(10, 0)), sg.Input(size=(15, 0), key='input_1')],
            [sg.Text('Put the value(m):', size=(10, 0)), sg.Input(size=(15, 0), key='input_2')],
            [sg.Text('Put the value(m):', size=(10, 0)), sg.Input(size=(15, 0), key='input_3')],
            [sg.Text('Result: ', size=(10,0)),sg.Input(size=(15,0),key='result')],
            [sg.Button("Calculate")],
            [sg.Output(size=(30,20))]
        ]
        #Window
        self.window = sg.Window("Values").layout(layout)
        #Extracting values
        self.button, self.values = self.window.Read()

    def Iniciate(self):
        while True:
            self.button, self.values = self.window.Read()
'''
            form = self.form['form']
            area = self.area['result']
            print(f'Form: {self.form}')
            if form == '1':
                h = self.values['input_1']
                w = self.values['input_2']
                Quadrilateral(h, w)

            elif form == '2':
                h = self.values['input_1']
                w = self.values['input_1']
                Triangule(h, w)
    
            elif form == '3':
                h = self.values['input_1']
                m_base = self.values['input_2']
                l_base = self.values['input_3']
                Trapeze(h, m_base, l_base)
    
            elif form == '4':
                r = self.values['input_1']
                Circle(r)
'''
tela = Screen()
tela.Iniciate()


