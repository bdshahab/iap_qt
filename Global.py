from enum import Enum


class NextWindow(Enum):
    MAIN = 0
    UI_SELECT_COIN = 1
    UI_PAYMENT = 2
    UI_BOUGHT = 3
    UI_ABOUT = 4


next_window = NextWindow.MAIN
user_bought = False
selected_payment = ""
img_size = 0
screen_width = 0
screen_height = 0
