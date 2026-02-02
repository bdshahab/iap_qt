from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import QCursor, QFont, QIcon
from PySide6.QtWidgets import (QComboBox, QDialog, QHBoxLayout,
    QLabel, QMessageBox, QPushButton, QSizePolicy, QVBoxLayout)

import Global
from Payment.web_functions import KEY_DATA_SITE_1, get_latest_key_data, all_address, coin_icons, data, selected_coin_name, selected_coin_icon, selected_coin_address
from tools.Centralization import center_window
from tools.dialogue import show_the_message

from Payment.language import custom_texts
from tools.for_images import show_image

class Ui_Select_Coin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.h1 = QHBoxLayout()
        self.h1.setObjectName(u"h1")
        self.b_select = QComboBox(self)
        self.b_select.addItem("")
        self.b_select.addItem("")
        self.b_select.addItem("")
        self.b_select.setObjectName(u"b_select")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b_select.sizePolicy().hasHeightForWidth())
        self.b_select.setSizePolicy(sizePolicy)
        self.h1.addWidget(self.b_select)
        self.verticalLayout.addLayout(self.h1)
        self.h2 = QHBoxLayout()
        self.h2.setObjectName(u"h2")
        self.selected_icon = QLabel(self)
        self.selected_icon.setObjectName(u"selected_icon")
        self.selected_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.h2.addWidget(self.selected_icon)
        self.verticalLayout.addLayout(self.h2)
        self.h3 = QHBoxLayout()
        self.h3.setObjectName(u"h3")
        self.b_ask_help = QComboBox(self)
        self.b_ask_help.setObjectName(u"b_ask_help")
        sizePolicy.setHeightForWidth(self.b_ask_help.sizePolicy().hasHeightForWidth())
        self.b_ask_help.setSizePolicy(sizePolicy)
        self.h3.addWidget(self.b_ask_help)
        self.verticalLayout.addLayout(self.h3)
        self.h4 = QHBoxLayout()
        self.h4.setObjectName(u"h4")
        self.empty_label = QLabel(self)
        self.empty_label.setObjectName(u"empty_label")
        self.h4.addWidget(self.empty_label)
        self.b_1 = QPushButton(self)
        self.b_1.setObjectName(u"b_1")
        sizePolicy.setHeightForWidth(self.b_1.sizePolicy().hasHeightForWidth())
        self.b_1.setSizePolicy(sizePolicy)
        self.h4.addWidget(self.b_1)
        self.b_2 = QPushButton(self)
        self.b_2.setObjectName(u"b_2")
        sizePolicy.setHeightForWidth(self.b_2.sizePolicy().hasHeightForWidth())
        self.b_2.setSizePolicy(sizePolicy)
        self.h4.addWidget(self.b_2)
        self.b_3 = QPushButton(self)
        self.b_3.setObjectName(u"b_3")
        sizePolicy.setHeightForWidth(self.b_3.sizePolicy().hasHeightForWidth())
        self.b_3.setSizePolicy(sizePolicy)
        self.h4.addWidget(self.b_3)
        self.verticalLayout.addLayout(self.h4)
        self.h_buttons = QHBoxLayout()
        self.h_buttons.setObjectName(u"h_buttons")
        self.b_back = QPushButton(self)
        self.b_back.setObjectName(u"b_back")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.b_back.sizePolicy().hasHeightForWidth())
        self.b_back.setSizePolicy(sizePolicy1)
        self.h_buttons.addWidget(self.b_back)
        self.b_help = QPushButton(self)
        self.b_help.setObjectName(u"b_help")
        sizePolicy1.setHeightForWidth(self.b_help.sizePolicy().hasHeightForWidth())
        self.b_help.setSizePolicy(sizePolicy1)
        self.h_buttons.addWidget(self.b_help)
        self.b_next = QPushButton(self)
        self.b_next.setObjectName(u"b_next")
        sizePolicy1.setHeightForWidth(self.b_next.sizePolicy().hasHeightForWidth())
        self.b_next.setSizePolicy(sizePolicy1)
        self.h_buttons.addWidget(self.b_next)
        self.verticalLayout.addLayout(self.h_buttons)
        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.b_select.setItemText(0, QCoreApplication.translate("Dialog", u"Choose a digital currency to pay:", None))
        self.b_select.setItemText(1, QCoreApplication.translate("Dialog", u"BTC", None))
        self.b_select.setItemText(2, QCoreApplication.translate("Dialog", u"LTC", None))

        self.selected_icon.setText("")
        self.empty_label.setText("")
        self.b_1.setText("")
        self.b_2.setText("")
        self.b_3.setText("")
        self.b_back.setText("")
        self.b_help.setText("")
        self.b_next.setText("")
    # retranslateUi
        try:
            self.set_init_data()
            self.set_custom_text()
            self.set_CSS_style()
            self.is_ok = get_latest_key_data(KEY_DATA_SITE_1)
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
            self.events()
            self.set_images()
            self.setup_buttons()
            self.populate_coin_list()
        except Exception:
            show_the_message(
                self.TITLE_LOST_CONNECTION, self.MESSAGE_LOST_CONNECTION, QMessageBox.Warning, parent=self)
            self.close_window()

    def populate_coin_list(self):
        all_address.clear()
        coin_icons.clear()
        for i in range(25, len(data), 3):
            if data[i].strip() != "":
                self.b_select.addItem(data[i])
                all_address.append(data[i+1])
                coin_icons.append(data[i+2])

    def set_init_data(self):
        self.TITLE_HELP = custom_texts[23]
        self.TITLE_PAYMENT_VERSION = custom_texts[25]
        self.MESSAGE_PAYMENT_VERSION = custom_texts[26]
        self.MESSAGE_HELP = custom_texts[40]
        self.MESSAGE_MAINTENANCE = custom_texts[41]

    def set_custom_text(self):
        self.setWindowTitle(custom_texts[0])
        Global.set_limit_on_size_of_widgets(1.55, self.b_select)
        self.b_select.clear()
        self.b_select.addItem(custom_texts[1])
        self.b_ask_help.clear()
        self.b_ask_help.addItems([
            custom_texts[35],
            custom_texts[36],
            custom_texts[37],
            custom_texts[38],
            custom_texts[39],
        ])
        self.b_1.setVisible(False)
        self.b_2.setVisible(False)
        self.b_3.setVisible(False)
    
    def set_CSS_style(self):
        self.font = QFont()
        self.font.setPointSize(25)
        self.setFont(self.font)

        self.setStyleSheet("""
                QDialog{
                    background-color: white;
                }
                QPushButton {
                    background-color: white; 
                    border: 1px solid white;
                    border-radius: 10px;
                }
                QPushButton:hover {
                    background-color: #858585; 
                    border: 1px solid white;
                    border-radius: 10px;
                }
                QPushButton:pressed {
                    background-color: #616161; 
                }
                /* =========================
                BLUE COMBOBOX (b_select)
                ========================= */
                QComboBox#b_select {
                    background-color: #1e88e5;
                    color: white;
                    padding: 6px 10px;
                }
                QComboBox#b_select:hover {
                    background-color: #2196f3;  /* slightly brighter */
                }
                QComboBox#b_select QAbstractItemView {
                    background-color: #e3f2fd;   /* light blue */
                    color: #0d47a1;
                    selection-background-color: #bbdefb;
                    selection-color: #0d47a1;
                }
                QComboBox#b_select QAbstractItemView::item:hover {
                    background-color: #c5e1f9;   /* brighter on hover */
                }
                QComboBox#b_ask_help {
                    background-color: #2e7d32;
                    color: white;
                }
                QComboBox#b_ask_help:hover {
                    background-color: #43a047;   /* slightly brighter */
                }
                /* Dropdown list */
                QComboBox#b_ask_help QAbstractItemView {
                    background-color: #e8f5e9;   /* light green */
                    color: #1b5e20;
                    selection-background-color: #c8e6c9;
                    selection-color: #1b5e20;
                }
                QComboBox#b_ask_help QAbstractItemView::item:hover {
                    background-color: #c8e6c9;   /* brighter on hover */
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
                    border-radius: 10px;
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
        self.b_back.clicked.connect(self.close_window)
        self.b_next.clicked.connect(self.goto_payment)
        self.b_help.clicked.connect(self.show_help)
        self.b_select.currentIndexChanged.connect(lambda _: self.on_coin_changed())
        self.b_ask_help.currentIndexChanged.connect(lambda _: self.on_ask_changed())

    def on_coin_changed(self):
        if self.b_select.currentIndex() > 0:
            selected_coin_name.clear()
            selected_coin_name.clear()
            selected_coin_name.append(self.b_select.currentText())
            selected_coin_name.append(self.b_select.currentText())
            selected_coin_icon.clear()
            selected_coin_icon.append(coin_icons[self.b_select.currentIndex()-1])
            selected_coin_address.clear()
            selected_coin_address.append(all_address[self.b_select.currentIndex()-1])
            show_image([self.selected_icon], [coin_icons[self.b_select.currentIndex()-1]], [(int(Global.img_size), int(Global.img_size))])
            self.selected_icon.setCursor(QCursor(Qt.PointingHandCursor))
            self.selected_icon.setToolTip(self.b_select.currentText())
            self.selected_icon.mousePressEvent = lambda _: self.on_selected_icon()
        else:
            self.selected_icon.clear()
            self.selected_icon.unsetCursor()
            self.selected_icon.setToolTip("")

    def on_selected_icon(self):
        if self.b_select.currentIndex() > 0:
            Global.search_term(self.b_select.currentText())

    def on_ask_changed(self):
        index = self.b_ask_help.currentIndex()
        self.current_urls = []
        
        # Visibility logic
        buttons_visible = index > 0
        self.empty_label.setVisible(not buttons_visible)
        for btn in (self.b_1, self.b_2, self.b_3):
            btn.setVisible(buttons_visible)
        
        if not buttons_visible:
            return
        
        # Define URL and image data indices for each index
        index_map = {
            1: (1, 3, 5),    # URL indices for buttons 1-3
            2: (7, 9, 11),   # URL indices for buttons 1-3
            3: (13, 15, 17), # URL indices for buttons 1-3
            4: (19, 21, 23)  # URL indices for buttons 1-3
        }
        
        # Image indices are URL indices + 1
        image_indices = {k: (v+1 for v in values) for k, values in index_map.items()}
        
        if index in index_map:
            buttons = [self.b_1, self.b_2, self.b_3]
            url_indices = index_map[index]
            img_indices = image_indices[index]
            
            for btn, url_idx, img_idx in zip(buttons, url_indices, img_indices):
                url = data[url_idx]
                self.current_urls.append(url)
                btn.setToolTip(url)
                show_image([btn], 
                        [data[img_idx]], 
                        [(int(Global.img_size), int(Global.img_size))])

    # Connect these during initialization:
    def setup_buttons(self):
        """Connect buttons to their click handlers"""
        # Use lambda to capture button index
        self.b_1.clicked.connect(lambda: self.open_button_url(0))
        self.b_2.clicked.connect(lambda: self.open_button_url(1))
        self.b_3.clicked.connect(lambda: self.open_button_url(2))
        if self.is_ok == -1:
            self.close_window()

    def open_button_url(self, button_index):
        """Open URL for the clicked button"""
        import webbrowser
        # Check if we have URLs stored and the index is valid
        if hasattr(self, 'current_urls') and button_index < len(self.current_urls):
            url = self.current_urls[button_index]
            if url:  # Make sure URL is not empty
                webbrowser.open(url)
    
    
    def show_help(self):
        show_the_message(
            self.TITLE_HELP, self.MESSAGE_HELP, QMessageBox.Information, parent=self)
    
    def set_images(self):
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        show_image([self.b_back],
                   [r"Payment\Photos\back.png"],
                   [(int(Global.img_size * 3), int(Global.img_size * 1.3))])
        show_image([self.b_next],
                   [r"Payment\Photos\back.png"],
                   [(int(Global.img_size * 3), int(Global.img_size * 1.3))],
                   ['h'])
        show_image([self.b_help],
                   [r"Payment\Photos\help.png"],
                   [(int(Global.img_size), int(Global.img_size))])

    def close_window(self):
        try:
            self.deleteLater()
            self.close()
        except Exception:
            pass

    def closeEvent(self, event):
        try:
            super().closeEvent(event)
            event.accept()
            self.close_window()
        except Exception:
            pass

    def goto_payment(self):
        if self.b_select.currentIndex() == 0:
            show_the_message(custom_texts[2],
                            custom_texts[3], QMessageBox.Critical)
            Global.selected_payment = ""
        else:
            Global.selected_payment = self.b_select.currentText()
            self.close_window()
            try:
                from tools.dialogue import loading
                loading(Global.NextWindow.UI_PAYMENT)
            except TypeError:
                # When price is less than MINIMUM_LIMIT_PRICE,
                # we have to prevent the app to create another useless window for payment.
                pass
