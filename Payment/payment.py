from decimal import Decimal
import json
import re
import time
from PySide6.QtCore import (
    QCoreApplication, QMetaObject, QSize, QTimer, QElapsedTimer, Qt)
from PySide6.QtGui import QCursor, QDesktopServices, QIcon
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QVBoxLayout, QMessageBox)
import requests

import Global
from Payment.iap_variables import APP_PRICE, TESTING, TOTAL_TIME
from Payment.web_functions import KEY_DATA_SITE_2, KEY_DATA_SITE_3, data, format_with_separator, get_just_number, get_latest_key_data, get_with_fallback, verify_payment
from tools import for_time
from tools.Centralization import center_window
from tools.dialogue import show_the_message
from tools.for_images import show_image

from Payment.web_functions import selected_coin_name, selected_coin_icon, selected_coin_address
from Payment.language import custom_texts


first_clock_now = ""
last_clock_now = ""
first_date_now = ""
last_date_now = ""


class Ui_Payment(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
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
        self.set_custom_text()
        self.set_images()
        self.set_CSS_style()
        self.set_data()
        self.events()

    def set_custom_text(self):
        self.setWindowTitle(custom_texts[4])
        Global.set_limit_on_size_of_widgets(1, self.title)
        Global.set_limit_on_size_of_widgets(0.25, self.l_address)
        Global.set_limit_on_size_of_widgets(0.25, self.l_price)
        Global.set_limit_on_size_of_widgets(1.55, self.l_txid)

        self.title.setText(custom_texts[5])
        self.l_address.setText(custom_texts[6])
        self.l_price.setText(custom_texts[7])
        self.l_txid.setText(custom_texts[8])
        self.TITLE_ANOTHER_ADDRESS = custom_texts[9]
        self.MESSAGE_ANOTHER_ADDRESS = custom_texts[10]
        self.TITLE_EXACT_PRICE = custom_texts[11]
        self.MESSAGE_EXACT_PRICE = custom_texts[12]
        self.TITLE_TXID_NOT_EXIST = custom_texts[13]
        self.MESSAGE_TXID_NOT_EXIST = custom_texts[14]
        self.TITLE_ANOTHER_DATE = custom_texts[15]
        self.MESSAGE_ANOTHER_DATE = custom_texts[16]
        self.TITLE_ANOTHER_TIME = custom_texts[17]
        self.MESSAGE_ANOTHER_TIME = custom_texts[18]
        self.TITLE_LOST_CONNECTION = custom_texts[19]
        self.MESSAGE_LOST_CONNECTION = custom_texts[20]
        self.TITLE_EMPTY_TXID = custom_texts[21]
        self.MESSAGE_EMPTY_TXID = custom_texts[22]
        self.TITLE_HELP = custom_texts[23]
        self.MESSAGE_HELP = custom_texts[24]
        self.TITLE_PAYMENT_VERSION = custom_texts[25]
        self.MESSAGE_PAYMENT_VERSION = custom_texts[26]
        self.TITLE_ANOTHER_CURRENCY = custom_texts[27]
        self.MESSAGE_ANOTHER_CURRENCY = custom_texts[28]

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
                QMessageBox {
                    background-color: white;
                    color: black;
                }
                QMessageBox QLabel {
                    color: black;
                }
                QMessageBox QPushButton {
                    color: white;
                    border: 1px solid #40b35f;
                    background-color: #40b35f;
                }
                QMessageBox QPushButton:hover {
                    border: 1px solid #7ee099;
                    background-color: #7ee099;
                }
                QMessageBox QPushButton:pressed {
                    border: 1px solid #077525;
                    background-color: #077525;
                }
            """)

    def events(self):
        self.setMinimumSize(100, 1)
        self.resize(Global.screen_width * 0.75, Global.screen_height * 0.75)
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

        # We need a reference to help the dialog box
        self.msg = None
        self.timer = QTimer()
        self.elapsed_timer = QElapsedTimer()
        self.base_time = TOTAL_TIME[0]

        self.start_time()

    def search_term(self, term):
        """Open browser and search for the term"""
        search_url = f"https://duckduckgo.com/?q={term}"
        QDesktopServices.openUrl(search_url)

    def set_images(self):
        img_size = int(Global.img_size * 0.8)
        self.icon.setToolTip(str(selected_coin_name[0]))
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        self.icon.setCursor(QCursor(Qt.PointingHandCursor))
        self.icon.mousePressEvent = lambda _: self.search_term(selected_coin_name[0])
        show_image([self.icon],
                   [selected_coin_icon[0]],
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
                   [(int(img_size * 3), int(img_size * 1.3))])
        show_image([self.b_help],
                   ["Payment/Photos/help.png"],
                   [(int(img_size * 2), int(img_size * 1.5))])
        show_image([self.b_copyall],
                   ["Payment/Photos/copy.png"],
                   [(int(img_size * 2), int(img_size * 1.5))])
        show_image([self.b_buy],
                   ["Payment/Photos/buy.png"],
                   [(int(img_size * 2), int(img_size * 1.5))])

    def close_window(self):
        try:
            Global.selected_payment = ""
            self.reset_timer()
            self.close()
            self.deleteLater()
        except Exception:
            pass

    def closeEvent(self, event):
        # This function is necessary if the help dialog is shown and time runs out!
        try:
            # Close the QMessageBox if it exists
            if self.msg and self.msg.isVisible():
                self.msg.close()
            super().closeEvent(event)
            event.accept()
            self.close_window()
        except Exception:
            pass

    def goto_select_coin(self):
        Global.selected_payment = ""
        self.reset_timer()
        self.close_window()
        from tools.dialogue import loading
        loading(Global.NextWindow.UI_SELECT_COIN)

    def payment_successful(self):
        # stopping timer and closing window and showing confirmation
        self.reset_timer()
        self.close_window()
        from tools.dialogue import loading
        loading(Global.NextWindow.UI_BOUGHT)

    def goto_bought(self):
        txid = self.t_txid.text()
        if txid:
            try:
                self.b_buy.setEnabled(False)
                price = self.t_price.text()
                self.is_ok = get_latest_key_data(KEY_DATA_SITE_3)
                if self.is_ok == -1: # The app is under repair.
                    show_the_message(self.TITLE_HELP,self.MESSAGE_MAINTENANCE,QMessageBox.Critical,parent=self)
                    return
                elif self.is_ok == -2: # The app is currently free.
                    self.close()
                    from tools.dialogue import loading
                    loading(Global.NextWindow.UI_BOUGHT)
                    return
                elif self.is_ok == False:
                    show_the_message(self.TITLE_PAYMENT_VERSION,
                                        self.MESSAGE_PAYMENT_VERSION, QMessageBox.Critical)
                    self.close()
                    from tools.dialogue import loading
                    loading(Global.NextWindow.UI_ABOUT)
                    return

                # Get Time
                response = get_with_fallback(data[1])
                the_result = response.text
                pattern = data[2]
                match = re.search(pattern, the_result)
                global first_clock_now, last_clock_now, first_date_now, last_date_now
                if match:
                    last_clock_now = match.group(1)
                else:
                    raise Exception
                # Get Date
                pattern = data[3]
                match = re.search(pattern, the_result)
                if match:
                    last_date_now = match.group(1)
                else:
                    raise Exception
                try:
                    self.b_buy.setEnabled(True)
                    the_address = self.input_address.text()
                    verify_result = verify_payment(
                        Global.selected_payment, the_address, price, txid, first_date_now,
                        last_date_now, first_clock_now, last_clock_now)
                    if verify_result == "OK":
                        self.payment_successful()
                    elif self.base_time < 0:
                        return
                    elif verify_result == "ADDRESS":
                        show_the_message(
                            self.TITLE_ANOTHER_ADDRESS, self.MESSAGE_ANOTHER_ADDRESS, QMessageBox.Warning, parent=self)
                    elif verify_result == "PRICE":
                        show_the_message(
                            self.TITLE_EXACT_PRICE, self.MESSAGE_EXACT_PRICE, QMessageBox.Warning, parent=self)
                    elif verify_result == "TXID":
                        show_the_message(
                            self.TITLE_TXID_NOT_EXIST, self.MESSAGE_TXID_NOT_EXIST, QMessageBox.Warning, parent=self)
                    elif verify_result == "DATE":
                        show_the_message(
                            self.TITLE_ANOTHER_DATE, self.MESSAGE_ANOTHER_DATE, QMessageBox.Warning, parent=self)
                    elif verify_result == "TIME":
                        show_the_message(
                            self.TITLE_ANOTHER_TIME, self.MESSAGE_ANOTHER_TIME, QMessageBox.Warning, parent=self)
                except ValueError:
                    show_the_message(
                        self.TITLE_TXID_NOT_EXIST, self.MESSAGE_TXID_NOT_EXIST, QMessageBox.Warning, parent=self)
            except (requests.exceptions.ConnectionError, ValueError):
                self.b_buy.setEnabled(True)
                show_the_message(
                    self.TITLE_LOST_CONNECTION, self.MESSAGE_LOST_CONNECTION, QMessageBox.Warning, parent=self)
        else:
            self.b_buy.setEnabled(True)
            show_the_message(
                self.TITLE_EMPTY_TXID, self.MESSAGE_EMPTY_TXID, QMessageBox.Critical, parent=self)

    def show_help(self):
        show_the_message(
            self.TITLE_HELP, self.MESSAGE_HELP, QMessageBox.Information, parent=self)

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

    def set_data(self):
        self.input_address.setText(selected_coin_address[0])

    def start_time(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)

        self.elapsed_timer = QElapsedTimer()
        self.base_time = TOTAL_TIME[0]
        self.time.setText(for_time.get_display_time(self.base_time))
        self.reset_timer()

        self.start_timer()
        self.updateTime()

    def updateTime(self):
        """
        This function updates every second, and we could also decrement the base time by 1 unit.
        But if the window freezes, it will not run, and time will fall behind in real time!
        So we use real-time difference to prevent that problem.
        """
        try:
            self.base_time = TOTAL_TIME[0] - \
                (int(time.time()) - for_time.start_time_in_system)
            self.time.setText(for_time.get_display_time(self.base_time))
            if self.base_time > 2 * (TOTAL_TIME[0] / 3):
                self.time.setStyleSheet("color: #0000ff;")
            elif self.base_time > (TOTAL_TIME[0] / 3):
                self.time.setStyleSheet("color: #14992f;")
            else:
                self.time.setStyleSheet("color: #ff0000;")
            if self.base_time < 0:
                self.goto_select_coin()
        except Exception:
            pass

    def start_timer(self):
        if not self.timer.isActive():
            for_time.start_time_in_system = int(time.time())
            self.elapsed_timer.start()
            self.timer.start(1000)  # Update every 1000 ms
            if self.t_price.text() == "":
                try:
                    self.is_ok = get_latest_key_data(KEY_DATA_SITE_2)
                    if self.is_ok == -1:
                        show_the_message(self.TITLE_HELP,self.MESSAGE_MAINTENANCE,QMessageBox.Critical,parent=self)
                        self.close()
                        return
                    elif self.is_ok == -2: # if it's free
                        self.close()
                        from tools.dialogue import loading
                        loading(Global.NextWindow.UI_BOUGHT)
                        return
                    elif self.is_ok == False:
                        show_the_message(self.TITLE_PAYMENT_VERSION,
                                            self.MESSAGE_PAYMENT_VERSION, QMessageBox.Critical)
                        self.close()
                        from tools.dialogue import loading
                        loading(Global.NextWindow.UI_ABOUT)
                        return
                    else:
                        # change updated time
                        TOTAL_TIME[0] = int(data[1])
                        self.base_time = TOTAL_TIME[0] + 1
                        # We have to get price from json
                        dic_price = json.loads(data[2])
                        dic_minimum_price = json.loads(data[3])
                        # set price of the app
                        response = get_with_fallback(str(dic_price.get(Global.selected_payment)))
                        the_result = response.text
                        # Regex to find price
                        pattern = data[4]

                        match = re.search(pattern, the_result)
                        if match:
                            price_str = match.group(1)
                            price = get_just_number(price_str)
                            
                            the_price = APP_PRICE / float(price)
                            the_price = Decimal(the_price)
                            # Automatically handles full decimal witout scientific (e)
                            the_price = format(the_price, 'f')
                            number_of_decimal_digits = len(dic_minimum_price.get(Global.selected_payment)) - 2
                            self.t_price.setText(format_with_separator(the_price, number_of_decimal_digits, ""))
                        else:
                            raise Exception
                        # Get Time
                        response = get_with_fallback(data[5])
                        the_result = response.text
                        pattern = data[6]
                        match = re.search(pattern, the_result)
                        global first_clock_now, first_date_now
                        if match:
                            first_clock_now = match.group(1)
                        else:
                            raise Exception
                        # Get Date
                        pattern = data[7]
                        match = re.search(pattern, the_result)
                        if match:
                            first_date_now = match.group(1)
                        else:
                            raise Exception
                        # Get mimimum valid amount
                        the_minimum = json.loads(data[3]).get(Global.selected_payment)
                        if Decimal(the_price) < Decimal(the_minimum):
                            show_the_message(self.TITLE_ANOTHER_CURRENCY, self.MESSAGE_ANOTHER_CURRENCY, parent=self)
                            self.goto_select_coin()
                        elif TESTING:
                            print("First Time format: " + first_clock_now)
                            print("First Date format: " + first_date_now)
                except Exception:
                    show_the_message(
                        self.TITLE_LOST_CONNECTION, self.MESSAGE_LOST_CONNECTION, QMessageBox.Warning, parent=self)
                    self.goto_select_coin()

    def reset_timer(self):
        self.timer.stop()
        for_time.start_time_in_system = 0