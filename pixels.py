import FreeSimpleGUI as sg

def rgb(r, g, b):
    return f'#{r:02x}{g:02x}{b:02x}'

w, h = 40, 30
k = 10

layout = [
    [sg.Graph(canvas_size=(k * w, k * h), graph_bottom_left=(0, k * h), graph_top_right=(k * w, 0), key='graph', background_color="white")],
    [sg.Exit()],
]

window = sg.Window('Gradient', layout, finalize=True)
graph = window['graph']

for j in range(0, h):
    for i in range(0, w):
        x, y = k * i, k * j
        graph.draw_rectangle((x + 1, y + 1), (x + k - 2, y + k - 2), fill_color=rgb(255, 128, 0))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
