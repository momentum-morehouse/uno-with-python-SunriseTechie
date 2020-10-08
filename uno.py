from random import randint

NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵"]


class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color

    def ___str___(self):
        return f"{self.color} {self.number}"   


class Player:
    def __init__(self, name):
        self.name = name 


class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = (color, number)
                self.cards.append(card)

    def shuffle(self):
        shuffled_deck = []
        deck_to_shuffle = self.cards.copy()
        while len(deck_to_shuffle) > 0:
            card_to_move = deck_to_shuffle[randint(0, len(deck_to_shuffle)-1)]
            deck_to_shuffle.remove(card_to_move)
            shuffled_deck.append(card_to_move)
        return shuffled_deck

deck = Deck(NUMBERS, COLORS)
shuffled = deck.shuffle()
for card in shuffled:
    print(card)    


class Game:
    pass