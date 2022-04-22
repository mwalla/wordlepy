import json

with open('bfba912f.js') as dataFile:
    data = dataFile.read()
    answers = data[data.find('Ma=')+3 : data.rfind('Oa=')-1]
    guesses = data[data.find('Oa=')+3 : data.rfind('Ra=')-1]
    answers = json.loads(answers)
    guesses = json.loads(guesses)

len(answers)
len(guesses)