import time
import sys

from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QDialog, QVBoxLayout, QGridLayout, QStackedWidget
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication
import sys

from Converter import *


class App(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Converter')
        self.setStyleSheet("background-color:grey")

        self.initUI()

    def initUI(self):
        self.setFixedSize(1280, 720)
        self.mainWindow()
        self.mergePNG_option()

        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(self.mainWindow)
        self.stackedWidget.addWidget(self.mergePNG)

        vbox = QVBoxLayout()
        vbox.addWidget(self.stackedWidget)
        self.setLayout(vbox)

        self.show()

    def mainWindow(self):
        self.mainWindow = QWidget()
        self.mainWindow.setStyleSheet("background-color:rgb(93,93,93)")

        self.label = QLabel(self)
        self.pixmap = QPixmap('../resources/Title.png')
        self.label.setPixmap(self.pixmap)
        self.label.setMaximumSize(319, 120)
        self.label.setStyleSheet("padding-top: 20px")

        layout = QGridLayout()

        # Buttons
        button_docx = QPushButton()
        button_docx.setStyleSheet(
            "background-image : url('../resources/docx.png');background-color:transparent;")
        button_docx.setFixedSize(319, 217)
        button_docx.setFlat(True)
        button_docx.clicked.connect(pdf_to_docx)
        button_jpg = QPushButton()
        button_jpg.setStyleSheet("background-image : url('../resources/JPG.png');background-color:transparent;")
        button_jpg.setFixedSize(319, 217)
        button_jpg.setFlat(True)
        button_jpg.clicked.connect(convert_images_to_jpg)
        button_png = QPushButton()
        button_png.setStyleSheet("background-image : url(../resources/PNG.png);background-color:transparent")
        button_png.setFixedSize(319, 217)
        button_png.setFlat(True)
        button_png.clicked.connect(convert_images_to_png)

        button_pdf = QPushButton()
        button_pdf.setFixedSize(319, 217)
        button_pdf.setStyleSheet(
            "background-image : url('../resources/PDF.png');background-color:transparent;")
        button_pdf.setFlat(True)
        button_pdf.clicked.connect(convert_images_to_pdf)
        button_mergePdf = QPushButton()
        button_mergePdf.setFixedSize(319, 217)
        button_mergePdf.setStyleSheet(
            "background-image : url('../resources/Merge PDF.png');background-color:transparent")
        button_mergePdf.setFlat(True)
        button_mergePdf.clicked.connect(merge_pdf)
        button_mergePng = QPushButton()
        button_mergePng.setStyleSheet(
            "background-image : url('../resources/Merge PNG.png');background-color:transparent")
        button_mergePng.setFixedSize(319, 217)
        button_mergePng.setFlat(True)
        button_mergePng.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))

        # Add buttons to Grid
        layout.addWidget(self.label, 0, 1, 1, 1)

        layout.addWidget(button_docx, 1, 0, 2, 1)
        layout.addWidget(button_jpg, 1, 1, 2, 1)
        layout.addWidget(button_png, 1, 2, 2, 1)

        layout.addWidget(button_pdf, 3, 0, 2, 1)
        layout.addWidget(button_mergePdf, 3, 1, 2, 1)
        layout.addWidget(button_mergePng, 3, 2, 2, 1)

        self.mainWindow.setLayout(layout)

    def mergePNG_option(self):
        self.mergePNG = QWidget()
        self.mergePNG.setStyleSheet("background-color:rgb(93,93,93)")

        # Title
        self.label = QLabel(self)
        self.pixmap = QPixmap('../resources/Title.png')
        self.label.setPixmap(self.pixmap)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setMaximumSize(1280, 120)
        self.label.setStyleSheet("padding-top: 20px")

        layout = QGridLayout()
        layout.addWidget(self.label, 0, 0, 1, 2)

        # Buttons
        button_vertical = QPushButton()
        button_vertical.setStyleSheet("background-image : url('../resources/Horizontal.png');background-color:transparent")
        button_vertical.setFixedSize(319, 217)
        button_vertical.setFlat(True)
        button_vertical.clicked.connect(vertical)
        button_horizontal = QPushButton()
        button_horizontal.setStyleSheet("background-image : url('../resources/Vertical.png');background-color:transparent")
        button_horizontal.setFlat(True)
        button_horizontal.setFixedSize(319, 217)
        button_horizontal.clicked.connect(horizontal)
        back = QPushButton(text='Back')
        back.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        back.setStyleSheet("background-color:grey")

        # Add buttons to grid
        layout.addWidget(button_vertical, 0, 0, 2, 1)
        layout.addWidget(button_horizontal, 0, 1, 2, 1)
        layout.addWidget(back, 2, 0, 1, 2)

        self.mergePNG.setLayout(layout)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()
