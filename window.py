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
        grid_layout = QGridLayout(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(grid_layout)


        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setRowCount(1)
        grid_layout.addWidget(self.table, 0, 0)

        self.table.setHorizontalHeaderLabels(["", "Значения", "Установки", "Заметки"])

        self.table.setItem(0, 1, QTableWidgetItem())
        self.table.setItem(0, 2, QTableWidgetItem("Text in column 3"))
        self.table.setItem(0, 3, QTableWidgetItem("Text in column 4"))

        # подготовка кнопок
        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button_widget.setLayout(button_layout)
        self.table.setCellWidget(0, 0, button_widget)

        # кнопки в первой колонке
        read_button = QPushButton("Чтение")
        button_layout.addWidget(read_button)
        read_button.clicked.connect(lambda: read_registers_func(self.table))

        test_heat = QPushButton("Тест нагрева")
        button_layout.addWidget(test_heat)
        test_heat.clicked.connect(lambda: write_registers_func(self.table))

        # подгоняем ячейку под размер контента
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        # # таймер для вызова функции считывания данных
        # self.timer = QTimer()
        # self.timer.timeout.connect(lambda: read_registers_func(self.table))
        # self.timer.start(1000)

    # TODO сделать один конфигурационный файл и подменять в нем значения в зависимости от вида теста
    # TODO забирать значения не из stdout, а сразу переменные из функции


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
