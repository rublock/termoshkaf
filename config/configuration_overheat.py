import typing

from config.configuration_alloff import *

DATA_MAP: typing.Final[dict] = {
    "HUMID_MAX_LEVEL": 890,  # Максимальная относительная влажность (умножено на 10) Диапазон 100...900 %, По умолчанию 800
    "OTP_LEVEL": 0,  # Температура перегрева х10 (отключения АО), 0...600ºС, По умолчанию 50
}
