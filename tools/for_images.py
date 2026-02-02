import base64
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QLabel, QPushButton

def show_image(image_label_list, image_path_list, image_size_list, flip_modes=None):
    """
    Display images with optional flipping using QImage for transformations.
    In last parameter(flip_modes):
    Use 'h' for flipping horizontally
    Use 'v' for flipping vertically
    Use 'both' for flipping both directions (horizontally and vertically)
    """
    # Input validation (same as before)
    if not (len(image_label_list) == len(image_path_list) == len(image_size_list)):
        raise ValueError("All input lists must be of the same length.")
    if flip_modes is not None and len(flip_modes) != len(image_path_list):
        raise ValueError(
            "flip_modes list must match the length of other lists.")
    flip_modes = flip_modes or [None] * len(image_path_list)

    for i in range(len(image_path_list)):
        data = image_path_list[i]

        # Check if it's a base64 string (very basic check)
        # common PNG/JPEG starts
        if isinstance(data, str) and data.strip().startswith(('iVBOR', '/9j/')):
            try:
                image_bytes = base64.b64decode(data)
                pixmap = QPixmap()
                pixmap.loadFromData(image_bytes)
            except Exception:
                # "Error loading base64 image
                image_label_list[i].setText("")
                continue
        else:
            # Assume it's a normal file path
            pixmap = QPixmap(data)

        if pixmap.isNull():
            image_label_list[i].setText("")
            continue

        # Scale first
        scaled_pixmap = pixmap.scaled(
            QSize(*image_size_list[i]),
            Qt.AspectRatioMode.IgnoreAspectRatio,
            Qt.SmoothTransformation
        )

        # Apply flipping using QImage
        flip_mode = flip_modes[i]
        if flip_mode:
            horizontal = flip_mode in ('h', 'both')
            vertical = flip_mode in ('v', 'both')

            # Convert to QImage for flipping
            image = scaled_pixmap.toImage()
            mirrored_image = image.mirrored(
                horizontal, vertical)  # Positional arguments
            scaled_pixmap = QPixmap.fromImage(mirrored_image)

        # Set to widget (same as before)
        if isinstance(image_label_list[i], QPushButton):
            scaled_size = calculate_scaled_size(
                pixmap.size(), image_size_list[i])
            image_label_list[i].setIcon(QIcon(scaled_pixmap))
            image_label_list[i].setIconSize(scaled_size)
        elif isinstance(image_label_list[i], QLabel):
            image_label_list[i].setPixmap(scaled_pixmap)

def calculate_scaled_size(original_size, target_size):
    """Calculate scaled size maintaining aspect ratio (for button icons)."""
    original_width, original_height = original_size.width(), original_size.height()
    target_width, target_height = target_size
    aspect_ratio = original_width / original_height

    if target_width / target_height >= aspect_ratio:
        scaled_height = target_height
        scaled_width = int(aspect_ratio * scaled_height)
    else:
        scaled_width = target_width
        scaled_height = int(scaled_width / aspect_ratio)

    return QSize(scaled_width, scaled_height)
