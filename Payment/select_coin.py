# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'select_coinWgeuZj.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget, QMessageBox)
from tools.for_images import show_image
import Global
from tools.Centralization import center_window
from tools.iap_variables import TITLE_COIN_NOT_SELECTED, MESSAGE_COIN_NOT_SELECTED
from Payment.payment import MINIMUM_LIMIT_PRICE, Ui_Payment
from tools.dialogue import show_the_message


class Ui_Select_Coin(QDialog):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self)
        self.title.setObjectName(u"title")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.h1 = QHBoxLayout()
        self.h1.setObjectName(u"h1")
        self.b_1 = QPushButton(self)
        self.b_1.setObjectName(u"b_1")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_1.sizePolicy().hasHeightForWidth())
        self.b_1.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_1)

        self.b_2 = QPushButton(self)
        self.b_2.setObjectName(u"b_2")
        sizePolicy.setHeightForWidth(self.b_2.sizePolicy().hasHeightForWidth())
        self.b_2.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_2)

        self.b_3 = QPushButton(self)
        self.b_3.setObjectName(u"b_3")
        sizePolicy.setHeightForWidth(self.b_3.sizePolicy().hasHeightForWidth())
        self.b_3.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_3)

        self.b_4 = QPushButton(self)
        self.b_4.setObjectName(u"b_4")
        sizePolicy.setHeightForWidth(self.b_4.sizePolicy().hasHeightForWidth())
        self.b_4.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_4)

        self.verticalLayout.addLayout(self.h1)

        self.h2 = QHBoxLayout()
        self.h2.setObjectName(u"h2")
        self.b_5 = QPushButton(self)
        self.b_5.setObjectName(u"b_5")
        sizePolicy.setHeightForWidth(self.b_5.sizePolicy().hasHeightForWidth())
        self.b_5.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_5)

        self.b_6 = QPushButton(self)
        self.b_6.setObjectName(u"b_6")
        sizePolicy.setHeightForWidth(self.b_6.sizePolicy().hasHeightForWidth())
        self.b_6.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_6)

        self.b_7 = QPushButton(self)
        self.b_7.setObjectName(u"b_7")
        sizePolicy.setHeightForWidth(self.b_7.sizePolicy().hasHeightForWidth())
        self.b_7.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_7)

        self.b_8 = QPushButton(self)
        self.b_8.setObjectName(u"b_8")
        sizePolicy.setHeightForWidth(self.b_8.sizePolicy().hasHeightForWidth())
        self.b_8.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_8)

        self.verticalLayout.addLayout(self.h2)

        self.h3 = QHBoxLayout()
        self.h3.setObjectName(u"h3")
        self.b_9 = QPushButton(self)
        self.b_9.setObjectName(u"b_9")
        sizePolicy.setHeightForWidth(self.b_9.sizePolicy().hasHeightForWidth())
        self.b_9.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_9)

        self.b_10 = QPushButton(self)
        self.b_10.setObjectName(u"b_10")
        sizePolicy.setHeightForWidth(
            self.b_10.sizePolicy().hasHeightForWidth())
        self.b_10.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_10)

        self.b_11 = QPushButton(self)
        self.b_11.setObjectName(u"b_11")
        sizePolicy.setHeightForWidth(
            self.b_11.sizePolicy().hasHeightForWidth())
        self.b_11.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_11)

        self.b_12 = QPushButton(self)
        self.b_12.setObjectName(u"b_12")
        sizePolicy.setHeightForWidth(
            self.b_12.sizePolicy().hasHeightForWidth())
        self.b_12.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_12)

        self.verticalLayout.addLayout(self.h3)

        self.h4 = QHBoxLayout()
        self.h4.setObjectName(u"h4")
        self.b_13 = QPushButton(self)
        self.b_13.setObjectName(u"b_13")
        sizePolicy.setHeightForWidth(
            self.b_13.sizePolicy().hasHeightForWidth())
        self.b_13.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_13)

        self.b_14 = QPushButton(self)
        self.b_14.setObjectName(u"b_14")
        sizePolicy.setHeightForWidth(
            self.b_14.sizePolicy().hasHeightForWidth())
        self.b_14.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_14)

        self.b_15 = QPushButton(self)
        self.b_15.setObjectName(u"b_15")
        sizePolicy.setHeightForWidth(
            self.b_15.sizePolicy().hasHeightForWidth())
        self.b_15.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_15)

        self.b_16 = QPushButton(self)
        self.b_16.setObjectName(u"b_16")
        sizePolicy.setHeightForWidth(
            self.b_16.sizePolicy().hasHeightForWidth())
        self.b_16.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_16)

        self.verticalLayout.addLayout(self.h4)

        self.h_buttons = QHBoxLayout()
        self.h_buttons.setObjectName(u"h_buttons")
        self.b_back = QPushButton(self)
        self.b_back.setObjectName(u"b_back")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.b_back.sizePolicy().hasHeightForWidth())
        self.b_back.setSizePolicy(sizePolicy1)

        self.h_buttons.addWidget(self.b_back)

        self.l_selected_coin = QLabel(self)
        self.l_selected_coin.setObjectName(u"l_selected_coin")
        self.l_selected_coin.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.h_buttons.addWidget(self.l_selected_coin)

        self.b_next = QPushButton(self)
        self.b_next.setObjectName(u"b_next")
        sizePolicy1.setHeightForWidth(
            self.b_next.sizePolicy().hasHeightForWidth())
        self.b_next.setSizePolicy(sizePolicy1)

        self.h_buttons.addWidget(self.b_next)

        self.verticalLayout.addLayout(self.h_buttons)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        self.setWindowTitle("Select coin")
        self.title.setText(QCoreApplication.translate(
            "Dialog", u"Choose a digital currency to pay:", None))
        self.b_1.setText("")
        self.b_2.setText("")
        self.b_3.setText("")
        self.b_4.setText("")
        self.b_5.setText("")
        self.b_6.setText("")
        self.b_7.setText("")
        self.b_8.setText("")
        self.b_12.setText("")
        self.b_9.setText("")
        self.b_10.setText("")
        self.b_11.setText("")
        self.b_13.setText("")
        self.b_14.setText("")
        self.b_15.setText("")
        self.b_16.setText("")
        self.b_back.setText("")
        self.b_next.setText("")
    # retranslateUi
        self.events()
        self.set_images()
        self.set_CSS_style()

    def set_CSS_style(self):
        self.setStyleSheet("""
                QLabel#l_selected_coin{
                    font-size: 20px;
                    font-weight: bold;
                    color: blue;
                }
                QLabel#title{
                    font-size: 35px;
                    font-weight: bold;
                }
                QDialog{
                    background-color: white;
                }
                QPushButton {
                    background-color: white; 
                    border: 1px solid white;
                    color: black;
                    border-radius: 10px;
                    font-size: 25px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #858585; 
                    border: 1px solid white;
                    color: white;
                    border-radius: 10px;
                }
                QPushButton:pressed {
                    background-color: #616161; 
                }
            """)

    def events(self):
        self.resize(800, 600)
        center_window(self)
        self.b_back.clicked.connect(self.close_window)
        self.b_next.clicked.connect(self.goto_payment)
        self.b_1.clicked.connect(
            lambda: self.l_selected_coin.setText("Bitcoin (BTC)"))
        self.b_2.clicked.connect(
            lambda: self.l_selected_coin.setText("Bitcoin Cash (BCH)"))
        self.b_3.clicked.connect(
            lambda: self.l_selected_coin.setText("Bitcoin Gold (BTG)"))
        self.b_4.clicked.connect(
            lambda: self.l_selected_coin.setText("Dash (DASH)"))
        self.b_5.clicked.connect(
            lambda: self.l_selected_coin.setText("DigiByte (DGB)"))
        self.b_6.clicked.connect(
            lambda: self.l_selected_coin.setText("Dogecoin (DOGE)"))
        self.b_7.clicked.connect(
            lambda: self.l_selected_coin.setText("Ethereum (ETH)"))
        self.b_8.clicked.connect(
            lambda: self.l_selected_coin.setText("Firo (FIRO)"))
        self.b_9.clicked.connect(
            lambda: self.l_selected_coin.setText("Komodo (KMD)"))
        self.b_10.clicked.connect(
            lambda: self.l_selected_coin.setText("Litecoin (LTC)"))
        self.b_11.clicked.connect(
            lambda: self.l_selected_coin.setText("Qtum (QTUM)"))
        self.b_12.clicked.connect(
            lambda: self.l_selected_coin.setText("Ravencoin (RVN)"))
        self.b_13.clicked.connect(
            lambda: self.l_selected_coin.setText("Reddcoin (RDD)"))
        self.b_14.clicked.connect(
            lambda: self.l_selected_coin.setText("Verge (XVG)"))
        self.b_15.clicked.connect(
            lambda: self.l_selected_coin.setText("Vertcoin (VTC)"))
        self.b_16.clicked.connect(
            lambda: self.l_selected_coin.setText("Zcash (ZEC)"))
        # Global.selected_payment

    def set_images(self):
        ico_size = Global.img_size
        show_image([self.b_back],
                   [r"Payment\Photos\back.png"],
                   [(ico_size * 3, ico_size * 1.3)])
        show_image([self.b_next],
                   [r"Payment\Photos\back.png"],
                   [(ico_size * 3, ico_size * 1.3)],
                   ['h'])
        show_image([self.b_1],
                   [r"Payment\Photos\bitcoin (btc).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_2],
                   [r"Payment\Photos\bitcoin cash (bch).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_3],
                   [r"Payment\Photos\bitcoin gold (btg).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_4],
                   [r"Payment\Photos\dash (dash).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_5],
                   [r"Payment\Photos\digibyte (dgb).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_6],
                   [r"Payment\Photos\dogecoin (doge).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_7],
                   [r"Payment\Photos\ethereum (eth).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_8],
                   [r"Payment\Photos\firo (firo).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_9],
                   [r"Payment\Photos\komodo (kmd).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_10],
                   [r"Payment\Photos\litecoin (ltc).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_11],
                   [r"Payment\Photos\qtum (qtum).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_12],
                   [r"Payment\Photos\ravencoin (rvn).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_13],
                   [r"Payment\Photos\reddcoin (rdd).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_14],
                   [r"Payment\Photos\verge (xvg).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_15],
                   [r"Payment\Photos\vertcoin (vtc).png"],
                   [(ico_size, ico_size)])
        show_image([self.b_16],
                   [r"Payment\Photos\zcash (zec).png"],
                   [(ico_size, ico_size)])

    def close_window(self):
        self.close()

    def goto_payment(self):
        if self.l_selected_coin.text() == "":
            show_the_message(TITLE_COIN_NOT_SELECTED,
                             MESSAGE_COIN_NOT_SELECTED, QMessageBox.Critical)
            Global.selected_payment = ""
        else:
            Global.selected_payment = self.l_selected_coin.text()
            self.close_window()
            try:
                the_ui = Ui_Payment()
                the_ui.exec()
            except TypeError:
                # When price is less than MINIMUM_LIMIT_PRICE,
                # we have to prevent the app to create another useless window for payment.
                pass
