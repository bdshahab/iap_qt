from enum import Enum

user_bought = False
selected_payment = ""
img_size = 0
TOTAL_TIME = 15 * 60
screen_width = 0
screen_height = 0


class NextWindow(Enum):
    MAIN = 0
    UI_SELECT_COIN = 1
    UI_PAYMENT = 2
    UI_BOUGHT = 3
    UI_ABOUT = 4


# Usage
next_window = NextWindow.MAIN
