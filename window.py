import subprocess
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600, 600)

        parent_layout = QVBoxLayout()

        self.label = QLabel("Тестировать устройство")
        self.button = QPushButton("Пуск")

        self.button.clicked.connect(self.click_handler)

        parent_layout.addWidget(self.label)
        parent_layout.addWidget(self.button)

        center_widget = QWidget()
        center_widget.setLayout(parent_layout)
        self.setCentralWidget(center_widget)

    def click_handler(self):

        file_to_run = 'read_registers.py'

        try:
            result = subprocess.run([sys.executable, file_to_run], capture_output=True, text=True, check=True)

            output = result.stdout
            self.label.setText(output)

        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении файла: {e}")
            print(e.stderr)
        except FileNotFoundError:
            print("Файл не найден. Проверьте путь.")


app = QApplication([])
window = Window()

window.show()
app.exec()
