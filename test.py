import FreeSimpleGUI as sg

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

layout = [
    [sg.Canvas(size=(100, 100), background_color='white', key='canvas')],
    [sg.Exit()],
]

w, h = 40, 30
k = 10

window = sg.Window('Dynamic Table', layout, finalize=True)

canvas = window['canvas'].TKCanvas
canvas.configure(width=k * w, height=k * h, bg="white")

for j in range(0, h):
    for i in range(0, w):
        x, y = k * i, k * j
        pixel = canvas.create_rectangle(x + 1, y + 1, x + k - 2, y + k - 2, fill=rgb(255, 128, 0))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
