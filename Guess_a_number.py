"""
2.2 თამაში 1: გამოიცანით რიცხვი
ამ თამაშში პროგრამა აგენერირებს შემთხვევით რიცხვს მითითებული დიაპაზონიდან. მომხმარებლებს სთხოვენ გამოიცნონ რიცხვი.
არასწორი რიცხვის შემთხვევაში პროგრამა მომხმარებელს აძლევს მინიშნებას (უფრო მაღალი/უფრო დაბალი). თამაში აკონტროლებს
მცდელობების რაოდენობას და აჩვენებს შედეგს, როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს

"""


from random import randint
nummber = randint(1, 100)
i = 0

print("Chavifiqre ricxvi 1-dan 100-mde diapazonshi, gtxov gamoicani is:\n")

while True:
    i += 1
    guess = int(input(f"Mcdeloba {i}, chapiqrebuli ricxvia? "))

    if guess == nummber:
        print(f"Gilocavt, tqven gamoicanit chapiqrebuli ricxvi. Es ricxvia {nummber}!")
        break
    elif guess > nummber:
        print("Tqveni ricxvi chapikrebul ricxvze magalia.")
    else:
        print("Tqveni ricxvi chapikrebul ricxvze dabalia.")
    print()
print("\nGame over!")
