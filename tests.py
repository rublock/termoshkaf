import subprocess
import sys

from PyQt6.QtWidgets import QTableWidgetItem


def write_registers_func(table):
    try:
        result = subprocess.run(
            [sys.executable, 'write_registers.py'], capture_output=True, text=True, check=True
        )
        item = QTableWidgetItem(result.stdout)
        # куда отправляются данные
        table.setItem(0, 3, item)
        table.resizeColumnsToContents()
        table.resizeRowsToContents()

    except subprocess.CalledProcessError as e:
        print(f"Ошибка при выполнении файла: {e}")
        print(e.stderr)
        table.setItem(0, 3, QTableWidgetItem("Ошибка выполнения."))

    except FileNotFoundError:
        print("Файл не найден. Проверьте путь.")
        table.setItem(0, 3, QTableWidgetItem("Файл не найден."))
