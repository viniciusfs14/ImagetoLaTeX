# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrICAup.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: white;\n"
"\n"
"QLineEdit:{\n"
"	background-color: rgb(0, 79, 0);\n"
"	border-top: 2px solid rgb(127, 167, 127);\n"
"	border-left: 2px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 2px solid rgb(0, 0, 0);\n"
"	border-right: 2px solid rgb(0, 0, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	background-color: rgb(0, 79, 0);\n"
"\n"
"	border-top: 1.5px solid rgb(127, 167, 127);\n"
"	border-left: 1.5px solid rgb(127, 167, 127);\n"
"\n"
"	border-bottom: 1.5px solid rgb(0, 0, 0);\n"
"	border-right: 1.5px solid rgb(0, 0, 0);\n"
"\n"
"	\n"
"	font: 12pt \"Helvetica\";\n"
"	text-align:center;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.baixo = QWidget(self.widget)
        self.baixo.setObjectName(u"baixo")
        self.horizontalLayout_3 = QHBoxLayout(self.baixo)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.baixo)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.linha2 = QLineEdit(self.baixo)
        self.linha2.setObjectName(u"linha2")

        self.horizontalLayout_3.addWidget(self.linha2)

        self.convert = QPushButton(self.baixo)
        self.convert.setObjectName(u"convert")
        self.convert.setStyleSheet(u"background-color: red;\n"
"color: white ")

        self.horizontalLayout_3.addWidget(self.convert)


        self.gridLayout_2.addWidget(self.baixo, 3, 0, 1, 1)

        self.header = QWidget(self.widget)
        self.header.setObjectName(u"header")
        self.header.setStyleSheet(u"color: red;")
        self.verticalLayout = QVBoxLayout(self.header)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.header)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(35)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_3 = QLabel(self.header)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(23)
        self.label_3.setFont(font2)

        self.verticalLayout.addWidget(self.label_3, 0, Qt.AlignHCenter)


        self.gridLayout_2.addWidget(self.header, 1, 0, 1, 1)

        self.equation = QWidget(self.widget)
        self.layout_equation = QVBoxLayout()
        self.equation.setLayout(self.layout_equation)
        self.equation.setObjectName(u"equation")

        self.gridLayout_2.addWidget(self.equation, 4, 0, 1, 1)

        self.bottom = QWidget(self.widget)
        self.bottom.setObjectName(u"bottom")
        self.horizontalLayout = QHBoxLayout(self.bottom)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.path = QLabel(self.bottom)
        self.path.setObjectName(u"path")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(False)
        self.path.setFont(font3)

        self.horizontalLayout.addWidget(self.path, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.linha = QLineEdit(self.bottom)
        self.linha.setObjectName(u"linha")

        self.horizontalLayout.addWidget(self.linha)

        self.pushButton = QPushButton(self.bottom)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background-color: red;\n"
"color: white ")

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.gridLayout_2.addWidget(self.bottom, 2, 0, 1, 1)

        self.info = QWidget(self.widget)
        self.info.setObjectName(u"info")
        self.verticalLayout_2 = QVBoxLayout(self.info)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.info)
        self.label_4.setObjectName(u"label_4")
        font4 = QFont()
        font4.setBold(False)
        font4.setItalic(True)
        self.label_4.setFont(font4)

        self.verticalLayout_2.addWidget(self.label_4, 0, Qt.AlignBottom)


        self.gridLayout_2.addWidget(self.info, 5, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Equa\u00e7\u00e3o: ", None))
        self.convert.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ImgToLaTeX", None))
        self.label_3.setText("")
        self.path.setText(QCoreApplication.translate("MainWindow", u"Caminho:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u00a9 ImgToLaTeX - Vin\u00edcius Fernandes Silvestre - 2024", None))
    # retranslateUi

