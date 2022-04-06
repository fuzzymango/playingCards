import random
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Deck:
    def __init__(self):
        self.deck = []
        self.discard_pile = QListWidget()
        self.suits = ["hearts",
                      "diamonds",
                      "spades",
                      "clubs"]
        self.cards = ["A",
                      "2",
                      "3",
                      "4",
                      "5",
                      "6",
                      "7",
                      "8",
                      "9",
                      "10",
                      "J",
                      "Q",
                      "K"]
        self.reset()

    def get_deck(self):
        return self.deck

    def get_discard_pile(self):
        return self.discard_pile

    def shuffle(self):
        random.shuffle(self.deck)

    def reset(self):
        self.deck.clear()
        self.discard_pile.clear()
        for suit in self.suits:
            for card in self.cards:
                card = QListWidgetItem("{} of {}".format(card, suit))
                self.deck.append(card)

    def deal_top_card(self):
        card_to_deal = self.deck[0]
        self.deck.remove(self.deck[0])
        return card_to_deal
