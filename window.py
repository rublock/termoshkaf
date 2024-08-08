from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QCheckBox, QButtonGroup, \
    QLabel


def click_handler():
    print("Button clicked!")


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 150)

        parent_layout = QVBoxLayout()

        self.label = QLabel("Тестировать устройство")
        self.button = QPushButton("Пуск")

        self.button.clicked.connect(click_handler)

        parent_layout.addWidget(self.label)
        parent_layout.addWidget(self.button)

        center_widget = QWidget()
        center_widget.setLayout(parent_layout)
        self.setCentralWidget(center_widget)


app = QApplication([])
window = Window()

window.show()
app.exec()
