# Poniższy kod ilustruje jak wykonać proste zadanie typu "self-paced counting".
# Zadanie to polega na tym, że badany naciskając klawisz odkrywa 2 lub 3 zamaskowane okręgi (dwa możliwe kolory).


from psychopy import visual, core, event, data
from random import randint

window = visual.Window(fullscr=True,
                    size = (1920,1080),
                    monitor='Default',
                    units='norm')

# Przygotowujemy sobie bodźce
welcome = visual.TextStim(window,
                          'Witamy w naszym prostym eksperymencie! Naciśnij ENTER aby kontynuować.')

instruction = visual.TextStim(window,
                              'Jeśli na ekranie mniej niż połowa kropek będzie niebieska, wciśnij klawisz Q, w innym wypadku wciśnij W.')

end = visual.TextStim(window, 'Dziękujemy za udział w eksperymencie!')

# Przygotowujemy sobie kółka oraz maski (też kółka w neutralnym kolorze). Wartości `pos` były dobrane drogą eksperymentowania.

circles = []
for i in range(2):
    for j in range(4):
        color = 'blue' if randint(0,1) == 1 else 'black'
        circles.append(visual.Circle(window, radius=0.1,
                                     pos = [-0.35 + j*0.25, 0.1 - i * 0.25 ],
                                     fillColor = color,
                                     lineColor = 'red',
                                     lineWidth = 3,
                                     units = 'height'))

masks = []
for i in range(2):
    for j in range(4):
        masks.append(visual.Circle(window,
                                   name = str(i*4 + j),
                                   radius=0.1,
                                   pos = [-0.35 + j*0.25, 0.1 - i * 0.25 ],
                                   fillColor = [0,0,0],
                                   lineColor = 'black',
                                   lineWidth = 3,
                                   units = 'height'))
        print(str(i*4+j))


# Ekran powitalny
while True:
    welcome.draw()
    if 'return' in event.getKeys():
        break
    window.flip()

# Instrukcje dla badanego
clock = core.Clock()
while clock.getTime() < 2:
    instruction.draw()
    window.flip()

# Główna próba badania
c = 0
# Wzorzec odkrywania - po 2 kółka
pattern = [['0','1'], ['2','3'], ['4','5'], ['6','7']] 
unmasked = []
while True:
    for circle in circles:
        circle.draw()

    for mask in masks:
        if mask.name not in unmasked:
            mask.draw()

    if event.getKeys(['q', 'w']):
        break

    if event.getKeys(['return']):
        try:
            unmasked = pattern[c] # ustawiamy "maskę" do kolejnego naciśnięcia spacji
            c += 1
        except:
            break # kiedy kończą się nam maski wyskakujemy z aktualnej próby

    window.flip()

# Wiadomość końcowa
clock = core.Clock()
while clock.getTime() < 2:
    end.draw()
    window.flip()
