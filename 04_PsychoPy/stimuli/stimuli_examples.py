# Importujemy z PsychoPy moduły niezbędne do pokazania różnych rodzajów bodźców
from psychopy import visual, core, event, data, sound

# `Window` jest podstawowym obiektem w PsychoPy, który reprezentuje okno w eksperymencie.
# Zawsze tworząc bodźce musimy powiedzieć, w którym oknie mają być rysowane/odtwarzane.
window = visual.Window(fullscr=True, # eksperyment wyświetlany jest na pełnym ekranie
                       size = (1920,1080), # rozdzielczość ekranu używana w eksperymencie
                       monitor='Default', # nazwa monitora (kiedy mamy np. skalibrowany monitor)
                       units='norm') # jednostki używane w eksperymencie, `norm` = standardowy układ współrzędnych

# Prosty bodzieć tekstowy
simple_text_stim = visual.TextStim(window, # zawsze podajemy obiekt `Window`, w którym chcemy wyświetlić bodziec!
                                   text = 'To jest bardzo prosty bodzieć tekstowy')

clock = core.Clock() # tworzymy zegar, który będzie tworzył czas (domyślnie - od stworzenia obiektu)

while clock.getTime() < 5: # metoda `get.Time()` zegara zwraca czas w sekundach, tutaj wyświetlamy przez 5 sekund
    simple_text_stim.draw() # przed każdym odświeżeniem ekranu musimy narysować wszystkie bodźce
    window.flip() # aktualizuje bufor graficzny i czeka na odświeżenie ekranu

# Bardziej zaawansowany bodziec tekstowy
customized_text_stim = visual.TextStim(window,
                                       text = '',
                                       color = 'red', # kolor możemy podać jako nazwę lub listę 3 wartości np. [1,0,0]
                                       pos = [0.1, 0.3], # pozycja na ekranie
                                       italic = True, # jedna z wielu opcji formatowania tekstu
                                       ori = 30, # obrót podany w stopniach
                                       height = 0.1) # wysokość linii tekstu


STIMULI_LIST = ['Pierwszy bodziec', 'Drugi bodziec', 'Trzeci bodziec'] # będziemy aktualizować tekst

for stimuli in STIMULI_LIST:
    clock = core.Clock()
    customized_text_stim.text = stimuli # możemy aktualizować atrybuty bodźców, tutaj zmieniamy teskt.
    while clock.getTime() < 2:
        simple_text_stim.draw()
        customized_text_stim.draw()
        window.flip()

# Losowo rozmieszczone prostokąty. Najpierw tworzymy listę z 10 prostokątami.
rectangles = []
for i in range(10):
    rectangles.append(
        visual.Rect(window,
                    width = 0.2,
                    height = 0.2) # ze względu na użyty układ współrzędnych wyjdą nam prostokąty!
    )

# Przy każdej z 5 iteracji zmieniamy kolory naszych prostokątów oraz ich pozycję na ekranie
from random import random, uniform
for i in range(5):
    for rect in rectangles:
        rect.pos = [uniform(-1, 1), uniform(-1, 1)]
        rect.fillColor = [random(), random(), random()]

    clock = core.Clock()
    while clock.getTime() < 2:
        for rect in rectangles:
            rect.draw()
        window.flip()

# Prosty bodziec z pliku graficznego
image_stim = visual.ImageStim(window,
                              image = 'doki.jpg',
                              units = 'height') # dla każdego bodźca możemy ustawić inne jednostki
clock = core.Clock()
while clock.getTime() < 5:
    image_stim.ori = clock.getTime() * 100 % 360 # atrybut `ori` zmienia się co każdą klatkę, cel: płynny obrót
    image_stim.draw()
    window.flip()

sound_stim = sound.Sound('poker-chips-daniel_simon.wav')
window.flip()
sound_stim.play()
dur = sound_stim.getDuration() # `getDuration()` zwraca długość dźwięku w sekundach
core.wait(dur) # `wait()` czeka określoną liczbę sekund`
