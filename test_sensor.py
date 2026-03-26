#   Подключаем библиотеку для работы с бампером I2C-flash.
from pyiArduinoI2Cbumper import *
#   Объявляем объект для работы с функциями и методами
#   библиотеки pyiArduinoI2Cbumper, указывая адрес модуля на шине I2C.
bum = pyiArduinoI2Cbumper(address = 0x09, bus = "/dev/i2c-1")

while True:
    b = bum.getLineSum()
    if b > 4:
        bum.setLineType(BUM_LINE_CHANGE)

    print(bum.getErrPID())
    
