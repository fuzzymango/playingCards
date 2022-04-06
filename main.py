import deck as d
import player
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self, deck, player):
        super().__init__()
        self.deck = deck
        self.player = player

        self.setWindowTitle("card dealer program")
        layout = QGridLayout()
        widgets = []

        self.player1_hand_label = QLabel("Player 1 Hand")
        layout.addWidget(self.player1_hand_label, 0, 0)

        self.player1_hand = self.player.get_hand()
        layout.addWidget(self.player1_hand, 1, 0)

        self.discard_pile_label = QLabel("Discard Pile")
        layout.addWidget(self.discard_pile_label, 0, 1)

        self.discard_pile = deck.get_discard_pile()
        layout.addWidget(self.discard_pile, 1, 1)

        self.shuffle = QPushButton("shuffle")
        self.shuffle.clicked.connect(self.shuffle_pressed)
        layout.addWidget(self.shuffle, 2, 1)

        self.draw_card = QPushButton("draw card")
        self.draw_card.clicked.connect(self.draw_card_pressed)
        layout.addWidget(self.draw_card, 2, 0)

        self.play_card = QPushButton("play card")
        self.play_card.clicked.connect(self.play_card_pressed)
        layout.addWidget(self.play_card, 3, 0)

        self.reset = QPushButton("reset")
        self.reset.clicked.connect(self.reset_clicked)
        layout.addWidget(self.reset, 4, 1)

        for w in widgets:
            layout.addWidget(w())
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def shuffle_pressed(self):
        self.deck.shuffle()

    def draw_card_pressed(self):
        if not self.deck.get_deck():
            print("no cards left in deck")
            return
        card = self.deck.deal_top_card()
        self.player1_hand.insertItem(0, card)

    def play_card_pressed(self):
        card_index = self.player1_hand.currentRow()
        card = self.player1_hand.currentItem()
        self.discard_pile.insertItem(0, card.text())
        self.player1_hand.takeItem(card_index)

    def reset_clicked(self):
        self.deck.reset()
        self.player.clear_hand()


def main():
    app = QApplication([])

    deck = d.Deck()
    player1 = player.Player("Michael")

    window = MainWindow(deck, player1)
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
