import typing

####################---------Установки связи---------####################

THERMOSTAT_PORT: typing.Final[str] = "COM4"  # Номер COM порта, присвоенный преобразователю USB>RS485
THERMOSTAT_ADDR: typing.Final[int] = 100  # Modbus адрес термостата

####################---------Установки для поддержания климата---------####################

DATA_MAP: typing.Final[dict] = {
    "TEMP_MAX_LEVEL": 550,  # Максимальная температура (умножено на 10) Диапазон: -400...600 ºС, По умолчанию 400
    "TEMP_MIN_LEVEL": -390,  # Минимальная температура (умножено на 10) Диапазон: -400...600 ºС, По умолчанию 100
    "HUMID_MAX_LEVEL": 890,  # Максимальная относительная влажность (умножено на 10) Диапазон 100...900 %, По умолчанию 800
    "HUMID_HYST": 100,  # Гистерезис (умножено на 10) влажности при осушении, 10...800%, По умолчанию 300
    "HUMID_ALARM_LEVEL": 990,  # Порог аварийной влажности (умножено на 10) 60...990 %, По умолчанию 900
    "SENSOR_PRIO1": 1,  # Приоритет для датчика температуры Диапозон 0...2 , Датчик с более высоким приоритетом является основным
    "SENSOR_PRIO2": 0,  # Приоритет для датчика температуры Диапозон 0...2 , Датчик с более высоким приоритетом является основным
    "SENSOR_PRIO3": 2,  # Приоритет для датчика температуры Диапозон 0...2 , Датчик с более высоким приоритетом является основным
    "SENSOR_EXT": 255,  # Наружный датчик температуры 0 - Тц1, 1 - Тц2, 255 - наружный датчик не выбран
    "SENSORS_ENABLED": 5,  # Включить датчики Битовая маска: Бит 0 - Tц1 Бит 1 - Tц2 Бит 2 - Tц3 Бит 3 - Ta, По умолчанию 15(включены все)
    "SEARCH_FOR_SENSORS": 0,  # Поиск датчиков Тц1 и Тц2 (1 - искать новые 1-wire датчики)
    "RELAY_MIN_SW_TIME": 60,  # Минимальное время переключения реле Диапазон 0...600 сек, По умолчанию 30
    "OTP_ENABLED": 1,  # Отключение АО при перегреве Диапазон 0...1, По умолчанию 0
    "OTP_LEVEL": 600,  # Температура перегрева х10 (отключения АО), 0...600ºС, По умолчанию 50
    "OTP_HYST": 10,  # Гистерезис температуры включения АО х10, 10...100 ºС, По умолчанию 50
    "COLD_START_ENABLED": 1,  # Включение режима холодного старта для АО 0...1, По умолчанию 1
    "COLD_START_LEVEL": -40,  # Минимальная температура включения АО (“холодный старт”), ºС Диапазон -40…+60, По умолчанию 0
    "FAN_HYST": 10,  # Гистерезис температуры включения вентилятора х10, 10...100 ºС, По умолчанию 50
    "HEAT_HYST": 10,  # Гистерезис температуры включения нагрева х10, 10...100 ºС, По умолчанию 50
    "MODBUS_ADDR": 100,  # ModBus-адрес устр-ва Диапазон 1...247, По умолчанию 1
}

####################---------Адреса регистров для чтения и записи---------####################


REGISTER_MAP: typing.Final[dict] = {
    "INPUT_REGISTERS":  # INPUT_REGISTERS Только для чтения
        {
            "T_DS1_VALUE": "0x00",  # Температура х10 (датчик Тц1), ºС
            "T_DS1_STATE": "0x01",  # Состояние датчика температуры Тц1
            "T_DS2_VALUE": "0x02",  # Температура х10 (датчик Тц2), ºС
            "T_DS2_STATE": "0x03",  # Состояние датчика температуры Тц2
            "TH_HUMID_VALUE": "0x0A",  # Показания влажности х10 (датчик температуры и влажности), %
            "TH_TEMP_VALUE": "0x0B",  # Показания температуры х10 (датчик температуры и влажности), ºС
            "TH_STATE": "0x0C",  # Состояние датчика температуры и влажности
            "ACTIVE_STATE": "0x0E",  # Состояние реле АО
            "FAN_STATE": "0x0F",  # Состояние реле вентилятора
            "HEAT_STATE": "0x10",  # Состояние реле нагревателя
            "ALARM_FLAG_HI": "0x18",  # Флаг аварии (HI)
            "ALARM_FLAG_LOW": "0x19",  # Флаг аварии (LOW)
            "SERIAL_HI": "0x1E",  # Серийный номер устройства (HI)
            "SERIAL_LOW": "0x1F",  # Серийный номер устройства (LOW)
            "VERSION_SW": "0x1C"  # Вверсия ПО
        },
    "HOLDING_REGISTERS":  # HOLDING_REGISTERS для чтения и записи
        {
            "TEMP_MAX_LEVEL": "0x00",  # Максимальная температура х10, ºС
            "TEMP_MIN_LEVEL": "0x01",  # Минимальная температура х10, ºС
            "HUMID_MAX_LEVEL": "0x02",  # Максимальная относительная влажность х10, %
            "HUMID_HYST": "0x03",  # Гистерезис относительной влажности х10, %
            "HUMID_ALARM_LEVEL": "0x04",  # Аварийная относительная влажность х10, %
            "SENSOR_PRIO1": "0x06",  # Тц1 - цифровой 1-Wire датчик с логическим приоритетом 0 (датчик с более высоким приоритетом (кроме наружного) является основным, с менее высоким - резервным)
            "SENSOR_PRIO2": "0x07",  # Tц2 - цифровой 1-Wire датчик температуры с логическим приоритетом 1
            "SENSOR_PRIO3": "0x08",  # Цифровой SWire датчик температуры с логическим приоритетом 2
            "SENSOR_EXT": "0x0B",  # Наружный датчик температуры
            "SENSORS_ENABLED": "0x0C",  # Включение датчиков
            "SEARCH_FOR_SENSORS": "0x0E",  # Поиск датчиков Тц1 и Тц2
            "RELAY_MIN_SW_TIME": "0x17",  # Минимальное время переключения реле, сек.
            "OTP_ENABLED": "0x18",  # Отключение АО при перегреве
            "OTP_LEVEL": "0x19",  # Температура перегрева х10 (отключения АО), ºС
            "OTP_HYST": "0x1A",  # Гистерезис температуры включения АО х10, ºС
            "COLD_START_ENABLED": "0x1B",  # Включение режима холодного старта для АО
            "COLD_START_LEVEL": "0x1C",  # Минимальная температура включения АО х10, ºС
            "FAN_HYST": "0x1E",  # Гистерезис температуры включения вентилятора х10, ºС
            "HEAT_HYST": "0x20",  # Гистерезис температуры включения нагрева х10, ºС
            "MODBUS_ADDR": "0x27",  # ModBus-адрес устр-ва 1...247
        }
}

####################---------Дополнительные настройки---------####################

ATTEMPTS_TO_MODBUS_CONNECTIONS: typing.Final[int] = 3  # Количество попыток подключения по Modbus протоколу (рекомендовано 3)
WRITE_MODBUS_TIMEOUT: typing.Final[float] = 0.2  # Таймаут между запись значений (рекомендовано 0.2)
LOG_FILE_NAME_WRITE: typing.Final[str] = "write_registers_log.json"  # Название файла для логов записи
LOG_FILE_NAME_READ: typing.Final[str] = "read_registers_log.json"  # Навзвание фала для логов чтения
