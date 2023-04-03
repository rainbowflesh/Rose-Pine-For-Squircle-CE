# Rub and connect
# Also do change device SSID (message 0x12)
#
# Tello Python3 Control Demo
#
# http://www.ryzerobotics.com/
#
# 1/1/2018

from time import sleep

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = ''
port = 8890
locaddr = (host, port)
tello_address = ('192.168.10.1', 8889)
sock.bind(locaddr)

uav_ssid = 'iamtelloaoligei'


def initial_sdk():
    i = 1
    while i < 5:
        # send 'command' first
        pre_command = 'command'
        pre_command = pre_command.encode(encoding="utf-8")
        sent = sock.sendto(pre_command, tello_address)
        print('pre_command:', pre_command, sent)
        i += 1
        sleep(0.1)


def main():

    i = 1
    while i < 10:
        # change ssid
        msg = 'wifi '+uav_ssid+' tello'
        sock.sendto(msg.encode(
            encoding="utf-8"), tello_address)
        i += 1
        sleep(0.1)


if __name__ == '__main__':

    initial_sdk()
    main()
