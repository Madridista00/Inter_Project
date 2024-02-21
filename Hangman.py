"""
2.3 თამაში 2: Hangman
Hangman არის სიტყვების გამოცნობის თამაში. პროგრამა ირჩევს შემთხვევით სიტყვას წინასწარ განსაზღვრული სიიდან და აჩვენებს მას ქვედა ტირეების გამოყენებით (რამდენი
ასოცაა სიტყვაში, იმდენი ქვედა ტირე), რომელიც წარმოადგენს ფარულ ასოებს. მომხმარებლებს სთხოვენ გამოიცნონ ასო და პროგრამა ამოწმებს არის თუ არა ასო სიტყვაში.
ვლინდება სწორად გამოცნობილი ასოები და თამაში გრძელდება მანამ, სანამ მომხმარებელი არ გამოიცნობს სიტყვას ან არ ამოიწურება მცდელობები.

"""

# import random

# def making_a_guess():
#     global update_display
#     correct_guess = False
#     for x in range(len(chosen_word)):
#         if guess.lower() == chosen_word[x]:
#             blank_list[x] = guess.lower()
#             correct_guess = True

#     if not correct_guess:
#         print(f"There is no {guess}, sorry.")
#         update_display += 1

# HANGMANPICS = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''',
#   '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''',
#   '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''',
#   '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''',
#  '''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#       |
#       |
# =========''',
#   '''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#  /    |
#       |
# =========''',
#   '''
#   +---+
#   |   |
#   O   |
#  /|\\  |
#  / \\  |
#       |
# =========''']

# word_list = ["advartisement", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]

# chosen_word = list(random.choice(word_list))

# blank_list = ["_" for _ in chosen_word]

# update_display = 0

# print(HANGMANPICS[update_display])
# guess = input(f"Welcome to Hangman.\n{' '.join(blank_list)}\nMake a guess?\nYou have six try! - ")
# making_a_guess()
# print(HANGMANPICS[update_display])
# print(' '.join(blank_list))

# while update_display < 6:
#     if blank_list == chosen_word:
#         print("YOU WIN!")
#         break
#     guess = input("Make another guess? ")
#     making_a_guess()
#     print(HANGMANPICS[update_display])
#     print(' '.join(blank_list))
# if update_display == 6:
#     print("GAME OVER.")
