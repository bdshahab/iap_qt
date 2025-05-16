import importlib
import threading
import time
from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtCore import QEvent
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget, QMessageBox)

from Payment.iap_variables import *
import sys
import Global
from tools.dialogue import show_the_message
from tools.Centralization import center_window


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(u"")
        self.actionExit = QAction(self)
        self.actionExit.setObjectName(u"actionExit")
        self.actionExit_2 = QAction(self)
        self.actionExit_2.setObjectName(u"actionExit_2")
        self.actionView_help = QAction(self)
        self.actionView_help.setObjectName(u"actionView_help")
        self.actionAbout = QAction(self)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.situation_button = QPushButton(self.centralwidget)
        self.situation_button.setObjectName(u"situation_button")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)  # TODO
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.situation_button.sizePolicy().hasHeightForWidth())
        self.situation_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.situation_button)

        self.pay_button = QPushButton(self.centralwidget)
        self.pay_button.setObjectName(u"pay_button")
        sizePolicy.setHeightForWidth(
            self.pay_button.sizePolicy().hasHeightForWidth())
        self.pay_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.pay_button)

        self.about_button = QPushButton(self.centralwidget)
        self.about_button.setObjectName(u"about_button")
        sizePolicy.setHeightForWidth(
            self.about_button.sizePolicy().hasHeightForWidth())
        self.about_button.setSizePolicy(sizePolicy)
        self.about_button.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.about_button)

        self.exit_button = QPushButton(self.centralwidget)
        self.exit_button.setObjectName(u"exit_button")
        sizePolicy.setHeightForWidth(
            self.exit_button.sizePolicy().hasHeightForWidth())
        self.exit_button.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.exit_button)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        Global.img_size = self.size().width()//10

    def retranslateUi(self, MainWindow):
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        self.setWindowTitle("IAP by cryptocurrency")

        self.actionExit.setText(QCoreApplication.translate(
            "MainWindow", u"Payment", None))
        self.actionExit_2.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionView_help.setText(
            QCoreApplication.translate("MainWindow", u"View help", None))
        self.actionAbout.setText(
            QCoreApplication.translate("MainWindow", u"About", None))
        self.situation_button.setText(QCoreApplication.translate(
            "MainWindow", u"You have not purchased this app yet!", None))
        self.pay_button.setText(QCoreApplication.translate(
            "MainWindow", u"In App Purchase by Cryptocurrency", None))
        self.about_button.setText(
            QCoreApplication.translate("MainWindow", u"About", None))
        self.exit_button.setText(
            QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi
        self.events()
        self.set_CSS_style()

    def events(self):
        self.setMinimumSize(100, 1)
        self.resize(Global.screen_width * 0.75, Global.screen_height * 0.75)
        center_window(self)
        self.pay_button.clicked.connect(self.goto_select_coin)
        self.about_button.clicked.connect(self.goto_about)
        self.exit_button.clicked.connect(lambda: sys.exit())

    def changeEvent(self, event):
        # Check if the event is a window activation change
        if event.type() == QEvent.ActivationChange and self.isActiveWindow():
            self.on_window_focused()
        # Call the base class method to handle other events
        super().changeEvent(event)

    def on_window_focused(self):
        # This method is called when the window gains focus
        if Global.user_bought:
            self.situation_button.setStyleSheet("background-color: #008000;")
            self.situation_button.setText("You bought this app!")
        else:
            self.situation_button.setStyleSheet("background-color: #808080;")
            self.situation_button.setText(
                "You have not purchased this app yet!")

    def set_CSS_style(self):
        self.setStyleSheet("""
                QMainWindow{
                    background-color: #f1ff00;
                }
                QPushButton {
                    background-color: #808080;
                    color: white;
                    border: 2px solid black;
                    padding: 10px;
                    border-radius: 20px;
                    font-size: 20px;
                }
                QPushButton:hover {
                    background-color: #b3b3b3;
                }
                QPushButton:pressed {
                    background-color: #5C5C5C;
                }
            """)

    def goto_select_coin(self):
        if Global.user_bought:
            show_the_message(TITLE_PAID, MESSAGE_PAID, QMessageBox.Information)
        else:
            from Payment.select_coin import Ui_Select_Coin
            the_ui = Ui_Select_Coin()
            the_ui.exec()

    def goto_about(self):
        from About.about import Ui_About
        the_ui = Ui_About()
        the_ui.exec()


def loading_heavy_modules_for_fast_loading():
    importlib.import_module("About.about")
    importlib.import_module("Payment.select_coin")
    importlib.import_module("Payment.bought")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.show()
    threading.Thread(target=loading_heavy_modules_for_fast_loading).start()

    sys.exit(app.exec())
