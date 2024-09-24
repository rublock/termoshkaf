from PyQt6.QtWidgets import QMessageBox

import config
import write_registers

from config import configuration_base as config_base


def modal_dialog_func(table, config_name):
    """
    Модальные окна после окончания теста
    """
    ask_msg_box = QMessageBox()
    ask_msg_box.setWindowTitle("Результат теста")
    ask_msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    break_msg_box = QMessageBox()
    break_msg_box.setWindowTitle("Информация")
    break_msg_box.setText("Возвращено к исходным значениям.")
    break_msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)

    completed_msg_box = QMessageBox()
    completed_msg_box.setWindowTitle("Информация")
    completed_msg_box.setText("Тест запущен.")
    completed_msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    completed_msg_box.button(QMessageBox.StandardButton.Ok).setText("Завершить")

    cycle_completed = False

    if isinstance(config_name, list):
        write_registers.main(table, getattr(config, config_name[1]))
        completed_msg_box.exec()
        write_registers.main(table, config_base)

    elif isinstance(config_name, dict):
        for k, v in config_name.items():
            write_registers.main(table, getattr(config, v[1]))
            ask_msg_box.setText(f'{k} пройден?')
            result = ask_msg_box.exec()
            if result == QMessageBox.StandardButton.No:
                write_registers.main(table, config_base)
                break_msg_box.exec()
                break
        else:
            cycle_completed = True

        if cycle_completed:
            write_registers.main(table, config_base)
            break_msg_box.exec()
