from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Player():
    def __init__(self, name="Player"):
        self.hand = QListWidget()
        self.name = name

    def get_hand(self):
        return self.hand

    def clear_hand(self):
        self.hand.clear()

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name
