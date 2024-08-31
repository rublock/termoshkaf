import typing

from config.configuration_alloff import *

DATA_MAP: typing.Final[dict] = {
    "HUMID_MAX_LEVEL": 890,  # Максимальная относительная влажность (умножено на 10) Диапазон 100...900 %, По умолчанию 800
    "COLD_START_LEVEL": -40,  # Минимальная температура включения АО (“холодный старт”), ºС Диапазон -40…+60, По умолчанию 0
}
