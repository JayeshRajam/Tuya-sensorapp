#!/usr/bin/env python
import time
import coloredlogs
from tuyalinksdk.client import TuyaClient
from tuyalinksdk.console_qrcode import qrcode_generate
coloredlogs.install(level='DEBUG')
import serial
import csv
from datetime import datetime

# Define the serial port and baud rate.
ser = serial.Serial('COM11', 115200, timeout=1)
client = TuyaClient(productid='zyj45zftq3e4pyxs',
                    uuid='tuya3109c5966245faa1',
                    authkey='JryUNf86h02PhnRJccdIDATZKdLRtnAN')

def on_connected():
    print('Connected.')

def on_qrcode(url):
    qrcode_generate(url)

def on_reset(data):
    print('Reset:', data)

def on_dps(dps):
    print('DataPoints:', dps)
    dps['101'] = int(ser.readline().decode('ascii'))
    # Here we are storing our data in a variable. We'll add this data in our csv file
    rows = [datetime.now(),ser.readline().decode('ascii')]
    with open('MS.csv', 'a' ,newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows)
    client.push_dps(dps)
    
client.on_connected = on_connected
client.on_qrcode = on_qrcode
client.on_reset = on_reset
client.on_dps = on_dps

client.connect()
client.loop_start()

while True:
    print(ser.readline().decode('ascii'))
    time.sleep(1)