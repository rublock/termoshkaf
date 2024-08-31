import typing

from config.configuration_alloff import *

DATA_MAP: typing.Final[dict] = {
    "HUMID_MAX_LEVEL": 890,  # Максимальная относительная влажность (умножено на 10) Диапазон 100...900 %, По умолчанию 800
    "HUMID_ALARM_LEVEL": 600,  # Порог аварийной влажности (умножено на 10) 60...99 %, По умолчанию 900
}
