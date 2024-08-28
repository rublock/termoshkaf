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
    QHBoxLayout,
    QLineEdit,
)

from get_data_from_read_registers import read_registers_func
import write_registers

from config import configuration_1 as config_1
from config import configuration_2 as config_2
from config import configuration_3 as config_3
from config import configuration_4 as config_4
from config import configuration_5 as config_5
from config import configuration_6 as config_6
from config import configuration_7 as config_7

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

        self.table.setHorizontalHeaderLabels([
            "",
            "Cчитанные значения",
            "Записанные установки",
            "Значения для записи"
        ])

        self.table.setItem(0, 1, QTableWidgetItem())
        self.table.setItem(0, 2, QTableWidgetItem())
        self.table.setItem(0, 3, QTableWidgetItem())

        # подготовка кнопок
        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button_widget.setLayout(button_layout)
        self.table.setCellWidget(0, 0, button_widget)

        # кнопки в первой колонке
        read_button = QPushButton("Чтение")
        button_layout.addWidget(read_button)
        read_button.clicked.connect(lambda: read_registers_func(self.table))

        # TODO продумать как изменять данные в конфиге пользователем!!!
        test_heat = QPushButton("Тест нагрева")
        button_layout.addWidget(test_heat)
        test_heat.clicked.connect(lambda: write_registers.main(config_1))

        test_fan = QPushButton("Тест вентиляции")
        button_layout.addWidget(test_fan)
        test_fan.clicked.connect(lambda:  write_registers.main(config_2))

        # поле ввода и кнопка отправки в третьей колонке
        input_widget = QWidget()
        input_layout = QHBoxLayout(input_widget)
        input_widget.setLayout(input_layout)

        input_field = QLineEdit()
        input_layout.addWidget(input_field)

        send_button = QPushButton("Отправить")
        input_layout.addWidget(send_button)

        self.table.setCellWidget(0, 3, input_widget)
        send_button.clicked.connect(lambda: self.handle_input(input_field))

        # Подгоняем ячейку под размер контента
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        # # таймер для вызова функции считывания данных
        # self.timer = QTimer()
        # self.timer.timeout.connect(lambda: read_registers_func(self.table))
        # self.timer.start(1000)

    def handle_input(self, input_field):
        input_text = input_field.text()
        print(f"Введенные данные: {input_text}")

    # TODO сделать один конфигурационный файл и подменять в нем значения в зависимости от вида теста
    # TODO забирать значения не из stdout, а сразу переменные из функции


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
