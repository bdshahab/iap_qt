from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QLayout, QPushButton, QSizePolicy, QVBoxLayout)

from Global import img_size
from tools.Centralization import center_window
from tools.for_images import show_image
import webbrowser


class Ui_About(QDialog):
    def __init__(self):
        super().__init__()
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(
            QLayout.SizeConstraint.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.h0 = QHBoxLayout()
        self.h0.setObjectName(u"h0")
        self.logo = QPushButton(self)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)

        self.h0.addWidget(self.logo)

        self.license = QPushButton(self)
        self.license.setObjectName(u"license")
        sizePolicy.setHeightForWidth(
            self.license.sizePolicy().hasHeightForWidth())
        self.license.setSizePolicy(sizePolicy)

        self.h0.addWidget(self.license)

        self.verticalLayout.addLayout(self.h0)

        self.h1 = QHBoxLayout()
        self.h1.setSpacing(0)
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

        self.b_5 = QPushButton(self)
        self.b_5.setObjectName(u"b_5")
        sizePolicy.setHeightForWidth(self.b_5.sizePolicy().hasHeightForWidth())
        self.b_5.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_5)

        self.b_6 = QPushButton(self)
        self.b_6.setObjectName(u"b_6")
        sizePolicy.setHeightForWidth(self.b_6.sizePolicy().hasHeightForWidth())
        self.b_6.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_6)

        self.b_7 = QPushButton(self)
        self.b_7.setObjectName(u"b_7")
        sizePolicy.setHeightForWidth(self.b_7.sizePolicy().hasHeightForWidth())
        self.b_7.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_7)

        self.b_8 = QPushButton(self)
        self.b_8.setObjectName(u"b_8")
        sizePolicy.setHeightForWidth(self.b_8.sizePolicy().hasHeightForWidth())
        self.b_8.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_8)

        self.b_9 = QPushButton(self)
        self.b_9.setObjectName(u"b_9")
        sizePolicy.setHeightForWidth(self.b_9.sizePolicy().hasHeightForWidth())
        self.b_9.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_9)

        self.b_10 = QPushButton(self)
        self.b_10.setObjectName(u"b_10")
        sizePolicy.setHeightForWidth(
            self.b_10.sizePolicy().hasHeightForWidth())
        self.b_10.setSizePolicy(sizePolicy)

        self.h1.addWidget(self.b_10)

        self.verticalLayout.addLayout(self.h1)

        self.h2 = QHBoxLayout()
        self.h2.setSpacing(0)
        self.h2.setObjectName(u"h2")
        self.b_11 = QPushButton(self)
        self.b_11.setObjectName(u"b_11")
        sizePolicy.setHeightForWidth(
            self.b_11.sizePolicy().hasHeightForWidth())
        self.b_11.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_11)

        self.b_12 = QPushButton(self)
        self.b_12.setObjectName(u"b_12")
        sizePolicy.setHeightForWidth(
            self.b_12.sizePolicy().hasHeightForWidth())
        self.b_12.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_12)

        self.b_13 = QPushButton(self)
        self.b_13.setObjectName(u"b_13")
        sizePolicy.setHeightForWidth(
            self.b_13.sizePolicy().hasHeightForWidth())
        self.b_13.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_13)

        self.b_14 = QPushButton(self)
        self.b_14.setObjectName(u"b_14")
        sizePolicy.setHeightForWidth(
            self.b_14.sizePolicy().hasHeightForWidth())
        self.b_14.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_14)

        self.b_15 = QPushButton(self)
        self.b_15.setObjectName(u"b_15")
        sizePolicy.setHeightForWidth(
            self.b_15.sizePolicy().hasHeightForWidth())
        self.b_15.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_15)

        self.b_16 = QPushButton(self)
        self.b_16.setObjectName(u"b_16")
        sizePolicy.setHeightForWidth(
            self.b_16.sizePolicy().hasHeightForWidth())
        self.b_16.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_16)

        self.b_17 = QPushButton(self)
        self.b_17.setObjectName(u"b_17")
        sizePolicy.setHeightForWidth(
            self.b_17.sizePolicy().hasHeightForWidth())
        self.b_17.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_17)

        self.b_18 = QPushButton(self)
        self.b_18.setObjectName(u"b_18")
        sizePolicy.setHeightForWidth(
            self.b_18.sizePolicy().hasHeightForWidth())
        self.b_18.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_18)

        self.b_19 = QPushButton(self)
        self.b_19.setObjectName(u"b_19")
        sizePolicy.setHeightForWidth(
            self.b_19.sizePolicy().hasHeightForWidth())
        self.b_19.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_19)

        self.b_20 = QPushButton(self)
        self.b_20.setObjectName(u"b_20")
        sizePolicy.setHeightForWidth(
            self.b_20.sizePolicy().hasHeightForWidth())
        self.b_20.setSizePolicy(sizePolicy)

        self.h2.addWidget(self.b_20)

        self.verticalLayout.addLayout(self.h2)

        self.h3 = QHBoxLayout()
        self.h3.setSpacing(0)
        self.h3.setObjectName(u"h3")
        self.b_21 = QPushButton(self)
        self.b_21.setObjectName(u"b_21")
        sizePolicy.setHeightForWidth(
            self.b_21.sizePolicy().hasHeightForWidth())
        self.b_21.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_21)

        self.b_22 = QPushButton(self)
        self.b_22.setObjectName(u"b_22")
        sizePolicy.setHeightForWidth(
            self.b_22.sizePolicy().hasHeightForWidth())
        self.b_22.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_22)

        self.b_23 = QPushButton(self)
        self.b_23.setObjectName(u"b_23")
        sizePolicy.setHeightForWidth(
            self.b_23.sizePolicy().hasHeightForWidth())
        self.b_23.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_23)

        self.b_24 = QPushButton(self)
        self.b_24.setObjectName(u"b_24")
        sizePolicy.setHeightForWidth(
            self.b_24.sizePolicy().hasHeightForWidth())
        self.b_24.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_24)

        self.b_25 = QPushButton(self)
        self.b_25.setObjectName(u"b_25")
        sizePolicy.setHeightForWidth(
            self.b_25.sizePolicy().hasHeightForWidth())
        self.b_25.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_25)

        self.b_26 = QPushButton(self)
        self.b_26.setObjectName(u"b_26")
        sizePolicy.setHeightForWidth(
            self.b_26.sizePolicy().hasHeightForWidth())
        self.b_26.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_26)

        self.b_27 = QPushButton(self)
        self.b_27.setObjectName(u"b_27")
        sizePolicy.setHeightForWidth(
            self.b_27.sizePolicy().hasHeightForWidth())
        self.b_27.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_27)

        self.b_28 = QPushButton(self)
        self.b_28.setObjectName(u"b_28")
        sizePolicy.setHeightForWidth(
            self.b_28.sizePolicy().hasHeightForWidth())
        self.b_28.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_28)

        self.b_29 = QPushButton(self)
        self.b_29.setObjectName(u"b_29")
        sizePolicy.setHeightForWidth(
            self.b_29.sizePolicy().hasHeightForWidth())
        self.b_29.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_29)

        self.b_30 = QPushButton(self)
        self.b_30.setObjectName(u"b_30")
        sizePolicy.setHeightForWidth(
            self.b_30.sizePolicy().hasHeightForWidth())
        self.b_30.setSizePolicy(sizePolicy)

        self.h3.addWidget(self.b_30)

        self.verticalLayout.addLayout(self.h3)

        self.h4 = QHBoxLayout()
        self.h4.setSpacing(0)
        self.h4.setObjectName(u"h4")
        self.b_31 = QPushButton(self)
        self.b_31.setObjectName(u"b_31")
        sizePolicy.setHeightForWidth(
            self.b_31.sizePolicy().hasHeightForWidth())
        self.b_31.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_31)

        self.b_32 = QPushButton(self)
        self.b_32.setObjectName(u"b_32")
        sizePolicy.setHeightForWidth(
            self.b_32.sizePolicy().hasHeightForWidth())
        self.b_32.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_32)

        self.b_33 = QPushButton(self)
        self.b_33.setObjectName(u"b_33")
        sizePolicy.setHeightForWidth(
            self.b_33.sizePolicy().hasHeightForWidth())
        self.b_33.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_33)

        self.b_34 = QPushButton(self)
        self.b_34.setObjectName(u"b_34")
        sizePolicy.setHeightForWidth(
            self.b_34.sizePolicy().hasHeightForWidth())
        self.b_34.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_34)

        self.b_35 = QPushButton(self)
        self.b_35.setObjectName(u"b_35")
        sizePolicy.setHeightForWidth(
            self.b_35.sizePolicy().hasHeightForWidth())
        self.b_35.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_35)

        self.b_36 = QPushButton(self)
        self.b_36.setObjectName(u"b_36")
        sizePolicy.setHeightForWidth(
            self.b_36.sizePolicy().hasHeightForWidth())
        self.b_36.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_36)

        self.b_37 = QPushButton(self)
        self.b_37.setObjectName(u"b_37")
        sizePolicy.setHeightForWidth(
            self.b_37.sizePolicy().hasHeightForWidth())
        self.b_37.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_37)

        self.b_38 = QPushButton(self)
        self.b_38.setObjectName(u"b_38")
        sizePolicy.setHeightForWidth(
            self.b_38.sizePolicy().hasHeightForWidth())
        self.b_38.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_38)

        self.b_39 = QPushButton(self)
        self.b_39.setObjectName(u"b_39")
        sizePolicy.setHeightForWidth(
            self.b_39.sizePolicy().hasHeightForWidth())
        self.b_39.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_39)

        self.b_40 = QPushButton(self)
        self.b_40.setObjectName(u"b_40")
        sizePolicy.setHeightForWidth(
            self.b_40.sizePolicy().hasHeightForWidth())
        self.b_40.setSizePolicy(sizePolicy)

        self.h4.addWidget(self.b_40)

        self.verticalLayout.addLayout(self.h4)

        self.ok = QPushButton(self)
        self.ok.setObjectName(u"ok")
        sizePolicy1 = QSizePolicy(
            QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.ok)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        self.setWindowIcon(QIcon("About/Photos/icon.png"))
        self.setWindowTitle("About")

        self.logo.setText(QCoreApplication.translate(
            "Dialog", u"Financial Calculator 7.0", None))
        self.license.setText("")
        self.b_1.setText("")
        self.b_2.setText("")
        self.b_3.setText("")
        self.b_4.setText("")
        self.b_5.setText("")
        self.b_6.setText("")
        self.b_7.setText("")
        self.b_8.setText("")
        self.b_9.setText("")
        self.b_10.setText("")
        self.b_11.setText("")
        self.b_12.setText("")
        self.b_13.setText("")
        self.b_14.setText("")
        self.b_15.setText("")
        self.b_16.setText("")
        self.b_17.setText("")
        self.b_18.setText("")
        self.b_19.setText("")
        self.b_20.setText("")
        self.b_21.setText("")
        self.b_22.setText("")
        self.b_23.setText("")
        self.b_24.setText("")
        self.b_25.setText("")
        self.b_26.setText("")
        self.b_27.setText("")
        self.b_28.setText("")
        self.b_29.setText("")
        self.b_30.setText("")
        self.b_31.setText("")
        self.b_32.setText("")
        self.b_33.setText("")
        self.b_34.setText("")
        self.b_35.setText("")
        self.b_36.setText("")
        self.b_37.setText("")
        self.b_38.setText("")
        self.b_39.setText("")
        self.b_40.setText("")
        self.ok.setText(QCoreApplication.translate("Dialog", u"OK", None))

    # retranslateUi
        self.set_tooltips()
        self.events()
        self.set_images()
        self.set_CSS_style()

    def set_CSS_style(self):
        self.setStyleSheet("""
            QDialog{
                background-color: white;
            }
            QPushButton {
                background-color: white; 
                border: 1px solid white;
                color: black;
                border-radius: 50px;
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
            QPushButton#ok {
                background-color: #ff0000; 
                border: 1px solid black;
                color: black;
                border-radius: 10px;
                font-size: 25px;
                font-weight: bold;
            }
            QPushButton#ok:hover {
                background-color: #fa6666; 
                border: 1px solid black;
                color: black;
                border-radius: 10px;
                font-size: 25px;
                font-weight: bold;
            }
            QPushButton#ok:pressed {
                background-color: #ab0303;
                border: 1px solid black;
                color: black;
                border-radius: 10px;
                font-size: 25px;
                font-weight: bold;
            }
        """)

    def set_tooltips(self):
        self.logo.setToolTip(
            "https://duckduckgo.com/?q=bdshahab+Financial+Calculator")
        self.license.setToolTip("https://creativecommons.org/licenses/by/4.0")
        self.b_1.setToolTip("https://bdshahab.blogspot.com")
        self.b_2.setToolTip("https://bsky.app/profile/bdshahab.bsky.social")
        self.b_3.setToolTip("https://www.chess.com/member/bdshahab1982")
        self.b_4.setToolTip("https://app.clouthub.com/#/users/u/bdshahab")
        self.b_5.setToolTip("https://diamondapp.com/u/bdshahab")
        self.b_6.setToolTip("https://diasp.org/u/bdshahab")
        self.b_7.setToolTip("https://discord.gg/xgMdTXBhnE")
        self.b_8.setToolTip(
            "https://www.facebook.com/shahab.baradaran.dilmaghani")
        self.b_9.setToolTip("https://www.flickr.com/photos/bdshahab")
        self.b_10.setToolTip("https://flipboard.com/@bdshahab1982")
        self.b_11.setToolTip("https://gab.com/bdshahab")
        self.b_12.setToolTip("https://gettr.com/user/bdshahab")
        self.b_13.setToolTip("https://www.instagram.com/bdshahab1982")
        self.b_14.setToolTip("https://bdshahab.itch.io")
        self.b_15.setToolTip("https://justpaste.it/u/bdshahab")
        self.b_16.setToolTip("https://lichess.org/@/bdshahab")
        self.b_17.setToolTip("https://www.linkedin.com/company/bdshahab")
        self.b_18.setToolTip("https://bdshahab1982.livejournal.com")
        self.b_19.setToolTip("https://mastodon.social/@bdshahab")
        self.b_20.setToolTip("https://matrix.to/#/#bdshahab:matrix.org")
        self.b_21.setToolTip("https://bdshahab.medium.com")
        self.b_22.setToolTip("https://mewe.com/bdshahab")
        self.b_23.setToolTip("https://www.minds.com/bdshahab")
        self.b_24.setToolTip("https://odysee.com/@bdshahab")
        self.b_25.setToolTip("https://www.pinterest.com/bdshahab")
        self.b_26.setToolTip(
            "https://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5")
        self.b_27.setToolTip("https://www.reddit.com/user/bdshahab")
        self.b_28.setToolTip("https://rumble.com/c/c-1832445/videos")
        self.b_29.setToolTip("https://spoutible.com/bdshahab")
        self.b_30.setToolTip("https://steemit.com/@bdshahab")
        self.b_31.setToolTip("https://t.me/bd_shahab")
        self.b_32.setToolTip(
            "https://the-dots.com/users/shahab-baradaran-dilmaghani-1291359")
        self.b_33.setToolTip("https://www.threads.net/@bdshahab1982")
        self.b_34.setToolTip("https://www.tiktok.com/@bdshahab")
        self.b_35.setToolTip("https://bdshahab.tumblr.com")
        self.b_36.setToolTip("https://vk.com/bdshahab")
        self.b_37.setToolTip("https://bdsh.wordpress.com")
        self.b_38.setToolTip("https://x.com/bdshahab")
        self.b_39.setToolTip(
            "https://www.xing.com/profile/Shahab_BaradaranDilmaghani")
        self.b_40.setToolTip("https://www.youtube.com/@bdshahab")

    def events(self):
        self.resize(800, 400)
        center_window(self)
        self.ok.clicked.connect(self.close_window)
        self.logo.clicked.connect(lambda: self.open_url(self.logo))

        self.license.clicked.connect(lambda: self.open_url(self.license))
        self.b_1.clicked.connect(lambda: self.open_url(self.b_1))
        self.b_2.clicked.connect(lambda: self.open_url(self.b_2))
        self.b_3.clicked.connect(lambda: self.open_url(self.b_3))
        self.b_4.clicked.connect(lambda: self.open_url(self.b_4))
        self.b_5.clicked.connect(lambda: self.open_url(self.b_5))
        self.b_6.clicked.connect(lambda: self.open_url(self.b_6))
        self.b_7.clicked.connect(lambda: self.open_url(self.b_7))
        self.b_8.clicked.connect(lambda: self.open_url(self.b_8))
        self.b_9.clicked.connect(lambda: self.open_url(self.b_9))
        self.b_10.clicked.connect(lambda: self.open_url(self.b_10))
        self.b_11.clicked.connect(lambda: self.open_url(self.b_11))
        self.b_12.clicked.connect(lambda: self.open_url(self.b_12))
        self.b_13.clicked.connect(lambda: self.open_url(self.b_13))
        self.b_14.clicked.connect(lambda: self.open_url(self.b_14))
        self.b_15.clicked.connect(lambda: self.open_url(self.b_15))
        self.b_16.clicked.connect(lambda: self.open_url(self.b_16))
        self.b_17.clicked.connect(lambda: self.open_url(self.b_17))
        self.b_18.clicked.connect(lambda: self.open_url(self.b_18))
        self.b_19.clicked.connect(lambda: self.open_url(self.b_19))
        self.b_20.clicked.connect(lambda: self.open_url(self.b_20))
        self.b_21.clicked.connect(lambda: self.open_url(self.b_21))
        self.b_22.clicked.connect(lambda: self.open_url(self.b_22))
        self.b_23.clicked.connect(lambda: self.open_url(self.b_23))
        self.b_24.clicked.connect(lambda: self.open_url(self.b_24))
        self.b_25.clicked.connect(lambda: self.open_url(self.b_25))
        self.b_26.clicked.connect(lambda: self.open_url(self.b_26))
        self.b_27.clicked.connect(lambda: self.open_url(self.b_27))
        self.b_28.clicked.connect(lambda: self.open_url(self.b_28))
        self.b_29.clicked.connect(lambda: self.open_url(self.b_29))
        self.b_30.clicked.connect(lambda: self.open_url(self.b_30))
        self.b_31.clicked.connect(lambda: self.open_url(self.b_31))
        self.b_32.clicked.connect(lambda: self.open_url(self.b_32))
        self.b_33.clicked.connect(lambda: self.open_url(self.b_33))
        self.b_34.clicked.connect(lambda: self.open_url(self.b_34))
        self.b_35.clicked.connect(lambda: self.open_url(self.b_35))
        self.b_36.clicked.connect(lambda: self.open_url(self.b_36))
        self.b_37.clicked.connect(lambda: self.open_url(self.b_37))
        self.b_38.clicked.connect(lambda: self.open_url(self.b_38))
        self.b_39.clicked.connect(lambda: self.open_url(self.b_39))
        self.b_40.clicked.connect(lambda: self.open_url(self.b_40))

    def open_url(self, the_button):
        webbrowser.open(the_button.toolTip())

    def set_images(self):
        ico_size = img_size - img_size // 3

        show_image([self.logo],
                   [r"About\Photos\icon.png"],
                   [(ico_size, ico_size)])
        show_image([self.license],
                   [r"About\Photos\license.png"],
                   [(4 * img_size, img_size)])
        show_image([self.b_1],
                   [r"About\Photos\social media\blogger.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_2],
                   [r"About\Photos\social media\blue_sky.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_3],
                   [r"About\Photos\social media\chess_com.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_4],
                   [r"About\Photos\social media\clouthub.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_5],
                   [r"About\Photos\social media\diamondapp.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_6],
                   [r"About\Photos\social media\diaspora.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_7],
                   [r"About\Photos\social media\discord.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_8],
                   [r"About\Photos\social media\facebook.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_9],
                   [r"About\Photos\social media\flickr.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_10],
                   [r"About\Photos\social media\flipboard.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_11],
                   [r"About\Photos\social media\gab.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_12],
                   [r"About\Photos\social media\gettr.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_13],
                   [r"About\Photos\social media\instagram.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_14],
                   [r"About\Photos\social media\itch_io.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_15],
                   [r"About\Photos\social media\justpaste_it.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_16],
                   [r"About\Photos\social media\lichess.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_17],
                   [r"About\Photos\social media\linkedin.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_18],
                   [r"About\Photos\social media\livejournal.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_19],
                   [r"About\Photos\social media\Mastodon.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_20],
                   [r"About\Photos\social media\matrix.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_21],
                   [r"About\Photos\social media\medium.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_22],
                   [r"About\Photos\social media\mewe.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_23],
                   [r"About\Photos\social media\minds.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_24],
                   [r"About\Photos\social media\odysee.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_25],
                   [r"About\Photos\social media\pinterest.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_26],
                   [r"About\Photos\social media\primal.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_27],
                   [r"About\Photos\social media\reddit.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_28],
                   [r"About\Photos\social media\rumble.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_29],
                   [r"About\Photos\social media\spoutible.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_30],
                   [r"About\Photos\social media\steemit.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_31],
                   [r"About\Photos\social media\telegram.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_32],
                   [r"About\Photos\social media\the_dots.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_33],
                   [r"About\Photos\social media\threads.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_34],
                   [r"About\Photos\social media\tiktok.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_35],
                   [r"About\Photos\social media\tumblr.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_36],
                   [r"About\Photos\social media\vk.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_37],
                   [r"About\Photos\social media\wordpress.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_38],
                   [r"About\Photos\social media\x.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_39],
                   [r"About\Photos\social media\xing.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_40],
                   [r"About\Photos\social media\youtube.png"],
                   [(ico_size, ico_size)])

    def close_window(self):
        self.close()
