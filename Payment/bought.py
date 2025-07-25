from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QDialog, QLabel, QPushButton,
                               QSizePolicy, QVBoxLayout)

import Global
from tools.Centralization import center_window
from tools.for_images import show_image
from Payment.language import custom_texts


class Ui_Bought(QDialog):
    def __init__(self):
        super().__init__()
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
        self.set_custom_text()

    def set_custom_text(self):
        self.setWindowTitle(custom_texts[29])
        Global.set_limit_on_size_of_widgets(1.55, self.l1)
        Global.set_limit_on_size_of_widgets(1.55, self.l2)
        Global.set_limit_on_size_of_widgets(1.55, self.l3)

        self.l1.setText(custom_texts[30])
        self.l2.setText(custom_texts[31])
        self.l3.setText(custom_texts[32])

    def set_CSS_style(self):
        self.setStyleSheet("""
            QDialog {
                background-color: #15009c;
            }
            QMainWindow {
                background-color: #15009c;
            }
            QLabel {
                color: white;
                font: 18pt;
            }
            QPushButton {
                background-color: #921ad6;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #ce78ff;
            }
            QPushButton:pressed {
                background-color: #63009c;
            }
        """)

    def events(self):
        self.setMinimumSize(100, 1)
        self.resize(int(Global.screen_width * 0.75),
                    int(Global.screen_height * 0.75))
        center_window(self)
        self.ok.clicked.connect(self.close_window)

    def set_images(self):
        show_image([self.ok],
                   [r"Payment\Photos\buy.png"],
                   [(int(Global.img_size*3), int(Global.img_size*3))])

    def close_window(self):
        Global.user_bought = True
        self.close()

    def closeEvent(self, event):
        try:
            super().closeEvent(event)
            event.accept()
            self.close_window()
        except Exception:
            pass
