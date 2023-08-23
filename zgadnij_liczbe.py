import random

lista = []
generate = random.randint(1,100)
game = True

trials = 0
while(game):
    ask = int(input("Zgadnij liczbe! Twój strzał: "))
    trials += 1
    lista.append(ask)
    if ask == generate:
        game = False
    elif ask > generate:
        print(f"Twoja liczba jest za wysoka! Spróbuj ponownie! Liczba twoich prób: {trials}")
    elif ask < generate:
        print(f"Twoja liczba jest za mała! Spróbuj ponownie! Liczba twoich prób: {trials}")

print(f"BRAWO! Zgadłeś za {trials} próbą!")
print(f"Lista kolejnych prób {lista}")
