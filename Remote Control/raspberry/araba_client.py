import socket
import io
import struct
import picamera
import sys
import car_sample
import simpleServoControl as servo
import time

#time.sleep(20)

servo.set_angle(7.5)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_address = "192.168.1.102"
socket_port = 2013
server_address = (ip_address,socket_port)
sock.connect(server_address)

try:    
    # Look for the response
    message = "00122223333"
    amount_received = 0
    amount_expected = len(message)

    aci = 7.5
    
    while True:
        data = sock.recv(16)
        amount_received += len(data)
        print(data.decode())        

        if data == 'G':
            car_sample.calis()
        elif data == 'W':
            aci = 7.5
            servo.set_angle(aci)
        elif data == 'A':
            aci = aci + 1
            servo.set_angle(aci)
        elif data == 'D':
            aci = aci - 1
            servo.set_angle(aci)
        elif data == 'S':
            car_sample.dur()
        elif data == 'O':
            servo.kapat() 
        else:
            print "Farkli veri"
            

finally:
    sock.close()
    
