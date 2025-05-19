from PySide6.QtWidgets import QApplication
import os
import sys


# set window in the center
def center_window(window):  # type: ignore
    sys.path.append(os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')))
    import Global

    screen_geometry = QApplication.primaryScreen().availableGeometry()
    Global.screen_height = screen_geometry.height()
    Global.screen_width = screen_geometry.width()

    if Global.screen_height < Global.screen_width:
        Global.img_size = Global.screen_height // 8
    else:
        Global.img_size = Global.screen_width // 8

    # Resize the window to 75% of screen size
    new_width = int(Global.screen_width * 0.75)
    new_height = int(Global.screen_height * 0.75)
    window.resize(new_width, new_height)  # type: ignore
