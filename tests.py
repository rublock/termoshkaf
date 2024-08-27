from config import configuration as config
from config import configuration_1 as config_1
from config import configuration_2 as config_2
from config import configuration_3 as config_3
from config import configuration_4 as config_4
from config import configuration_5 as config_5
from config import configuration_6 as config_6
from config import configuration_7 as config_7

import write_registers

# TODO написать логику чтобы при нажатии нужной записывался конфиг
# TODO продумать как изменять данные в конфиге пользователем!!!
write_registers.main(config)
