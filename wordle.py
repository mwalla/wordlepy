
#from ast import For
import pandas as pd

#import the possible answers and possible guesses
answers = pd.read_csv("wordle_answers.txt", names = ["word"])
guesses = pd.read_csv("wordle_guesses.txt", names = ["word"])

answers['position_1'] = answers.word.str[0]
answers['position_2'] = answers.word.str[1]
answers['position_3'] = answers.word.str[2]
answers['position_4'] = answers.word.str[3]
answers['position_5'] = answers.word.str[4]
answers['count_pos_1'] = answers.groupby('position_1')['position_1'].transform('count')
answers['count_pos_2'] = answers.groupby('position_2')['position_2'].transform('count')
answers['count_pos_3'] = answers.groupby('position_3')['position_3'].transform('count')
answers['count_pos_4'] = answers.groupby('position_4')['position_4'].transform('count')
answers['count_pos_5'] = answers.groupby('position_5')['position_5'].transform('count')
answers['score'] = answers['count_pos_1'] + answers['count_pos_2'] + answers['count_pos_3'] + answers['count_pos_4'] + answers['count_pos_5']

#sort the answers by score
answers_ranked = answers.sort_values(by='score',ascending = False)

#initialise turn and word list
answers = answers_ranked['word'].to_list()
guesses = guesses['word'].to_list()
turn = 0


#function to get guess
def get_guess(prompt = "Enter your 5 letter guess:\n"):
    """Function to retrieve valid word guess from user"""
    while True:
        guess = input(prompt)
        if guess not in answers and guess not in guesses:
            print(f'"{guess}" is not a valid guess, please try again...\n')
        else:
            return(guess)

#function to get result
def get_results(prompt = "Enter your 5 letter results (g for green, y for yellow, b for black/grey. e.g. 'bbyyg'):\n"):
    """Function to retrieve valid results from user"""
    acceptable = ['b', 'g', 'y']
    while True:
        results = input(prompt)
        if len(results) != 5 or any([letter not in acceptable for letter in results]):
            print(f' "{results}" is not a valid result, please try again...\n')
        else:
            return(results)


print("wordlepy: A wordle helper")
while len(answers) > 1:
    turn += 1
    print("turn number:", turn)
    print("maybe you should guess: ", answers[0])
    guess = get_guess()
    results = get_results()

    for i in range(5):
        if results[i] == "g":
            #filter answers list for answers containing the green letter in the guessed position
            answers = [x for x in answers if x[i] == guess[i] and guess[i] in x]
        elif results[i] == "y":
            #filter answers to exclude answers where yellow letter in guessed position
            answers = [x for x in answers if x[i] != guess[i] and guess[i] in x]
        elif results[i] == "b":
            answers = [x for x in answers if guess[i] not in x]
    print("there are ", len(answers), " possible answers remaining:")
    print(answers)


