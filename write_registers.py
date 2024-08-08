import minimalmodbus
import time
import json
from config import configuration as config


def my_modbus_worker(func, args):
    attempts_counter: int = 0

    while attempts_counter <= config.ATTEMPTS_TO_MODBUS_CONNECTIONS:
        try:
            if func(**args) is None:
                return True
        except Exception as err:
            # print(err)
            attempts_counter += 1
            time.sleep(config.WRITE_MODBUS_TIMEOUT)

    return False

def convert_to_unsigned(value):
    """Преобразует int в u_int."""
    if value < 0:
        value = (1 << 16) + value
    return value

def main():
    """
    Пишем регистры термостата по адресу: THERMOSTAT_ADDR, используя COM порт: THERMOSTAT_PORT
    Все регистры доступные для записи заданы в REGISTER_MAP
    Результат о записи регистра складывается в LOG_FILE_NAME

    Необходимо указать значения записываемых регистров в REGISTERS_DATA_FILE_NAME
    """

    # Инициализируем подключение
    Thermostat: minimalmodbus.Instrument = minimalmodbus.Instrument(port=config.THERMOSTAT_PORT,
                                                                    slaveaddress=config.THERMOSTAT_ADDR)
    Thermostat.serial.baudrate = 115200
    Thermostat.serial.bytesize = 8
    Thermostat.serial.parity = minimalmodbus.serial.PARITY_NONE
    Thermostat.serial.stopbits = 1
    Thermostat.serial.timeout = 1

    log: dict = dict()

    my_modbus_worker(func=Thermostat.write_register,
                     args={
                         "registeraddress": 13,
                         "value": 1,
                         "functioncode": 16
                     })

    for register_name in config.DATA_MAP.keys():
        if register_name in config.REGISTER_MAP.get("HOLDING_REGISTERS").keys():
            if ret_val := my_modbus_worker(func=Thermostat.write_register,
                                           args={
                                               "registeraddress": int(
                                                   config.REGISTER_MAP.get("HOLDING_REGISTERS").get(register_name), 16),
                                               "value": convert_to_unsigned(config.DATA_MAP.get(register_name)),
                                               "functioncode": 6
                                           }):
                print(f"Successful writing {register_name}")
                log.setdefault(register_name, True)
            else:
                print(f"Error while writing {register_name}")
                log.setdefault(register_name, False)

    print("\n***Finished writing***")

    with open(config.LOG_FILE_NAME_WRITE, "w") as json_file:
        json.dump(log, json_file, indent=4)


main()
