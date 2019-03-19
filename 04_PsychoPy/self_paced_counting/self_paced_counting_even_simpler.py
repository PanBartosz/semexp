from psychopy import visual, core, event, data
from random import choice

window = visual.Window(fullscr=False,
                    size = (1366,786),
                    monitor='Default',
                    units='norm')

patterns = ['00000000',
           '11000000',
           '00111000',
           '00000111']

dots = []
masks = []

for i in range(8):
    dots.append(visual.Circle(window,
                              radius=0.1,
                              pos = (-0.7 + i * 0.2, 0),
                              fillColor = choice(['blue', 'red']),
                              lineWidth = 3,
                              units = 'height'))

    masks.append(visual.Circle(window,
                              radius=0.1,
                              pos = (-0.7 + i * 0.2, 0),
                              fillColor = (0,0,0),
                              lineWidth = 3,
                              units = 'height'))

for pattern in patterns:
    continueRoutine = True
    while True:
        keys = event.getKeys()
        if 'return' in keys:
            break
        if 'q' in keys or 'w' in keys:
            continueRoutine = False
            break
        for dot in dots:
            dot.draw()
        for mask, v in zip(masks, list(pattern)):
            mask.draw() if v == '0' else None
        window.flip()
    if not continueRoutine:
        break
