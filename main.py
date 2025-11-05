import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt

class BorderlessWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Borderless Window")

        # Set fixed window size (250x122 pixels)
        self.setFixedSize(250, 122)

        # Remove window border (title bar, buttons, etc.)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)

        # Optional: Make the window stay on top of others
        # self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        # Optional: Add a label or widget to the window
        # from PyQt5.QtWidgets import QLabel
        # label = QLabel("This is a borderless window!", self)
        # label.move(50, 50)

# Create the application
app = QApplication(sys.argv)

# Create and show the window
window = BorderlessWindow()
window.show()

# Start the application event loop
sys.exit(app.exec_())
