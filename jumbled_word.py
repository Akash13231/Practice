from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import random
import sys
from PyQt5 import uic


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi("untitled123.ui", self)

        self.words = ['apple', 'mango', 'delhi', 'pune', 'chennai', 'engine', 'mobile', 'pen', 'hockey', 'monkey']
        self.new = ''

        self.start = self.findChild(QPushButton, 'Start')
        self.reset = self.findChild(QPushButton, 'Reset')
        self.check = self.findChild(QPushButton, 'Check')
        self.add_word = self.findChild(QPushButton, 'add_word')
        self.line1 = self.findChild(QLineEdit, 'lineEdit1')
        self.line2 = self.findChild(QLineEdit, 'lineEdit2')
        self.line3 = self.findChild(QLineEdit, 'lineEdit3')

        self.start.clicked.connect(self.start_action)
        self.reset.clicked.connect(self.reset_action)
        self.check.clicked.connect(self.check_action)
        self.add_word.clicked.connect(self.add)

    def start_action(self):
        self.new = random.choice(self.words)
        word = list(self.new)
        random.shuffle(word)
        shuffled = ''.join(word)
        self.line1.setText(shuffled)
        self.line2.setText('')

    def reset_action(self):
        self.new = ''
        self.line1.setText('')
        self.line2.setText('')
        self.line3.setText('')
        self.line3.setStyleSheet('background:white')

    def add(self):
        new_word = self.line1.text()

        if new_word in self.words:
            self.line1.setText('word already exist')
        else:
            self.words.append(new_word)
        print(self.words)

    def check_action(self):
        self.uitext = self.line2.text()  # user input text

        if self.uitext == self.new:
            self.line3.setText("correct answer")
            self.line3.setStyleSheet('background:green')

        else:
            self.line3.setText('wrong answer')
            self.line3.setStyleSheet('background:red')


app = QApplication([])
window = UI()
window.show()
sys.exit(app.exec())