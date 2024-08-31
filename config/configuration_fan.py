import typing

from config.configuration_base import *

DATA_MAP: typing.Final[dict] = {
    "TEMP_MAX_LEVEL": 50,  # Максимальная температура (умножено на 10) Диапазон: -400...600 ºС, По умолчанию 400
    "HUMID_MAX_LEVEL": 890,  # Максимальная относительная влажность (умножено на 10) Диапазон 100...900 %, По умолчанию 800
}
