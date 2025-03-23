from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon


def show_the_message(title, message, icon_type):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(icon_type)
    msg.setWindowIcon(QIcon("About/Photos/icon.png"))
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)

    _ = msg.exec()
