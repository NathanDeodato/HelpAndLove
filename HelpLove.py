# Libs
import PySimpleGUI as sg
from random import randint

# Start
def HelpLove():
    sg.theme("BlueMono")

    layout = [
        [sg.Text("┣•", text_color="white"), sg.Text("Evol - Óla! Me chamo Evol, fui criado com o intuito de te ajudar,")],
        [sg.Text("┣•", text_color="white"), sg.Text("Tenho algumas funções para situações diversas,")],
        [sg.Text("┣•", text_color="white"), sg.Text("caso queira que eu te ajude, clique em uma das opções.")],
        [sg.Text("┣•", text_color="white"), sg.Text("Espero conseguir ajudar você, lembre-se, você é forte! <3")],

        [sg.Text("|───────────────────────────────────────────|", text_color="white")],

        [sg.Text(" " * 11), sg.Button("!Fé!", size=(9, 0), border_width=4), sg.Button("!Esperança!", size=(9, 0), border_width=4), sg.Button("!Amor!", size=(9, 0), border_width=4)],

        [sg.Text("|───────────────────────────────────────────|", text_color="white")],

        [sg.Output(size=(54, 8))],

        [sg.Text(" " * 35), sg.Text("(c) NT Developer")],
    ]
    return sg.Window("HelpLove", layout=layout)


window = HelpLove()

while True:
    try:
        event, values = window.Read()

        # Close Window
        if event == sg.WINDOW_CLOSED:
            break

        # !Fé!
        if event == "!Fé!":
            pass

        # !Eperança!
        if event == "!Esperança!":
            pass
    
        # !Amor!
        if event == "!Amor!":
            pass

    except Exception as error:
        print(f"{error}")
    
