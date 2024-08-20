import json
import time
import typing
from typing import List

import minimalmodbus

from config import configuration_1 as config


def my_modbus_worker(func, args):
    attempts_counter: int = 0

    while attempts_counter <= config.ATTEMPTS_TO_MODBUS_CONNECTIONS:
        try:
            return func(**args)
        except Exception as err:
            attempts_counter += 1
            time.sleep(config.WRITE_MODBUS_TIMEOUT)

    return False


def get_t1(Thermostat) -> List[int]:
    return my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("T_DS1_VALUE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )


def get_t2(Thermostat) -> List[int]:
    return my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("T_DS2_VALUE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )


def get_ht3_humid(Thermostat) -> List[int]:
    return my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("TH_HUMID_VALUE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )


def get_ht3_temp(Thermostat) -> List[int]:
    return my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("TH_TEMP_VALUE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )


def get_htr(Thermostat) -> str:
    htr_condition = my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("HEAT_STATE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )
    if htr_condition[0]:
        return "ON"
    else:
        return "OFF"


def get_fan(Thermostat) -> str:
    fan_condition = my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("FAN_STATE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )
    if fan_condition[0]:
        return "ON"
    else:
        return "OFF"


def get_ae(Thermostat) -> str:
    ae_condition = my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("ACTIVE_STATE"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    )
    if ae_condition[0]:
        return "ON"
    else:
        return "FALSE"


def get_sw_version(Thermostat) -> str:
    if version := my_modbus_worker(
        func=Thermostat.read_registers,
        args={
            "registeraddress": int(
                config.REGISTER_MAP.get("INPUT_REGISTERS").get("VERSION_SW"), 16
            ),
            "number_of_registers": 1,
            "functioncode": 4,
        },
    ):
        return f"{version[0] // 256}.{version[0] % 256}"


def convert_to_signed(value):
    """Преобразует u_int в int"""
    if value >= 0x8000:
        value -= 0x10000
    return value


def main():
    """
    Читаем регистры термостата по адресу: THERMOSTAT_ADDR, используя COM порт: THERMOSTAT_PORT
    Все регистры доступные для чтения заданы в REGISTER_MAP
    Считанные значения складываются в LOG_FILE_NAME

    Необходимо закомментировать строку с регистром в REGISTER_MAP, если не нужно его читать
    """

    # Инициализируем подключение
    Thermostat: minimalmodbus.Instrument = minimalmodbus.Instrument(
        port=config.THERMOSTAT_PORT, slaveaddress=config.THERMOSTAT_ADDR
    )
    Thermostat.serial.baudrate = 115200
    Thermostat.serial.bytesize = 8
    Thermostat.serial.parity = minimalmodbus.serial.PARITY_NONE
    Thermostat.serial.stopbits = 1
    Thermostat.serial.timeout = 1

    log: dict = dict()

    FUNCTION_CODE: typing.Final[dict] = {
        "INPUT_REGISTERS": 4,
        "HOLDING_REGISTERS": 3,
    }

    print("\n***Current values***\n")

    print(f"T1: {get_t1(Thermostat)[0] / 10} C")
    print(f"T2: {get_t2(Thermostat)[0] / 10} C")
    print(f"HT3: {get_ht3_temp(Thermostat)[0] / 10} C {get_ht3_humid(Thermostat)[0] / 10} %Rh")
    print(f"HTR: {get_htr(Thermostat)}, FAN:{get_fan(Thermostat)}, AE: {get_ae(Thermostat)}")
    print(f"SW veresion: {get_sw_version(Thermostat)}\n")

    print("***Registers data***\n")
    for registers_type in config.REGISTER_MAP.keys():
        for register_name in config.REGISTER_MAP.get(registers_type).keys():
            if ret_val := my_modbus_worker(
                func=Thermostat.read_registers,
                args={
                    "registeraddress": int(
                        config.REGISTER_MAP.get(registers_type).get(register_name), 16
                    ),
                    "number_of_registers": 1,
                    "functioncode": FUNCTION_CODE.get(registers_type),
                },
            ):
                print(f"Value of {register_name}: {convert_to_signed(ret_val[0])}")
                log.setdefault(register_name, convert_to_signed(ret_val[0]))
            else:
                print(f"Error while reading {register_name}")
                log.setdefault(register_name, "")

    print("\n***Finished reading***")

    with open(config.LOG_FILE_NAME_READ, "w") as json_file:
        json.dump(log, json_file, indent=4)


if __name__ == "__main__":
    main()
