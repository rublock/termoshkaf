import subprocess
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidget, \
    QGridLayout, QTableWidgetItem, QPushButton, QHBoxLayout, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 400)
        self.setWindowTitle("Тестирование REM")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout(self)
        central_widget.setLayout(grid_layout)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(1)

        self.table.setHorizontalHeaderLabels(["", "Значения", "Установки", "Заметки"])

        read_button = QPushButton("Чтение")
        test_button = QPushButton("Тест")
        read_button.clicked.connect(self.click_handler)

        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button_layout.addWidget(read_button)
        button_layout.addWidget(test_button)
        button_widget.setLayout(button_layout)

        # Set the button widget in the table cell (0, 0)
        self.table.setCellWidget(0, 0, button_widget)

        self.table.setItem(0, 1, QTableWidgetItem(" " * 50))
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.table.setItem(0, 3, QTableWidgetItem("Text in column 4"))

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        grid_layout.addWidget(self.table, 0, 0)

    def click_handler(self):
        file_to_run = 'read_registers.py'

        try:
            result = subprocess.run([sys.executable, file_to_run], capture_output=True, text=True, check=True)

            output = result.stdout
            result_output = ''

            for line in output.splitlines():
                if line.startswith("HT3:") or line.startswith("HTR:"):
                    result_output += f'{line} + \n'

            self.table.setItem(0, 1, QTableWidgetItem(result_output.strip()))

        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении файла: {e}")
            print(e.stderr)
            self.table.setItem(0, 1, QTableWidgetItem("Ошибка выполнения."))

        except FileNotFoundError:
            print("Файл не найден. Проверьте путь.")
            self.table.setItem(0, 1, QTableWidgetItem("Файл не найден."))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
