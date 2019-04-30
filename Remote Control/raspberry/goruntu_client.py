import io
import socket
import struct
import time
import picamera
from time import sleep

#time.sleep(20)

# create socket and bind host
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.1.102', 2014))
connection = client_socket.makefile('wb')


while True:
    print("Komut alinabilir")
    time.sleep(5)
