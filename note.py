
import sys

from PyQt5.QtGui import QIcon

from PySide6.QtWidgets import QApplication,QTextEdit, QVBoxLayout,QWidget,QPushButton,QHBoxLayout
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

class NotesWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(
            self.windowFlags()
            |Qt.WindowType.FramelessWindowHint


            |Qt.WindowType.WindowStaysOnTopHint
        )
        self.setStyleSheet(
            "background:#FFFF99;color:black;border-radius:5px;font-size:14px;")
        layout = QVBoxLayout()
        buttons=QHBoxLayout()
        self.close_btn = QPushButton("x")
        self.close_btn.setStyleSheet(
            "font-weight:bold;font-size:14;width: 14px;height:14px;"
        )
        self.close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.close_btn.clicked.connect(self.close)
        buttons.addStretch()
        buttons.addWidget(self.close_btn)
        layout.addWidget(self.close_btn)
        layout.addLayout(buttons)

        self.textEdit = QTextEdit()
        layout.addWidget(self.textEdit)
        self.setLayout(layout)

    def mousePressEvent(self, event):
        self.previous_position = event.globalPosition()
    def mouseMoveEvent(self, event):
        delta = event.globalPosition() - self.previous_position
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.previous_position = event.globalPosition()
def create_notewindow():
    note = NotesWindow()
    note.show()
create_notewindow()

app.exec()
