from tools.Centralization import center_window
from PySide6.QtCore import Qt, QTimer, QCoreApplication, QEvent
from PySide6.QtWidgets import QDialog, QLabel, QVBoxLayout, QMessageBox, QApplication
from PySide6.QtGui import QIcon

from Payment.language import custom_texts


def show_the_message(title, message, icon_type, parent=None):
    import Global
    msg = QMessageBox(parent)
    
    # Set icon and title
    msg.setWindowIcon(QIcon("About/Photos/icon.png"))
    msg.setWindowTitle(title)
    
    # Hide the default text (we'll use a custom QLabel)
    msg.setText("")  
    
    msg.setIcon(icon_type)

    # Add OK button
    ok_button = msg.addButton(QMessageBox.Ok)
    ok_button.setText((" " * 2) + "OK" + (" " * 2))
    
    msg.setWindowModality(Qt.ApplicationModal)
    # ------------------------------------------------------------------
    # Custom QLabel for the message content
    # ------------------------------------------------------------------
    label = QLabel(message)
    label.setTextFormat(Qt.RichText)      # support HTML
    label.setWordWrap(True)               # allow multi-line
    label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
    font = label.font()
    font.setPointSize(24)        # ← change size here
    # font.setBold(True)        # optional
    label.setFont(font)
    label.setMinimumWidth(Global.screen_width // 2)  # half of screen width

    # Add QLabel to the QMessageBox layout
    msg.layout().addWidget(label, 0, 1)  # row 0, column 1 (content area)
    # font-size: 14px;
    ok_button.setStyleSheet("""
        QPushButton {
            font-size: 34px;
            font-weight: bold;
            padding: 8px 22px;
            border-radius: 6px;
            background-color: #38d130;
        }
        QPushButton:hover {
            background-color: #8beb86;
        }
        QPushButton:pressed {
            background-color: #108c0a;
        }
        """)

    return msg.exec()


def loading(next_window):
    import os
    import sys
    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))

    import Global  # path for this is done from parent window.
    if (next_window == Global.NextWindow.UI_SELECT_COIN) and Global.user_bought:
        from tools.dialogue import show_the_message
        show_the_message(
            custom_texts[33], custom_texts[34], QMessageBox.Information)
        return
    # Create and setup loading dialog
    loading_dialog = QDialog()
    loading_dialog.setWindowFlags(
        Qt.Window | Qt.CustomizeWindowHint | Qt.WindowTitleHint)
    loading_dialog.setModal(True)
    loading_dialog.setWindowTitle("Loading...")

    layout = QVBoxLayout()
    label = QLabel("Loading..." + "\n" + "Please wait")

    label.setAlignment(Qt.AlignCenter)
    layout.addWidget(label)
    loading_dialog.setLayout(layout)
    loading_dialog.setStyleSheet("""
                                 QLabel{
                                     font-size: """ + str(int(Global.img_size * 1.4)) + """px;
                                     font-weight: bold;
                                }
                                 """)

    loading_dialog.resize(int(Global.screen_width * 0.75),
                          int(Global.screen_height * 0.75))
    center_window(loading_dialog)

    loading_dialog.show()
    QApplication.processEvents()  # Force UI update

    def do_loading():
        the_ui = None
        try:
            if next_window == Global.NextWindow.UI_SELECT_COIN:
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
        except Exception as e:
            print(e)
            pass
        finally:
            loading_dialog.close()
            # Remove posted events before opening next window
            QCoreApplication.sendPostedEvents(None, QEvent.Type.None_)
            QCoreApplication.processEvents()
            if the_ui is not None:
                try:
                    the_ui.exec()
                except Exception:
                    pass

    # Use zero-delay timer to start loading immediately after UI refresh
    QTimer.singleShot(10, do_loading)
