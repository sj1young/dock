import PySimpleGUI as sg

layout = [sg.Button("1"), sg.Button("2")]
window = sg.Window(title="test",layout = layout)

while True:
    event, values = window.read();
    
    if event == sg.WIN_CLOSED:
        break
        
window.close()
