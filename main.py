from machine import Pin
from utime import sleep

ledMap = {
    0: 6,
    1: 7,
    2: 8,
    3: 9,
    4: 10,
    5: 11,
    6: 12,
    7: 13
}

def decToBin(num):
    return "{:08b}".format(int(num))

def strSplit(string):
    lst = []
    lst.extend(string)
    return lst

def writeLed(address, state):
    led = Pin(address, Pin.OUT)
    if int(state):
        led.high()
        return 1
    else:
        led.low()
        return 0

def main():
    for i in range(256):
        register = strSplit(decToBin(i))
        for bit in range(len(register)):
            writeLed(ledMap[bit],register[bit])
        sleep(0.5)

while True:
    main()