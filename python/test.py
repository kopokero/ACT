#text파일에 시간과 온도만 받는 코드
import time
import serial
import csv
from random import *
import datetime
import time


def loar_receiver():

    # UART 세팅
    ser = serial.Serial(port='COM5', baudrate=9600, timeout=None)

    while True:
        try:
            data = ser.readline().decode('utf8').replace(' ', '').replace('\n', '') #필요 옵션 추가
            data = data.upper()
            text = open('data.txt', 'a')
            now = time.localtime()
            now = "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
            print (now + ' ' + data)
            text.write(now + ' ' + data)
            if not data : #수신되는 데이터가 없다면 계속 첫 수신 상태로
                continue

        except Exception as e:
            pass

if __name__ == '__main__':

    loar_receiver()

