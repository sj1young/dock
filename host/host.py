import PySimpleGUI as sg
import subprocess

layout = [[sg.Button("RStudio"), sg.Button("Spyder")], [sg.Button("IBMSas"), sg.Button("Orange")], [sg.Button("JuPYter"), sg.Button("Visual Studio")], [sg.Button("SonarQube"), sg.Button("Markdown")]]
window = sg.Window(title="ML Toolbox", layout=layout)

while True:
    event, values = window.read()
    if event == "Spyder":
        com = "./run_spyder.sh"
        subprocess.call(com)

    if event == "RStudio":
        subprocess.call("./run_rstudio.sh")

    if event == "IBMSas":
        subprocess.call("./run_sas.sh")

    if event == "Orange":
        subprocess.call("./run_orange.sh")

    if event == "JuPYter":
        subprocess.call("./run_jupyter.sh")

    if event == "Visual Studio":
        subprocess.call("./run_vs.sh")

    if event == "SonarQube":
        subprocess.call("./run_qube.sh")

    if event == "Markdown":
        subprocess.call("./run_md.sh")

    if event == sg.WIN_CLOSED:
        break

window.close()