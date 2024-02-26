"""
2.2 თამაში 1: გამოიცანით რიცხვი
ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან. მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი.
არასწორი რიცხვის შემთხვევაში პროგრამა მომხმარებელს აძლევს მინიშნებას (უფრო მაღალი/უფრო დაბალი). თამაში აკონტროლებს
მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს

"""

from random import randint

try:
    number = randint(1, 100)
    i = 0

    print("\nChavifiqre ricxvi 1-dan 100-mde diapazonshi, gtxov gamoicani is:\n")

    while True:
        i += 1
        try:
            guess = int(input(f"Mcdeloba {i}, chapiqrebuli ricxvia? "))
        except ValueError:
            print("Gtxovt sheiyvanot mteli dadebiti ricxvi!\n")
            continue

        if guess < 1 or guess > 100:
            print("Tqveni sheyvanili ricxvi unda iyos 0-dan 100-mde diapazonshi\n")
            continue

        if guess == number:
            print(f"Gilocavt, tqven gamoicanit chapiqrebuli ricxvi. Es ricxvia {number}!")
            break
        elif guess > number:
            print("Tqveni ricxvi chapikrebul ricxvze magalia.")
        else:
            print("Tqveni ricxvi chapikrebul ricxvze dabalia.")
        print()
    print("\nGame over!")
except KeyboardInterrupt:
    print("\nExiting the game.")