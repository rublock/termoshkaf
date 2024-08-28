import subprocess
import sys

from PyQt6.QtWidgets import QTableWidgetItem


def read_registers_func(table):
    try:
        read_registers_stdout = subprocess.run(
            [sys.executable, 'read_registers.py'], capture_output=True, text=True, check=True
        )

        read_registers_stdout_splited = read_registers_stdout.stdout.strip().split('\n')

        strings_to_show_dict = {
            "T1, state:": "Value of T_DS1_STATE",
            "T1, ºС:": "Value of T_DS1_VALUE",
            "T2, state:": "Value of T_DS2_STATE",
            "T2, ºС:": "Value of T_DS2_VALUE",
            "TH, state:": "Value of TH_STATE",
            "TH, ºС:": "Value of TH_TEMP_VALUE",
            "TH, %:": "Value of TH_HUMID_VALUE",
            "Оборудование:": "Value of ACTIVE_STATE",
            "Нагрев:": "Value of HEAT_STATE",
            "Вентиляция:": "Value of FAN_STATE",
            "Перегрев:": "Value of ALARM_FLAG_HI",
            "Переохлаждение:": "Value of ALARM_FLAG_LOW",
        }

        result_list = list()

        for line in read_registers_stdout_splited:
            for key, value in strings_to_show_dict.items():
                if line.startswith(value):
                    int_value = int(line.split(': ')[1])
                    int_value = int_value / 10 if int_value > 99 else int_value
                    result_list.append(f'{key} {int_value}') # можно добавить текст к значениям
                    break

        result_list_wraped = "\n".join(result_list)

        item = QTableWidgetItem(result_list_wraped)
        table.setItem(0, 1, item)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении файла: {e}")
        print(e.stderr)
        table.setItem(0, 1, QTableWidgetItem("Ошибка выполнения."))

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь.")
        table.setItem(0, 1, QTableWidgetItem("Файл не найден."))
