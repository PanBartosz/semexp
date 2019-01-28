from psychopy import visual, core, event, data

window = visual.Window(fullscr=True,
                    size = (1920,1080),
                    monitor='Default',
                    units='norm')

welcome_msg = visual.TextStim(window,
                              text = 'Witamy w naszym eksperymencie! Wciśnij ENTER aby kontynuować')


while True:
    welcome_msg.draw()
    window.flip()
    if event.getKeys(['return']):
        break

STIMULI_LIST = ['Królowa Wielkiej Brytanii jest łysa',
                'Bonus RPK jest warszawskim raperem',
                'PsychoPy jest bardzo prosty w obsłudze.',
                'Każdy arab to terrorysta.']

sentence = visual.TextStim(window,
                           text = '')

feedback = visual.TextStim(window,
                           text = '')

for stimulus in STIMULI_LIST:
    sentence.text = stimulus
    while True:
        resp = event.getKeys()
        if 'q' in resp:
            feedback.text = 'Brawo! Naciśnięty został klawisz Q! Naciśnij ENTER aby przejść dalej.'
            break
        if 'w' in resp:
            feedback.text = 'Brawo! Naciśnięty został klawisz W! Naciśnij ENTER aby przejść dalej'
            break

        sentence.draw()
        window.flip()

    while True:
        if event.getKeys(['return']):
            break
        feedback.draw()
        window.flip()


rect_blue  = visual.Rect(window,
                         width = 0.3,
                         height = 0.3,
                         fillColor = 'blue',
                         pos = [-0.5, 0])

rect_red  = visual.Rect(window,
                        width = 0.3,
                        height = 0.3,
                        fillColor = 'red',
                        pos = [0.5, 0])


mouse = event.Mouse()

while True:
    if rect_red.contains(mouse.getPos()):
        if mouse.getPressed()[0] == 1:
            break
        rect_red.width = 0.4
    else:
        rect_red.width = 0.3

    if mouse.isPressedIn(rect_blue):
        rect_blue.height = 0.4
    else:
        rect_blue.height = 0.3

    rect_red.draw()
    rect_blue.draw()
    window.flip()


info = visual.TextStim(window,
                       text = '')

for _ in range(5):
    likert_scale = visual.RatingScale(window,
                                      low = 1,
                                      high = 9,
                                      scale = '1=nie podoba mi się badanie; 9=świetne badanie',
                                      precision = 0.5,
                                      labels = ['Zła odpowiedź', 'Dobra odpowiedź'])

    while likert_scale.noResponse:
        info.text = str(likert_scale.getRating()) + ' ' + str(likert_scale.getRT())
        info.draw()
        likert_scale.draw()
        window.flip()


