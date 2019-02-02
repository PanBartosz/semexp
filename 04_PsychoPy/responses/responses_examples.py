from psychopy import visual, core, event, data

# PRZYKŁAD 1. Odpowiedzi za pomocą klawiatury
#############################################

window = visual.Window(fullscr=True,
                    size = (1920,1080),
                    monitor='Default',
                    units='norm')

welcome_msg = visual.TextStim(window,
                              text = 'Witamy w naszym eksperymencie! Wciśnij ENTER aby kontynuować')

while True:
    welcome_msg.draw()
    window.flip()
    # Najprostszy sposób reagowania na klawisze to funkcja `getKeys` z modułu `event`
    # Jako argument przyjmuje (opcjonalnie) listę klawiszy
    if event.getKeys(['return']): # jeśli lista jest niepusta, wyskakujemy z pętli
        break

# Lista bodźców tekstowych
STIMULI_LIST = ['Królowa Wielkiej Brytanii jest łysa',
                'Bonus RPK jest warszawskim raperem',
                'PsychoPy jest bardzo prosty w obsłudze.',
                'Każdy arab to terrorysta.']

sentence = visual.TextStim(window,
                           text = '')

feedback = visual.TextStim(window,
                           text = '')

# Prezentujemy na keranie zdania i oczekujemy jednej z dwóch odpowiedzi (na klawiaturze): Q albo W.
# Jeśli uzyskamy odpowiedź wyświetlamy krótką wiadomość dotyczącą odpowiedzi (jaki klawisz został naciśnięty) i czekamy na klawisz ENTER.
for stimulus in STIMULI_LIST:
    sentence.text = stimulus
    while True:
        # Jeśli nie zadeklarujemy klawiszy, to `getKeys` zwraca wszystkie naciśnięte klawisze
        resp = event.getKeys()
        if 'q' in resp: # jeśli naciśnięty klawisz to Q ustawiamy odpowiedni tekst naszego feedbacku i uciekamy z pętli
            feedback.text = 'Brawo! Naciśnięty został klawisz Q! Naciśnij ENTER aby przejść dalej.'
            break
        if 'w' in resp: # jeśli naciśnięty klawisz to W ustawiamy odpowiedni tekst naszego feedbacku i uciekamy z pętli
            feedback.text = 'Brawo! Naciśnięty został klawisz W! Naciśnij ENTER aby przejść dalej'
            break

        sentence.draw()
        window.flip()

    while True:
        if event.getKeys(['return']):
            break
        feedback.draw()
        window.flip()


# PRZYKŁAD 2. Odpowiedzi za pomocą myszy.
###########################################

# Nasze bodźce to dwa prostokąty
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

# Tworzymy obiekt `Mouse`, który pozwoli nam monitorować myszkę.
mouse = event.Mouse()

while True:
# Mouse.getPost() zwraca tuple z koordynatami X oraz Y myszy
# Obiekty klasy `Rect` posiadają metodę `contains`, która pozwala sprawdzić, czy dane koordynaty znajdują się w obrębie figury
    if rect_red.contains(mouse.getPos()):
# getPressed zwraca listę trzech wartości (0 - nienaciśnięty, 1 - naciśnięty) oznaczającą czy klawisze myszy są naciśnięte. Nas interesuje lewy przycisk myszy.
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


# PRZYKŁAD 3. Suwak
###################

info = visual.TextStim(window,
                       text = '')

# Obiekty klasy RatingScale przyjmują bardzo dużo argumentów. Tutaj są tylko przykładowe, w dokumentacji jest znacznie więcej.
# Aby zobaczyć co każdy z nich robi warto uruchomić skrypt.

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


