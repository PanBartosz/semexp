from psychopy import visual, core, event, data, gui
from pathlib import Path # aktualny sposób radzenia sobie ze ścieżkami


# Wyświetlamy okienko do wpisywania danych badanego
expName = 'Eksperyment testowy'
expInfo = {'uczestnik': '',
           'sesja': '001',
           'płeć (M/F)': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # jeżeli klikniemy na anuluj, to PsychoPy zakończy działanie

# Dodajemy do danych eksperymentu nazwę eksperymentu oraz datę
expInfo['date'] = data.getDateStr()
expInfo['expName'] = expName
# Konstruujemy ściężkę, w której będą się zapisywać rezultaty badania
filename = Path().absolute() /  'data/{p}_{e}_{d}'.format(p = expInfo['uczestnik'], e = expName, d = expInfo['date'])
filename = str(filename)

# Obiekt, który będzie pomagał nam w zapisywaniu danych z eksperymentu
exp = data.ExperimentHandler(name = 'Eksperyment testowy',
                             extraInfo = expInfo,
                             dataFileName = filename)


# Warunki eksperymentalne można importować z plików Excela lub zwykłych CSV
conditions = data.importConditions('conditions.xlsx')

# Tworzymy obiekt, który będzie przechowywał nasze próby
trials = data.TrialHandler(conditions, # lista ze słownikami dla każdego warunku
                           nReps = 3, # liczba powtórzeń listy warunków
                           method = 'random') # metoda randomizacji

exp.addLoop(trials) # informujemy nasz obiekt `exp` o istnieniu obiektu `trials``


window = visual.Window(fullscr=True,
                    size = (1920,1080),
                    monitor='Default',
                    units='norm')

# Tworzymy bodźce
sentence = visual.TextStim(window,
                           text = '')

instruction = visual.TextStim(window,
                              text = 'Wciśnij Q, jeśli zdanie Ci się podoba lub W, jeśli Ci się nie podoba',
                              pos = [-0.3, -0.5],
                              height = 0.04)

for thisTrial in trials: # obiekt trials jest Pythonowskim iteratorem
    clock = core.Clock()
    sentence.text = thisTrial['sentence'] # modyfikujemy atrybuty naszego bodźca
    sentence.ori = thisTrial['rotation']
    while True:
        keys = event.getKeys()
        if 'q' in keys or 'w' in keys:
            rt = clock.getTime() # składujemy w zmiennej czas reakcji badanego
            # zapisujemy, której odpowiedzi udzielił badany
            if 'q' in keys:
                resp = 'podoba'
            elif 'w' in keys:
                resp = 'nie podoba'

            exp.addData('response.resp', resp) # zapisujemy odpowiedź na bodziec naszego badanego
            exp.addData('response.rt', rt) # oraz szybkość odpowiedzi
            exp.nextEntry() # informujemy obiekt zajmujący się zapisywaniem danych, że jesteśmy w kolejnej próbie
            break

        sentence.draw()
        instruction.draw()
        window.flip()


