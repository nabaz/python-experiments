import itertools, random

def shuffelDeck(draw):

    deck = list(itertools.product(range(1,14), ['spade','heart','diamond', 'club']))
    random.shuffle(deck)
    for i in range(draw):
        print(deck[i][0], "of ", deck[i][1])




shuffelDeck(5)
