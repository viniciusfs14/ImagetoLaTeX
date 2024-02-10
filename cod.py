from PIL import Image
from pix2tex.cli import LatexOCR
import PySimpleGUI as sg 

x = ""
instrucoes = 'O programa vai pedir o diretório da sua imagem então inserir o caminho da imagem como demonstrado o exemplo abaixo: \n \nC:\\Users\\55319\\Desktop\\teste.png'
sg.theme('LightBrown13')
window_size = (600,600)
layout = [
    [sg.Text('ImgToLaTeX', size=(300,1), justification='center', font=('Comic Sans',20), text_color='Black')],
    [sg.Text('')],
    [sg.Text('Instruções', size=(300,1), justification='center', font=('Comic Sans',15), text_color='Black')],
    [sg.Text('')],
    [sg.Multiline(default_text=instrucoes, size=(300,10), autoscroll = True, disabled = True, font=('Comic Sans',12))],
    [sg.InputText(key='-INPUT-', size=(300,1))],
    [sg.Text()],
    [sg.Button('Enviar', size=(300,1), font=('Comic Sans',12))],
    [sg.Text('', size=(300, 1), key='-OUTPUT-', font=('Comic Sans',12))]
]
window = sg.Window('ImgToLaTeX', layout, size=window_size)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Enviar':
        dir = values['-INPUT-']
        img = Image.open(dir)
        model = LatexOCR()
        x = model(img)
        window['-OUTPUT-'].update(x)

window.close()