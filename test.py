import FreeSimpleGUI as sg

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

w, h = 40, 30
k = 10

layout = [
    [sg.Canvas(size=(k * w, k * h), background_color='white', key='canvas')],
    [sg.Exit()],
]

window = sg.Window('Dynamic Table', layout, finalize=True)
canvas = window['canvas'].TKCanvas

for j in range(0, h):
    for i in range(0, w):
        x, y = k * i, k * j
        pixel = canvas.create_rectangle(x + 1, y + 1, x + k - 2, y + k - 2, fill=rgb(255, 128, 0))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
