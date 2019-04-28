import threading
import SocketServer
import numpy as np
import cv2
import pygame
from pygame.locals import *
import time
import os

araba_data = " "

class ArabaDataHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        global araba_data
        try:
            while True:
                while araba_data is not None and araba_data != "bos" and araba_data != " ":
                    self.request.send(araba_data.encode())
                    print(araba_data)
                    araba_data = "bos"
        finally:
            print("Connection closed on thread 2")

class VideoStreamHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        global araba_data

        pygame.init()

        self.send_inst = True

        try:
            while True:
                while self.send_inst:
                    for event in pygame.event.get():
                        if event.type == KEYDOWN:
                            key_input = pygame.key.get_pressed()

                            if key_input[pygame.K_SPACE]:
                                print("Gaz")
                                #self.ser.write(chr(1)
                                araba_data = "G"

                            elif key_input[pygame.K_UP]:
                                print("Forward")
                                araba_data = "W"

                            elif key_input[pygame.K_DOWN]:
                                print("Stop")
                                #self.ser.write(chr(1)
                                araba_data = "S"

                            elif key_input[pygame.K_RIGHT]:
                                print("Right")
                                araba_data = "D"

                            elif key_input[pygame.K_LEFT]:
                                print("Left")
                                araba_data = "A"

                            elif key_input[pygame.K_o]:
                                print ('servo kapat')
                                araba_data = "O"
                                #self.ser.write(chr(0))

                            elif key_input[pygame.K_q]:
                                print ('basarili exit')
                                self.send_inst = False
                                #self.ser.write(chr(0))
                                break

                self.send_inst = True

        finally:
            self.rfile.close()
            print("Connection closed on thread 1")

class ThreadServer(object):

    def server_thread(host, port):
        server = SocketServer.TCPServer((host, port), VideoStreamHandler)
        server.serve_forever()

    def server_thread2(host, port):
        server = SocketServer.TCPServer((host, port), ArabaDataHandler)
        server.serve_forever()

    araba_thread = threading.Thread(target=server_thread2, args=('192.168.1.100', 2011))
    araba_thread.start()
    video_thread = threading.Thread(target=server_thread('192.168.1.100', 2012))
    video_thread.start()

if __name__ == '__main__':
    ThreadServer()
