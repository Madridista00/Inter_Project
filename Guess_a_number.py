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
        try:
            guess = input(f"Mcdeloba {i+1}, chapiqrebuli ricxvia? ")
            if not guess.isdigit():
                print("Gtxovt sheiyvanot mteli dadebiti ricxvi!\n")
                continue
            guess = int(guess)
            i += 1
        except KeyboardInterrupt:
            print("\nExiting the game.")
            break

        if guess < 1 or guess > 100:
            print("Tqveni sheyvanili ricxvi unda iyos 1-dan 100-mde diapazonshi\n")
            i -= 1
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