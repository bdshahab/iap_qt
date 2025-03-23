# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'boughtzVGHaO.ui'
##
# Created by: Qt User Interface Compiler version 6.8.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)
import Global
import Main_Menu as the_main
from tools.for_images import show_image
from tools.Centralization import center_window


class Ui_Bought(QDialog):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"background-color: rgb(163, 0, 255);\n"
                           "color: rgb(255, 255, 255);\n"
                           "font: 18pt \"Segoe UI\";")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.vbox = QVBoxLayout()
        self.vbox.setObjectName(u"vbox")
        self.l1 = QLabel(self)
        self.l1.setObjectName(u"l1")
        self.l1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.l1)

        self.l2 = QLabel(self)
        self.l2.setObjectName(u"l2")
        self.l2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.l2)

        self.l3 = QLabel(self)
        self.l3.setObjectName(u"l3")
        self.l3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vbox.addWidget(self.l3)

        self.verticalLayout.addLayout(self.vbox)

        self.ok = QPushButton(self)
        self.ok.setObjectName(u"ok")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.ok)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        self.setWindowTitle("Bought")
        from tools.Centralization import center_window
        center_window(self)

        self.l1.setText(QCoreApplication.translate(
            "Dialog", u"Congratulations!", None))
        self.l2.setText(QCoreApplication.translate(
            "Dialog", u"Your purchase was successful.", None))
        self.l3.setText(QCoreApplication.translate(
            "Dialog", u"Now you can use all the features of this program.", None))
        self.ok.setText("")
    # retranslateUi
        self.events()
        self.set_images()
        self.set_CSS_style()

    def set_CSS_style(self):
        self.setStyleSheet("""
                    QMainWindow{
                            background-color: #f1ff00;
                    }
                    QPushButton {
                        background-color: #808080;
                        color: white;
                        font-size: 20px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #b3b3b3;
                        color: black;
                    }
                """
                           )

    def events(self):
        self.resize(800, 600)
        center_window(self)
        self.ok.clicked.connect(self.close_window)

    def set_images(self):
        show_image([self.ok],
                   [r"Payment\Photos\buy.png"],
                   [(Global.img_size*5, Global.img_size*5)])

    def close_window(self):
        Global.user_bought = True
        self.close()
