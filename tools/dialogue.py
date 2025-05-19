import os
import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QCoreApplication, QEvent, QObject

from Payment.bought import Qt


def show_the_message(title, message, icon_type):
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(message)
    msg.setIcon(icon_type)
    msg.setWindowIcon(QIcon("About/Photos/icon.png"))
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)

    _ = msg.exec()


def set_centralize(app):
    # Get the available screen size
    screen_geometry = QApplication.primaryScreen().availableGeometry()

    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))
    import Global

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

    # Optionally center the window
    app.move(
        screen_geometry.x() + (new_width - Global.img_size) // 4,
        screen_geometry.y() + (new_height - Global.img_size) // 4
    )


def loading(next_window):
    # Remove posted events before opening next window
    QCoreApplication.sendPostedEvents(None, QEvent.Type.None_)
    QCoreApplication.processEvents()

    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))
    import Global
    from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout
    # Show loading dialog
    loading_dialog = QDialog()
    loading_dialog.setWindowFlags(
        Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
    loading_dialog.setModal(True)
    loading_dialog.setWindowTitle("Loading...")
    layout = QVBoxLayout()
    label = QLabel("Please wait, loading...")
    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)
    loading_dialog.setLayout(layout)
    set_centralize(loading_dialog)
    loading_dialog.setWindowOpacity(0.75)
    loading_dialog.show()

    # Process events so the dialog is shown immediately
    QApplication.processEvents()
    the_ui = None
    if next_window == Global.NextWindow.UI_SELECT_COIN:
        if Global.user_bought:
            from tools.dialogue import show_the_message
            from Payment.iap_variables import TITLE_PAID, MESSAGE_PAID
            show_the_message(TITLE_PAID, MESSAGE_PAID, QMessageBox.Information)
            return
        from Payment.select_coin import Ui_Select_Coin
        the_ui = Ui_Select_Coin()
    elif next_window == Global.NextWindow.UI_PAYMENT:
        from Payment.payment import Ui_Payment
        the_ui = Ui_Payment()
    elif next_window == Global.NextWindow.UI_BOUGHT:
        from Payment.bought import Ui_Bought
        the_ui = Ui_Bought()
    elif next_window == Global.NextWindow.UI_ABOUT:
        from About.about import Ui_About
        the_ui = Ui_About()
    # Close the loading dialog before showing main UI
    loading_dialog.close()
    the_ui.exec()
