import socket
import cv2
import numpy
# tester of Seq

print('Initiate NN Accelerator...')

from pynq import Xlnk
from pynq import Overlay
import numpy as np
from numpy import *
import math
import time

#import matplotlib.pyplot as plt
overlay = Overlay('./board_zcu104/zcu104_pe2.bit')
accelerator = overlay.cnn_top_0
xlnk = Xlnk()

from yottai.nna_v0_8 import NNA
from yottai.utils_v0_5 import *
from yottai.Sequential_v0_8 import Seq
from yottai.caffe_classes import class_names


##############################################################################################
# Initiate NN accelerator, load parameter and data
print('Load parameter...')

nna = NNA(accelerator, xlnk)
model_name = 'alexnet_tf'
model_name = '../seq/model/' + model_name + '.yonet'
seq = Seq(nna, model_name)

address = ('0.0.0.0', 13000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(address)
s.listen(True)


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf
while 1:

    conn, addr = s.accept()

    length = recvall(conn,16)
    stringData = recvall(conn, int(length))
    data = numpy.fromstring(stringData, dtype='uint8')
    decimg=cv2.imdecode(data,1)
    print(type(decimg))
    print(decimg[:224].shape)#[numpy.newaxis, : ,:]
    #cv2.imshow('SERVER',decimg)
    #if cv2.waitKey(10) == 27:
    #    break

    image = seq.load_picture(decimg[:224],decimg[224:])
    print(type(image))
    print(image.shape)
    stat(image, 'image')
    
    t = time.time()
    prob = seq.build()
    print('Time(s): %.2f' % (time.time()-t))

    # output
    output= seq.prob
    inds = argsort(prob)
    print("--------->",inds)
    data1=""
    for i in range(5):
        print(class_names[inds[0][-1-i]], prob[0][inds[0][-1-i]])
        if i==4:
            data1+=str(class_names[inds[0][-1-i]])+"Core:"+str(prob[0][inds[0][-1-i]])
        else:
            data1+=str(class_names[inds[0][-1-i]])+"<br>Core:"+str(prob[0][inds[0][-1-i]])+"<hr>"
    data1+="<br><hr><br><hr>"
    for i in range(5):
        print(class_names[inds[1][-1-i]], prob[1][inds[1][-1-i]])
        if i==4:
            data1+=str(class_names[inds[1][-1-i]])+"<br><br>Core:"+str(prob[1][inds[1][-1-i]])
        else:
            data1+=str(class_names[inds[1][-1-i]])+"<br>Core:"+str(prob[1][inds[1][-1-i]])+"<hr>"
    from socket import *

    HOST = '192.168.1.96' # or 'localhost'
    PORT = 13000
    BUFSIZ =1024
    ADDR = (HOST,PORT)

    tcpCliSock = socket(AF_INET,SOCK_STREAM)
    tcpCliSock.connect(ADDR)
#data1="helleok"
#while True:
     #data1 = input('>')
     #data = str(data)
     # if not data1:
     #    break
    tcpCliSock.send(data1.encode())
    #tcpCliSock.send(data2.encode())
     #tcpCliSock.send(data1.encode())
     #data1 = tcpCliSock.recv(BUFSIZ)
     #if not data1:
      #   break
     #print(data1.decode('utf-8'))
    tcpCliSock.close()
# address = ('0.0.0.0', 13000)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(address)
# s.listen(True)


# def recvall(sock, count):
#     buf = b''
#     while count:
#         newbuf = sock.recv(count)
#         if not newbuf: return None
#         buf += newbuf
#         count -= len(newbuf)
#     return buf

# conn, addr = s.accept()

# length = recvall(conn,16)
# stringData = recvall(conn, int(length))
# data = numpy.fromstring(stringData, dtype='uint8')
# decimg=cv2.imdecode(data,1)
# print(type(decimg))
# print(decimg.shape)#[numpy.newaxis, : ,:]
#     #cv2.imshow('SERVER',decimg)
#     #if cv2.waitKey(10) == 27:
#     #    break

# image = seq.load_picture(decimg)
# print(type(image))
# print(image.shape)
# stat(image, 'image')
    
# t = time.time()
# prob = seq.build()
# print('Time(s): %.2f' % (time.time()-t))

#     # output
# output= seq.prob
# inds = argsort(prob)
# print("--------->",inds)
# for i in range(5):
#     print(class_names[inds[-1-i]], prob[inds[-1-i]])
#     if i==0 :
#         data1=class_names[inds[-1-i]]
#     if i==1 :
#         data2=class_names[inds[-1-i]]
# s.close()
# from socket import *

# HOST = '192.168.1.96' # or 'localhost'
# PORT = 13000
# BUFSIZ =1024
# ADDR = (HOST,PORT)

# tcpCliSock = socket(AF_INET,SOCK_STREAM)
# tcpCliSock.connect(ADDR)
# #data1="helleok"
# #while True:
#      #data1 = input('>')
#      #data = str(data)
#      # if not data1:
#      #    break
# tcpCliSock.send(data1.encode())
# tcpCliSock.send(data2.encode())
#      #tcpCliSock.send(data1.encode())
#      #data1 = tcpCliSock.recv(BUFSIZ)
#      #if not data1:
#       #   break
#      #print(data1.decode('utf-8'))
# tcpCliSock.close()
# address = ('192.168.1.96', 13000)
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(address)
# # s, addr = s.accept()
# s.send(('%s' % ('ok')).encode())
# # #s.send(b'USER test\r\n')
# s.close()
#cv2.destroyAllWindows()