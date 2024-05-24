from PyQt5 import *
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

pass_key = "auavzkcycnhdmjmk"

# import MySQLdb

from PyQt5.uic import loadUiType

ui, _ = loadUiType("./UI/bookdetail.ui")

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.addtochart.clicked.connect(self.gotochart)


    def gotochart(self):
        print('')

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()





if __name__ == '__main__':
    main()