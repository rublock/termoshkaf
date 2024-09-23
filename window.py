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

from get_data_from_read_registers import get_read_registers
import write_registers
from modal_dialog import modal_dialog_func

from config import configuration_base as config_base
from config import configuration_heat as config_heat
from config import configuration_fan as config_fan
from config import configuration_heathym as config_heathym
from config import configuration_overheat as config_overheat
from config import configuration_overcool as config_overcool
from config import configuration_overhym as config_overhym
from config import configuration_individ as config_individ


config_dict = {
    'Тест нагрева': ['Тест нагрева', 'configuration_heat'],
    'Тест вентиляции': ['Тест вентиляции', 'configuration_fan'],
    'Тест по влаге': ['Тест по влаге', 'configuration_heathym'],
    'Тест перегрева': ['Тест перегрева', 'configuration_overheat'],
    'Тест переохлаждения': ['Тест переохлаждения', 'configuration_overcool'],
    'Тест защиты высокой влажности': ['Тест защиты высокой влажности', 'configuration_overhym'],
}


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
        self.table.setColumnCount(3)
        self.table.setRowCount(1)
        grid_layout.addWidget(self.table, 0, 0)

        self.table.setHorizontalHeaderLabels([
            "                        ",
            "            Текущие показатели              ",
            "            Текущие установки            ",
        ])

        # Скрыть номера строк
        self.table.verticalHeader().setVisible(False)

        self.table.setItem(0, 1, QTableWidgetItem())
        self.table.setItem(0, 2, QTableWidgetItem())
        self.table.setItem(0, 3, QTableWidgetItem())

        # Подготовка кнопок
        button_widget = QWidget()
        button_layout = QVBoxLayout(button_widget)
        button_widget.setLayout(button_layout)
        self.table.setCellWidget(0, 0, button_widget)

        # Кнопки в первой колонке
        read_button = QPushButton("Авточтение")
        button_layout.addWidget(read_button)
        read_button.clicked.connect(lambda: auto_read(self))

        test_start = QPushButton("Базовые настройки")
        button_layout.addWidget(test_start)
        test_start.clicked.connect(lambda: write_registers.main(self.table, config_base))

        auto_test = QPushButton("Автотест")
        button_layout.addWidget(auto_test)
        auto_test.clicked.connect(lambda: modal_dialog_func(self.table, config_dict))

        test_heat = QPushButton("Тест нагрева")
        button_layout.addWidget(test_heat)
        test_heat.clicked.connect(lambda: modal_dialog_func(self.table, config_dict['Тест нагрева']))

        test_fan = QPushButton("Тест вентиляции")
        button_layout.addWidget(test_fan)
        test_fan.clicked.connect(lambda: modal_dialog_func(self.table, config_dict['Тест вентиляции']))

        test_humidity = QPushButton("Тест по влаге")
        button_layout.addWidget(test_humidity)
        test_humidity.clicked.connect(lambda: modal_dialog_func(self.table, config_dict['Тест по влаге']))

        test_overheat = QPushButton("Тест перегрева")
        button_layout.addWidget(test_overheat)
        test_overheat.clicked.connect(lambda: modal_dialog_func(self.table, config_dict['Тест перегрева']))

        test_overcool = QPushButton("Тест переохлаждения")
        button_layout.addWidget(test_overcool)
        test_overcool.clicked.connect(lambda: modal_dialog_func(self.table, config_dict['Тест переохлаждения']))

        test_high_humidity = QPushButton("Тест защиты высокой влажности")
        button_layout.addWidget(test_high_humidity)
        test_high_humidity.clicked.connect(lambda: modal_dialog_func(self.table, config_dict['Тест защиты высокой влажности']))

        test_individual = QPushButton("Индивидуальный тест")
        button_layout.addWidget(test_individual)
        test_individual.clicked.connect(lambda: write_registers.main(self.table, config_individ))

        # Устанавливаем таблицу как центральный виджет
        self.setCentralWidget(self.table)

        # Настраиваем размеры строк и столбцов в соответствии с содержимым
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

        # Автоматическое считывание данных
        def auto_read(self):
            self.timer = QTimer()
            self.timer.timeout.connect(lambda: get_read_registers(self.table))
            self.timer.start(5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec())
