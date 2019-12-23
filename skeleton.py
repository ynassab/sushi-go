
## currently, play a simple game of sushi go with yourself in the terminal with
## tempura, nigiri, dumplings, sashimi (easiest points to count)

import random

print('hello world!')

deck = []  # list of card objects * count


class CardType:
    def __init__(self, name, points, count, id):
        self.name = name
        self.points = points
        self.count = count
        self.id = id
        self.depleted = False
        for _ in range(count):
            deck.append(self)


class DraftHand:
    def __init__(self, id, size):  # change size of the draft hand based on # of players

        self.id = id
        self.cards = []
        self.cards_repr = []

        for _ in range(size):
            draw_index = random.randint(0, len(deck)-1)  # choose a card randomly
            drawn_card = deck.pop(draw_index)  # remove it from the deck
            self.append(drawn_card)  # add it to the draft hand
            if len(deck) == 0:
                print('deck depleted!')
                break

    def append(self, new_card):
        self.cards.append(new_card)
        self.cards_repr.append(new_card.name + ' (id=%d)' % new_card.id)

    def remove(self, old_card):
        self.cards.remove(old_card)
        self.cards_repr.remove(old_card.name + ' (id=%d)' % old_card.id)

    def show(self):
        print('Draft Hand ', self.id, ':', sep='')
        print(self.cards_repr)


class Board:
    def __init__(self):
        self.cards = []
        self.cards_repr = []
        self.new_card = None
        pass

    def append(self, new_card):  # add card face down; keep track of it
        self.new_card = new_card
        self.cards.append(new_card)
        self.cards_repr.append('?')
        pass

    def show(self):  # shows cards
        print('Board: ')
        print(self.cards_repr)
        pass

    def flip(self):  # flip face-down card
        self.cards_repr.remove('?')
        self.cards_repr.append(self.new_card.name + ' (id=%d)' % self.new_card.id)
        pass



egg_nigiri      = CardType(name='egg nigiri', points=1, count=0, id=0)
salmon_nigiri   = CardType(name='salmon nigiri', points=2, count=0, id=1)
squid_nigiri    = CardType(name='squid nigiri', points=3, count=0, id=2)
dumpling        = CardType(name='dumpling', points=None, count=0, id=3)
tempura         = CardType(name='tempura', points=None, count=5, id=4)
sashimi         = CardType(name='sashimi', points=None, count=7, id=5)


drafthand1 = DraftHand(id=1, size=11)
# drafthand2 = DraftHand(id=2, size=11)
# drafthand3 = DraftHand(id=3, size=11)

player1board = Board()


def choose():  # someone clicking on the card to place it in front of them

    while True:
        chosen_id = input('choose a card: ')  # int
        try:
            chosen_id = int(chosen_id)
            break
        except:
            print('choose a valid value!')

    found_card = False
    for card in drafthand1.cards:
        if card.id == chosen_id:
            chosen_card = card  # if more than one card with the same id, chooses only one (overwrites others)
            found_card = True
    if not found_card:
        print('choose a valid value!')
        return choose()
    else:
        drafthand1.remove(chosen_card)
        player1board.append(chosen_card)
        return chosen_card


