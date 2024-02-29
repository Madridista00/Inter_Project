"""
2.3 თამაში 2: Hangman
Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი
ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს ფარულ ასოებს. მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში.
ვლინდება სწორად გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან არ ამოიწურება მცდელობები.

"""

import random

def making_a_guess():
    global update_display
    global guess
    if guess.lower() == chosen_word_lowercase:
        print("YOU WIN!")
        return True
    correct_guess = False
    for x in range(len(chosen_word)):
        if guess.lower() == chosen_word[x]:
            blank_list[x] = guess.lower()
            correct_guess = True

    if not correct_guess:
        print(f"There is no {guess}, sorry.")
        update_display += 1
    return False

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
 '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''',
  '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

word_dict = {
    "advertisement": "A notice or announcement in a public medium promoting a product, service, or event.",
    "ball": "A solid or hollow spherical or egg-shaped object that is kicked, thrown, or hit in a game.",
    "train": "A connected series of railroad cars pulled or pushed by one or more locomotives.",
    "car": "A road vehicle, typically with four wheels, powered by an internal combustion engine.",
    "yellow": "Of the color between green and orange in the spectrum, a primary subtractive color complementary to blue.",
    "beautiful": "Pleasing the senses or mind aesthetically.",
    "mountain": "A large natural elevation of the earth's surface rising abruptly from the surrounding level; a large steep hill.",
    "cloud": "A visible mass of condensed water vapor floating in the atmosphere, typically high above the ground."
}

chosen_word = random.choice(list(word_dict.keys()))
chosen_word_lowercase = chosen_word.lower()

blank_list = ["_" for _ in chosen_word]

update_display = 0

print(HANGMANPICS[update_display])
print(f"Definition: {word_dict[chosen_word]}")
guess = input(f"\nWelcome to Hangman.\n{' '.join(blank_list)}\nMake a guess?\nYou have six tries! - ")
if making_a_guess():
    print("The word has been guessed correctly!")
    exit()

print(HANGMANPICS[update_display])
print(' '.join(blank_list))

while update_display < 6:
    if ''.join(blank_list) == chosen_word:
        print("YOU WIN!")
        break
    guess = input("Make another guess? ")
    if making_a_guess():
        print("The word has been guessed correctly!")
        break
    print(HANGMANPICS[update_display])
    print(' '.join(blank_list))
if update_display == 6:
    print("GAME OVER.")