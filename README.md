# Thermostat Modbus Writer and Reader

Этот репозиторий содержит конфигурационный файл и два скрипта для работы с термостатом по протоколу Modbus RTU: 
<br>`write_register.py` для записи данных в регистры
<br>`read_registers.py` для чтения данных из регистров.
<br>`configuration_*.py` Параметры конфигурации для закрузки в теромстат</br>

## Установка драйвера

[Рекомендуемая модель ПРЕОБРАЗОВАТЕЛЯ ИНТЕРФЕЙСОВ USB-485](https://bolid.ru/production/orion/interface-converter/usb-rs485.html#characteristics)

Перед началом работы убедитесь, что у вас установлен и активен драйвер для работы с USB в RS485.<br>Если драйвер не установлен, загрузите его по следующей ссылке:</br>

[Скачать драйвер для USB в RS485](https://bolid.ru/files/373/566/xrusbser_2500.zip)

После скачивания распакуйте архив, содержащий драйвер и выполните установку, следуя инструкциям установщика.

## Установка Python и необходимых модулей

1. Убедитесь, что на вашем компьютере установлен Python версии 3.x. Если Python не установлен, вы можете загрузить его с 
официального сайта python.org, далее запустить установленный файл, в открывшемся окне отметить **Add Python 3.x to PATH** и выбрать Install now.
2. Откройте командную строку на вашем компьютере. В Windows вы можете это сделать, нажав Win+R, введя "cmd" в поле "Выполнить" и нажав Enter.
3. Установите витуальное окружение и необходимые библиотеки, выполнив следующие команды в командной строке:

```
py -m venv venv
```
```
.\venv\Scripts\activate
```
```
pip install -r requirements.txt
``` 

## Конфигурация

В файле `configuration.py` вы можете настроить следующие параметры:
 
- `THERMOSTAT_ADDR`: адрес устройства Modbus.
- `THERMOSTAT_PORT`: порт COM, к которому подключено устройство. 
- `LOG_FILE_NAME_WRITE`: имя файла, в который записывается результат записи.
- `LOG_FILE_NAME_READ`: имя файла, в который записывается результат чтения.
- `REGISTERS_DATA_FILE_NAME`: имя файла, из которого считываются данные для записи.
- `REGISTER_MAP`: карта регистров, где указаны их имена, адреса и описание.
- `DATA_MAP`: указаны значения для записи в регистры.


## Использование ПО

1. Подключите термостат к компьютеру c помощью преобразователя USB в 485 интерфейс.
2. Укажите значение `THERMOSTAT_PORT`
3. По необходимости, отредактируйте файл, чтобы указать значения, которые вы хотите записать в регистры термостата,`configuration_base.py`. 
**Внимание**: убедитесь, что вы указываете валидные адреса регистров и значения.
4. Запустите необходимый скрипт, выполнив команду в командной строке:

**python write_registers.py**
или 
**python read_registers.py**

## Примечания

В случае возникновения ошибок, убедитесь, что:
1) Термостат подключен правильно.
2) Указаны правильные подключения.
3) Указаны допустимые адреса регистров и значения в случае их записи.

## Чтобы запустить интерфейс пользователя кликните на
```
run.bat
```
