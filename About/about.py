from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (
    QDialog, QHBoxLayout, QLayout, QPushButton, QSizePolicy, QVBoxLayout)

from tools.Centralization import center_window
from tools.for_images import show_image
import webbrowser
import requests
from Payment.web_functions import GITHUB

import Global


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
            "Dialog", u"IAP by Cryptocurrency", None))
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
        self.init()
        self.update_links()
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

    def init(self):
        self.link_logo = "https://duckduckgo.com/?q=bdshahab"
        self.link_license = "https://opensource.org/license/mit"
        self.link_b_1 = "https://www.aparat.com/bdshahab"
        self.link_b_2 = "https://www.apsense.com/user/bdshahab"
        self.link_b_3 = "https://bdshahab.blogspot.com"
        self.link_b_4 = "https://bdshahab.blogix.ir"
        self.link_b_5 = "https://bsky.app/profile/bdshahab.bsky.social"
        self.link_b_6 = "https://diamondapp.com/u/bdshahab"
        self.link_b_7 = "https://discord.gg/xgMdTXBhnE"
        self.link_b_8 = "https://www.facebook.com/bdshahab1982"
        self.link_b_9 = "https://flipboard.com/@bdshahab1982"
        self.link_b_10 = "https://forem.com/bdshahab"
        self.link_b_11 = "https://gettr.com/user/bdshahab"
        self.link_b_12 = "https://hashnode.com/@bdshahab"
        self.link_b_13 = "https://www.instagram.com/bdshahab1982"
        self.link_b_14 = "https://bdshahab.itch.io"
        self.link_b_15 = "https://justpaste.it/u/bdshahab"
        self.link_b_16 = "https://www.linkedin.com/company/bdshahab"
        self.link_b_17 = "https://bdshahab1982.livejournal.com"
        self.link_b_18 = "https://lnk.bio/bdshahab"
        self.link_b_19 = "https://mastodon.social/@bdshahab"
        self.link_b_20 = "https://matrix.to/#/#bdshahab:matrix.org"
        self.link_b_21 = "https://bdshahab.medium.com"
        self.link_b_22 = "https://mewe.com/bdshahab"
        self.link_b_23 = "https://www.minds.com/bdshahab"
        self.link_b_24 = "https://odysee.com/@bdshahab"
        self.link_b_25 = "https://app.parler.com/bdshahab"
        self.link_b_26 = "https://www.pinterest.com/bdshahab"
        self.link_b_27 = "https://primal.net/p/npub1lu5m9cjqnyaqay0uc77t526qjtkx5qu8qxe8l2kqrflmagac3c8q7g8nu5"
        self.link_b_28 = "https://www.producthunt.com/@bdshahab"
        self.link_b_29 = "https://spoutible.com/bdshahab"
        self.link_b_30 = "https://steemit.com/@bdshahab"
        self.link_b_31 = "https://t.me/bd_shahab"
        self.link_b_32 = "https://www.threads.com/@bdshahab1982"
        self.link_b_33 = "https://www.tiktok.com/@bdshahab1982"
        self.link_b_34 = "https://bdshahab.tumblr.com"
        self.link_b_35 = "https://vk.com/bdshahab"
        self.link_b_36 = "https://whatsapp.com/channel/0029VbBIpNP1XquP4Lz4eZ3M"
        self.link_b_37 = "https://bdsh.wordpress.com"
        self.link_b_38 = "https://x.com/bdshahab"
        self.link_b_39 = "https://www.xing.com/profile/Shahab_BaradaranDilmaghani"
        self.link_b_40 = "https://www.youtube.com/@bdshahab"

    def update_links(self):
        try:
            LINKS_SITE = GITHUB + "links.txt"
            response = requests.get(LINKS_SITE)
            # response.raise_for_status()  # Raise an error for bad status codes
            the_result = response.text
            list_of_links = []

            for line in the_result.split("\n"):
                list_of_links.append(line)

            self.logo.setToolTip(f"{list_of_links[0]} {self.logo.text()}")
            self.license.setToolTip(self.link_license)

            for i in range(1, 41):
                getattr(self, f"b_{i}").setToolTip(list_of_links[i + 1])
        except Exception:
            self.set_tooltips()

    def set_tooltips(self):
        self.logo.setToolTip(f"{self.link_logo} {self.logo.text()}")
        self.license.setToolTip(self.link_license)

        for i in range(1, 41):
            btn = getattr(self, f"b_{i}")
            link = getattr(self, f"link_b_{i}")
            btn.setToolTip(link)

    def events(self):
        self.setMinimumSize(100, 1)
        self.resize(Global.screen_width * 0.75, Global.screen_height * 0.75)
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
        ico_size = Global.img_size - Global.img_size // 3

        show_image([self.logo],
                   [r"About\Photos\icon.png"],
                   [(ico_size, ico_size)])
        show_image([self.license],
                   [r"About\Photos\license.png"],
                   [(Global.img_size, Global.img_size)])
        show_image([self.b_1],
                   [r"About\Photos\social media\aparat.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_2],
                   [r"About\Photos\social media\apsense.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_3],
                   [r"About\Photos\social media\blogger.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_4],
                   [r"About\Photos\social media\blogix.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_5],
                   [r"About\Photos\social media\blue_sky.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_6],
                   [r"About\Photos\social media\diamondapp.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_7],
                   [r"About\Photos\social media\discord.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_8],
                   [r"About\Photos\social media\facebook.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_9],
                   [r"About\Photos\social media\flipboard.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_10],
                   [r"About\Photos\social media\forem.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_11],
                   [r"About\Photos\social media\gettr.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_12],
                   [r"About\Photos\social media\hashnode.png"],
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
                   [r"About\Photos\social media\linkedin.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_17],
                   [r"About\Photos\social media\livejournal.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_18],
                   [r"About\Photos\social media\lnk_bio.png"],
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
                   [r"About\Photos\social media\parler.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_26],
                   [r"About\Photos\social media\pinterest.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_27],
                   [r"About\Photos\social media\primal.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_28],
                   [r"About\Photos\social media\producthunt.png"],
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
                   [r"About\Photos\social media\threads.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_33],
                   [r"About\Photos\social media\tiktok.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_34],
                   [r"About\Photos\social media\tumblr.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_35],
                   [r"About\Photos\social media\vk.png"],
                   [(ico_size, ico_size)])
        show_image([self.b_36],
                   [r"About\Photos\social media\whatsapp.png"],
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
