import FreeSimpleGUI as sg

def interp(t, a, b):
    return (1 - t) * a + t * b

def rgb(r, g, b):
    return f'#{int(r):02x}{int(g):02x}{int(b):02x}'

w, h = 40, 30
k = 10

layout = [
    [sg.Graph(canvas_size=(k * w + 1, k * h + 1), graph_bottom_left=(0, k * h), graph_top_right=(k * w, 0),
              key='graph', enable_events=True, drag_submits=True, background_color="white")],
    [sg.Exit()],
]

window = sg.Window('Gradient', layout, finalize=True)
graph = window['graph']
#canvas = window['canvas'].TKCanvas

for j in range(0, h):
    for i in range(0, w):
        x, y = k * i, k * j
        v = interp(i / (w - 1), 0, 1) * interp(j / (h - 1), 0, 1)
        graph.draw_rectangle((x + 1, y + 1), (x + k - 2, y + k - 2), fill_color=rgb(255 * v, 128, 0))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):
        break
