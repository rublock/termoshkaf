import sys

from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QMainWindow,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from read import read_registers_func
from tests import write_registers_func


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)
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
        read_button.clicked.connect(lambda: read_registers_func(self.table))
        test_heat = QPushButton("Тест нагревателя")
        test_heat.clicked.connect(lambda: write_registers_func(self.table))

        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button_layout.addWidget(read_button)
        button_layout.addWidget(test_heat)
        button_widget.setLayout(button_layout)

        self.table.setCellWidget(0, 0, button_widget)

        self.table.setItem(0, 1, QTableWidgetItem())
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.table.setItem(0, 3, QTableWidgetItem("Text in column 4"))

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        grid_layout.addWidget(self.table, 0, 0)

        self.timer = QTimer()
        self.timer.timeout.connect(lambda: read_registers_func(self.table))
        self.timer.start(1000)

    # TODO сделать один конфигурационный файл и подменять в нем значения в зависимости от вида теста
    # TODO забирать значения не из stdout а сразу переменные из функции


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
