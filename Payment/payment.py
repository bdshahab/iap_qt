from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtCore import QTimer, QElapsedTimer
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLineEdit,
                               QSizePolicy, QVBoxLayout, QMessageBox)

import Global
import Payment.addresses as addr
from Payment.web_functions import *
from tools.Centralization import center_window
from tools.dialogue import show_the_message
from tools.for_images import *
from tools.for_time import *
from tools.iap_variables import *

first_clock_now = ""
last_clock_now = ""
first_date_now = ""
last_date_now = ""


class Ui_Payment(QDialog):
    def __init__(self):
        super().__init__()
        self.elapsed_timer = None
        self.timer = None
        self.msg = None
        self.base_time = None
        self.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.h1 = QHBoxLayout()
        self.h1.setObjectName(u"h1")
        self.icon = QLabel(self)
        self.icon.setObjectName(u"icon")

        self.h1.addWidget(self.icon)

        self.title = QLabel(self)
        self.title.setObjectName(u"title")

        self.h1.addWidget(self.title)

        self.time = QLabel(self)
        self.time.setObjectName(u"time")
        self.time.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time.setAlignment(Qt.AlignmentFlag.AlignRight |
                               Qt.AlignmentFlag.AlignTrailing | Qt.AlignmentFlag.AlignVCenter)

        self.h1.addWidget(self.time)

        self.verticalLayout.addLayout(self.h1)

        self.h2 = QHBoxLayout()
        self.h2.setObjectName(u"h2")
        self.l_address = QLabel(self)
        self.l_address.setObjectName(u"l_address")
        self.l_address.setMinimumSize(QSize(100, 0))

        self.h2.addWidget(self.l_address)

        self.input_address = QLineEdit(self)
        self.input_address.setObjectName(u"input_address")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.input_address.sizePolicy().hasHeightForWidth())
        self.input_address.setSizePolicy(sizePolicy)
        self.input_address.setStyleSheet(u"")
        self.input_address.setReadOnly(True)

        self.h2.addWidget(self.input_address)

        self.copy_address = QPushButton(self)
        self.copy_address.setObjectName(u"copy_address")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.copy_address.sizePolicy().hasHeightForWidth())
        self.copy_address.setSizePolicy(sizePolicy1)
        self.copy_address.setMinimumSize(QSize(75, 0))

        self.h2.addWidget(self.copy_address)

        self.verticalLayout.addLayout(self.h2)

        self.h3 = QHBoxLayout()
        self.h3.setObjectName(u"h3")
        self.l_price = QLabel(self)
        self.l_price.setObjectName(u"l_price")
        sizePolicy2 = QSizePolicy(
            QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.l_price.sizePolicy().hasHeightForWidth())
        self.l_price.setSizePolicy(sizePolicy2)
        self.l_price.setMinimumSize(QSize(100, 0))

        self.h3.addWidget(self.l_price)

        self.t_price = QLineEdit(self)
        self.t_price.setObjectName(u"t_price")
        sizePolicy.setHeightForWidth(
            self.t_price.sizePolicy().hasHeightForWidth())
        self.t_price.setSizePolicy(sizePolicy)
        self.t_price.setStyleSheet(u"")
        self.t_price.setReadOnly(True)

        self.h3.addWidget(self.t_price)

        self.copy_price = QPushButton(self)
        self.copy_price.setObjectName(u"copy_price")
        sizePolicy1.setHeightForWidth(
            self.copy_price.sizePolicy().hasHeightForWidth())
        self.copy_price.setSizePolicy(sizePolicy1)
        self.copy_price.setMinimumSize(QSize(75, 0))

        self.h3.addWidget(self.copy_price)

        self.verticalLayout.addLayout(self.h3)

        self.l_txid = QLabel(self)
        self.l_txid.setObjectName(u"l_txid")

        self.verticalLayout.addWidget(self.l_txid)

        self.h4 = QHBoxLayout()
        self.h4.setObjectName(u"h4")
        self.t_txid = QLineEdit(self)
        self.t_txid.setObjectName(u"t_txid")
        sizePolicy.setHeightForWidth(
            self.t_txid.sizePolicy().hasHeightForWidth())
        self.t_txid.setSizePolicy(sizePolicy)
        self.t_txid.setStyleSheet(u"")
        self.t_txid.setReadOnly(True)

        self.h4.addWidget(self.t_txid)

        self.paste_txid = QPushButton(self)
        self.paste_txid.setObjectName(u"paste_txid")
        sizePolicy1.setHeightForWidth(
            self.paste_txid.sizePolicy().hasHeightForWidth())
        self.paste_txid.setSizePolicy(sizePolicy1)
        self.paste_txid.setMinimumSize(QSize(75, 0))

        self.h4.addWidget(self.paste_txid)

        self.verticalLayout.addLayout(self.h4)

        self.h_buttons = QHBoxLayout()
        self.h_buttons.setObjectName(u"h_buttons")
        self.b_back = QPushButton(self)
        self.b_back.setObjectName(u"b_back")
        sizePolicy1.setHeightForWidth(
            self.b_back.sizePolicy().hasHeightForWidth())
        self.b_back.setSizePolicy(sizePolicy1)

        self.h_buttons.addWidget(self.b_back)

        self.b_help = QPushButton(self)
        self.b_help.setObjectName(u"b_help")
        sizePolicy1.setHeightForWidth(
            self.b_help.sizePolicy().hasHeightForWidth())
        self.b_help.setSizePolicy(sizePolicy1)

        self.h_buttons.addWidget(self.b_help)

        self.b_copyall = QPushButton(self)
        self.b_copyall.setObjectName(u"b_copyall")
        sizePolicy1.setHeightForWidth(
            self.b_copyall.sizePolicy().hasHeightForWidth())
        self.b_copyall.setSizePolicy(sizePolicy1)

        self.h_buttons.addWidget(self.b_copyall)

        self.b_buy = QPushButton(self)
        self.b_buy.setObjectName(u"b_buy")
        sizePolicy1.setHeightForWidth(
            self.b_buy.sizePolicy().hasHeightForWidth())
        self.b_buy.setSizePolicy(sizePolicy1)

        self.h_buttons.addWidget(self.b_buy)

        self.verticalLayout.addLayout(self.h_buttons)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Form):
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        self.setWindowTitle("Payment")
        self.icon.setText("")
        self.title.setText(QCoreApplication.translate(
            "Form", u"Pay before time's up!", None))
        self.time.setText(QCoreApplication.translate("Form", u"00:00", None))
        self.l_address.setText(
            QCoreApplication.translate("Form", u"Address", None))
        self.input_address.setText("")
        self.copy_address.setText("")
        self.l_price.setText(
            QCoreApplication.translate("Form", u"Price", None))
        self.t_price.setText("")
        self.copy_price.setText("")
        self.l_txid.setText(QCoreApplication.translate(
            "Form", u"Input your Transaction Hash ID (TXID):", None))
        self.paste_txid.setText("")
        self.b_back.setText("")
        self.b_help.setText("")
        self.b_copyall.setText("")
        self.b_buy.setText("")
    # retranslateUi
        self.events()
        self.set_images()
        self.set_CSS_style()
        self.set_data()

    def set_CSS_style(self):
        self.setStyleSheet("""
                QLabel{
                    font-size: 25px;
                    font-weight: bold;
                }
                QLabel#title{
                    font-size: 30px;
                }
                QLabel#time{
                    font-size: 45px;
                }
                QLineEdit{
                    font-size: 25px;
                    color: white;
                    background-color: #0000FF;
                }
                QLineEdit#t_txid{
                    font-size: 25px;
                    color: white;
                    background-color: #FF00FF;
                }
                QDialog{
                    background-color: #cbcbcb;
                }
                QPushButton {
                    background-color: #cbcbcb;
                    border: 1px solid #cbcbcb;
                    color: black;
                    border-radius: 10px;
                    font-size: 25px;
                    font-weight: bold;
                }
                QPushButton:hover {
                    background-color: #858585;
                    border: 1px solid #858585;
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
        self.b_back.clicked.connect(self.goto_select_coin)
        self.b_buy.clicked.connect(self.goto_bought)
        self.b_help.clicked.connect(self.show_help)
        self.copy_address.clicked.connect(
            lambda: self.copy_to_clipboard(self.input_address))
        self.copy_price.clicked.connect(
            lambda: self.copy_to_clipboard(self.t_price))
        self.paste_txid.clicked.connect(
            lambda: self.paste_from_clipboard(self.t_txid))
        self.b_copyall.clicked.connect(
            lambda: self.copyall_to_clipboard())

        # We need a reference to help dialog box
        self.msg = None
        self.timer = QTimer()
        self.elapsed_timer = QElapsedTimer()
        self.base_time = Global.TOTAL_TIME

        self.start_time()

    def set_images(self):
        img_size = Global.img_size

        show_image([self.icon],
                   [addr.cryptos.get(Global.selected_payment)],
                   [(img_size, img_size)])
        show_image([self.copy_address],
                   ["Payment/Photos/copy.png"],
                   [(img_size, img_size)])
        show_image([self.copy_price],
                   ["Payment/Photos/copy.png"],
                   [(img_size, img_size)])
        show_image([self.paste_txid],
                   ["Payment/Photos/paste.png"],
                   [(img_size, img_size)])
        show_image([self.b_back],
                   ["Payment/Photos/back.png"],
                   [(img_size * 3, img_size * 1.3)])
        show_image([self.b_help],
                   ["Payment/Photos/help.png"],
                   [(img_size * 2, img_size * 1.5)])
        show_image([self.b_copyall],
                   ["Payment/Photos/copy.png"],
                   [(img_size * 2, img_size * 1.5)])
        show_image([self.b_buy],
                   ["Payment/Photos/buy.png"],
                   [(img_size * 2, img_size * 1.5)])

    def close_window(self):
        self.close()

    def goto_select_coin(self):
        Global.selected_payment = ""
        self.reset_timer()
        self.close_window()
        from Payment.select_coin import Ui_Select_Coin
        the_ui = Ui_Select_Coin()
        the_ui.exec()

    def get_datetime_data(self):
        response = requests.get(DATE_TIME_SITE)
        response.raise_for_status()  # Raise an error for bad status codes
        the_result = response.text
        return the_result

    def payment_successful(self):
        # stopping timer and closing window and showing confirmation
        self.reset_timer()
        self.close_window()
        from Payment.bought import Ui_Bought
        the_ui = Ui_Bought()
        the_ui.exec()

    def goto_bought(self) -> None:
        txid = self.t_txid.text()
        if txid:
            try:
                self.b_buy.setEnabled(False)
                price = self.t_price.text()
                datetime_data = self.get_datetime_data()
                global first_clock_now, last_clock_now, first_date_now, last_date_now
                last_clock_now = get_current_time(datetime_data)
                last_date_now = get_current_date(datetime_data)
                if TESTING:
                    print("Second Time format: " + last_clock_now)
                    print("Second Date format: " + last_date_now)
                    print(
                        "Now we change some key elements to simulate real payment in testing mode")
                    first_clock_now = "07:00:00"
                    last_clock_now = "07:10:00"
                    price = "0.00994753"
                    first_date_now = "08 Feb 2022"
                    last_date_now = "09 Feb 2022"
                    print(f"first_clock_now: {first_clock_now}")
                    print(f"last_clock_now: {last_clock_now}")
                    print(f"price: {price}")
                    print(f"first_date_now: {first_date_now}")
                    print(f"last_date_now: {last_date_now}")
                try:
                    verify_result = verify_payment(
                        Global.selected_payment, price, txid, first_date_now,
                        last_date_now, first_clock_now, last_clock_now)
                    if verify_result == "OK":
                        self.payment_successful()
                    elif verify_result == "ADDRESS":
                        show_the_message(
                            TITLE_ANOTHER_ADDRESS, MESSAGE_ANOTHER_ADDRESS, QMessageBox.Warning)
                    elif verify_result == "PRICE":
                        show_the_message(
                            TITLE_EXACT_PRICE, MESSAGE_EXACT_PRICE, QMessageBox.Warning)
                    elif verify_result == "TXID":
                        show_the_message(
                            TITLE_TXID_NOT_EXIST, MESSAGE_TXID_NOT_EXIST, QMessageBox.Warning)
                    elif verify_result == "DATE":
                        show_the_message(
                            TITLE_ANOTHER_DATE, MESSAGE_ANOTHER_DATE, QMessageBox.Warning)
                    elif verify_result == "TIME":
                        show_the_message(
                            TITLE_ANOTHER_TIME, MESSAGE_ANOTHER_TIME, QMessageBox.Warning)
                except ValueError:
                    show_the_message(
                        TITLE_TXID_NOT_EXIST, MESSAGE_TXID_NOT_EXIST, QMessageBox.Warning)
            except (requests.exceptions.ConnectionError, ValueError):
                show_the_message(
                    TITLE_LOST_CONNECTION, MESSAGE_LOST_CONNECTION, QMessageBox.Warning)
            finally:
                self.b_buy.setEnabled(True)
        else:
            show_the_message(
                TITLE_EMPTY_TXID, MESSAGE_EMPTY_TXID, QMessageBox.Critical)

    def show_help(self):
        show_the_message(
            TITLE_HELP, MESSAGE_HELP, QMessageBox.Information)

    def copy_to_clipboard(self, the_line_edit):
        # Select all text in the QLineEdit
        if not the_line_edit.text():
            QApplication.clipboard().clear()
        else:
            the_line_edit.selectAll()
            # Copy the selected text to the clipboard
            the_line_edit.copy()
            # Deselect the text
            the_line_edit.deselect()

    def copyall_to_clipboard(self):
        temp = Global.selected_payment + "\n" + self.input_address.text() + "\n" + \
            self.t_price.text() + "\n" + self.t_txid.text()
        # Set custom text to clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(temp)

    def paste_from_clipboard(self, the_line_edit):
        the_line_edit.clear()
        the_line_edit.paste()
        text = the_line_edit.text()
        text = self.remove_all_whitespaces(text)
        text = text.split("/")[-1]
        the_line_edit.clear()
        the_line_edit.setText(text)

    def remove_all_whitespaces(self, temp):
        return "".join(temp.split())

    # This function is necessary if the help dialog is shown and time runs out!

    def closeEvent(self, event):
        # Close the QMessageBox if it exists
        if self.msg and self.msg.isVisible():
            self.msg.close()
        event.accept()

    def set_data(self):
        self.input_address.setText(addr.addresses.get(Global.selected_payment))

    def start_time(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)

        self.elapsed_timer = QElapsedTimer()
        self.base_time = Global.TOTAL_TIME
        self.time.setText(get_display_time(self.base_time))
        self.reset_timer()

        self.updateTime()
        self.start_timer()

    def updateTime(self):
        self.time.setText(get_display_time(self.base_time))
        self.base_time = self.base_time - 1
        if self.base_time > 2 * (Global.TOTAL_TIME / 3):
            self.time.setStyleSheet("color: #0000ff;")
        elif self.base_time > (Global.TOTAL_TIME / 3):
            self.time.setStyleSheet("color: #14992f;")
        else:
            self.time.setStyleSheet("color: #ff0000;")
        if self.base_time < 0:
            self.goto_select_coin()

    def start_timer(self):
        if not self.timer.isActive():
            self.elapsed_timer.start()
            self.timer.start(1000)  # Update every 1000 ms
            if self.t_price.text() == "":
                try:
                    if not get_latest_key_data():
                        show_the_message(TITLE_PAYMENT_VERSION,
                                         MESSAGE_PAYMENT_VERSION, QMessageBox.critical)
                    # set price of the app
                    the_price = APP_PRICE / \
                        float(get_coin_current_price(Global.selected_payment))
                    self.t_price.setText(f"{the_price:.8f}")
                    datetime_data = get_datetime_data()
                    global first_clock_now, first_date_now
                    first_clock_now = get_current_time(datetime_data)
                    first_date_now = get_current_date(datetime_data)

                    if the_price < MINIMUM_LIMIT_PRICE:
                        show_the_message(
                            TITLE_ANOTHER_CURRENCY, MESSAGE_ANOTHER_CURRENCY, QMessageBox.Warning)
                        self.goto_select_coin()
                    elif TESTING:
                        print("First Time format: " + first_clock_now)
                        print("First Date format: " + first_date_now)
                except requests.exceptions.ConnectionError:
                    show_the_message(
                        TITLE_LOST_CONNECTION, MESSAGE_LOST_CONNECTION, QMessageBox.Warning)
                    self.goto_select_coin()

    def reset_timer(self):
        self.timer.stop()
