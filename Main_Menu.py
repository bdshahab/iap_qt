import os
from PySide6.QtCore import (QCoreApplication, QMetaObject, QEvent)
from PySide6.QtGui import (QAction, QIcon)
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QSizePolicy,
                               QVBoxLayout, QWidget, QMessageBox)

from Payment.iap_variables import *
import sys
import Global
from tools.dialogue import show_the_message
from tools.Centralization import center_window
from Payment.language import custom_texts


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
        Global.img_size = self.size().width() // 10

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
            show_the_message(
                custom_texts[33], custom_texts[34], QMessageBox.Information)
        else:
            from tools.dialogue import loading
            loading(Global.NextWindow.UI_SELECT_COIN)

    def goto_about(self):
        from tools.dialogue import loading
        loading(Global.NextWindow.UI_ABOUT)


def set_centralize(app):
    # Get the available screen size
    screen_geometry = QApplication.primaryScreen().availableGeometry()
    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))

    Global.screen_height = screen_geometry.height()
    Global.screen_width = screen_geometry.width()

    if Global.screen_height < Global.screen_width:
        Global.img_size = Global.screen_height // 8
    else:
        Global.img_size = Global.screen_width // 8

    # Resize the window to 75% of screen size
    new_width = int(Global.screen_width * 0.75)
    new_height = int(Global.screen_height * 0.75)
    app.resize(new_width, new_height)

    app.move(
        (Global.screen_width - new_width) // 2,
        (Global.screen_height - new_height) // 2
    )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    set_centralize(ui)
    ui.show()
    sys.exit(app.exec())
