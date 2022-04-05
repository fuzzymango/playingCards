class Deck:
    def __init__(self):
        self.deck = []
        self.suits = ["hearts",
                      "diamonds",
                      "spades",
                      "clubs"]
        self.cards = ["ace",
                      "one",
                      "two",
                      "three",
                      "four",
                      "five",
                      "six",
                      "seven",
                      "eight",
                      "nine",
                      "ten",
                      "jack",
                      "queen",
                      "king"]
        for suit in self.suits:
            for card in self.cards:
                self.deck.add("%s of %s" % suit, card)

    def getDeck(self):
        return self.deck
