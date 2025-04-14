import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QPushButton,
    QSystemTrayIcon,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

app = QApplication(sys.argv)
active_notewindows = {}



class NoteWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            self.windowFlags()
            | Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
        )
        
        self.setStyleSheet(
            "background: lightblue; color: black; border: 0; font-size: 14pt;"
        )
        
        layout = QVBoxLayout()

        buttons = QHBoxLayout()
        self.close_btn = QPushButton("×")
        self.close_btn.setStyleSheet(
            "font-weight: bold; font-size: 20px; width: 20px; height: 20px;"
        )
        
        self.close_btn.clicked.connect(self.close)
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        buttons.addStretch()
        buttons.addWidget(self.close_btn)
        layout.addLayout(buttons)

        self.text = QTextEdit()
        layout.addWidget(self.text)
        self.setLayout(layout)

        active_notewindows[id(self)] = self

    def mousePressEvent(self, e):
        self.previous_pos = e.globalPosition()

    def mouseMoveEvent(self, e):
        delta = e.globalPosition() - self.previous_pos
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previous_pos = e.globalPosition()
def create_notewindow():
    note = NoteWindow()
    note.show()

create_notewindow()
create_notewindow()

icon = QIcon("1.png")


tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)


def handle_tray_click(reason):

    if (
        QSystemTrayIcon.ActivationReason(reason)
        == QSystemTrayIcon.ActivationReason.Trigger
    ):
        create_notewindow()

tray.activated.connect(handle_tray_click)

app.exec()
