import sys

# importing PyQt5 modules

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap
import random


# guessing game class inherits QWidget
class GuessingGame(QWidget):
    EXIT = -5

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setGeometry(850, 250, 500, 300)
        self.setWindowTitle("Guessing Game")
        self.rand = random.randint(0, 10)
        self.show()

        # LABELS
        self.Guesses = QLabel("Guesses:")
        self.Guesses.setFont(QFont("Ariel", 20))

        guess1 = QLabel("Guess 1: ")
        guess2 = QLabel("Guess 2: ")
        guess3 = QLabel("Guess 3: ")
        big = QLabel("To big")
        small = QLabel("To small")
        correct = QLabel("correct!")

        self.n = 0
        self.answer1 = QLabel("")
        self.output1 = QLabel("")

        self.answer2 = QLabel("")
        self.output2 = QLabel("")

        self.answer3 = QLabel("")
        self.output3 = QLabel("")

        # EDIT
        self.edit = QLineEdit()
        self.something = self.edit.displayText()

        # self.nameLabel = QLabel(self)
        # self.nameLabel.setText('Name:')
        # self.line = QLineEdit(self)

        # Button
        button_guess = QPushButton("Guess")
        button_guess.clicked.connect(self.buttonzz)

        # LABEL
        interface = QLabel("Interface:")
        interface.setFont(QFont("Ariel", 20))
        picture = QLabel("Picture:")
        colour = QLabel("Colour:")

        # Combo Box
        self.combo1 = QComboBox()
        self.combo1.addItem("pluto")
        self.combo1.addItem("mickey")
        self.pixmap = QPixmap("mickey.gif")
        self.pic_label = QLabel(self)
        self.combo2 = QComboBox()
        self.combo2.addItem("Red")
        self.combo2.addItem("Blue")

        # Push Button
        change = QPushButton("Change")
        change.clicked.connect(self.change_clicked)
        change.clicked.connect(self.picture)

        close = QPushButton("Close")
        close.clicked.connect(self.closing)

        new_game = QPushButton("New Game")
        new_game.clicked.connect(self.reboot)

        #adding to a grid
        grid = QGridLayout()
        grid.addWidget(self.Guesses, 0, 3)
        grid.addWidget(guess1, 1, 3)
        grid.addWidget(guess2, 2, 3)
        grid.addWidget(guess3, 3, 3)
        grid.addWidget(self.edit, 4, 4)

        grid.addWidget(self.answer1, 1, 4)
        grid.addWidget(self.output1, 1, 5)

        grid.addWidget(self.answer2, 2, 4)
        grid.addWidget(self.output2, 2, 5)

        grid.addWidget(self.answer3, 3, 4)
        grid.addWidget(self.output3, 3, 5)

        grid.addWidget(button_guess, 4, 5)

        grid.addWidget(interface, 5, 3)
        grid.addWidget(picture, 6, 3)
        grid.addWidget(self.combo1, 6, 4)
        grid.addWidget(colour, 7, 3)
        grid.addWidget(self.combo2, 7, 4)
        grid.addWidget(change, 7, 5)

        grid.addWidget(close, 8, 3)
        grid.addWidget(new_game, 8, 4)

        pixmap = QPixmap("mickey.gif")
        self.pic_label = QLabel()
        self.pic_label.setPixmap(pixmap)
        grid.addWidget(self.pic_label, 0, 1, 8, 1)

        self.setLayout(grid)

    def picture(self):
        self.new_pic = self.combo1.currentText()
        self.new_pic = QPixmap(self.new_pic + ".gif")
        self.pic_label.setPixmap(self.new_pic)

    def change_clicked(self):

        self.setPalette(QPalette(QColor(self.combo2.currentText())))
        self.setAutoFillBackground(True)

    def colour(self):

        pic_label = self.QLabel()
        pic_label.setPixmap(self.pixmap)
        # grid.addWidget(pic_label, 0, 1, 8, 1)

    # def Button(self):
    #
    #     num = self.edit.displayText()
    #     self.edit.clear()
    #     if int(num) < self.rand:
    #         self.answer1.setText("To small")
    #     if int(num) > self.rand:
    #         self.answer2.setText("To big")
    #     if int(num) == self.rand:
    #         self.answer3.setText("correct!")

    def buttonzz(self):

        self.n += 1
        if self.n == 1:
            self.something = self.edit.displayText()
            self.answer1.setText(self.something)
            if self.rand == int(self.something):
                self.output1.setText('Correct')
            elif self.rand > int(self.something):
                self.output1.setText('Too small')
            else:
                self.output1.setText('Too big')

        if self.n == 2:
            self.something = self.edit.displayText()
            self.answer2.setText(self.something)
            if self.rand == int(self.something):
                self.output2.setText('Correct')
            elif self.rand > int(self.something):
                self.output2.setText('Too small')
            else:
                self.output2.setText('Too big')

        if self.n == 3:
            self.something = self.edit.displayText()
            self.answer3.setText(self.something)
            if self.rand == int(self.something):
                self.output3.setText('Correct')
            elif self.rand > int(self.something):
                self.output3.setText('Too small')
            else:
                self.output3.setText('Too big')
        self.edit.clear()

    #             def click(self):
    # self.guess = QtWidgets.QPushButton(self)
    # self.guess.clicked.connect(self.Button)

    def closing(self):
        sys.exit()

    def reboot(self):
        qApp.exit(GuessingGame.EXIT)

    # def newgame(self):
    #     self.answer1.setText('')
    #     self.output1.setText('')
    #
    #     self.answer2.setText('')
    #     self.output2.setText('')
    #
    #     self.answer3.setText('')
    #     self.output3.setText('')


def main():
    rebooting = GuessingGame.EXIT
    while rebooting == GuessingGame.EXIT:
        app = QApplication(sys.argv)
        guessing_Game = GuessingGame()
        # guessing_Game.show()
        # sys.exit(app.exec_())
        rebooting = app.exec_()
        app = None


main()
