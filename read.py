import subprocess
import sys

from PyQt6.QtWidgets import QTableWidgetItem


def read_registers_func(table):
    try:
        result = subprocess.run(
            [sys.executable, 'read_registers.py'], capture_output=True, text=True, check=True
        )
        start_index = result.stdout.find("***Current values***")
        end_index = result.stdout.find("***Registers data***", start_index)
        result_text = result.stdout[start_index:end_index].strip()

        item = QTableWidgetItem(result_text)
        table.setItem(0, 2, item)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()


    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении файла: {e}")
        print(e.stderr)
        table.setItem(0, 2, QTableWidgetItem("Ошибка выполнения."))

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь.")
        table.setItem(0, 2, QTableWidgetItem("Файл не найден."))
