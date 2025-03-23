from PySide6.QtWidgets import QApplication


def center_window(window):
    # set window in the center
    from PySide6.QtGui import QScreen
    screen_geometry = QScreen.availableGeometry(
        QApplication.primaryScreen())
    screen_center = screen_geometry.center()
    geo = window.frameGeometry()
    geo.moveCenter(screen_center)
    window.move(geo.topLeft())
