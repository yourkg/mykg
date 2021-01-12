# tester of Seq

print('Initiate NN Accelerator...')

from pynq import Xlnk
from pynq import Overlay
import numpy as np
from numpy import *
import math
import time
PE= input('Input PE:')
PE=int(PE)
#import matplotlib.pyplot as plt
#overlay = Overlay('../seq/board_zcu104/zcu104_mac256_clk150_1.bit')
overlay = Overlay('./board_zcu104/zcu104_pe'+str(PE)+'.bit')
accelerator = overlay.cnn_top_0
xlnk = Xlnk()

from yottai.nna_v1_1 import NNA
from yottai.utils_v0_5 import *
from yottai.Sequential_v1_1 import Seq
from yottai.caffe_classes import class_names


##############################################################################################
# Initiate NN accelerator, load parameter and data
print('Load parameter...')

nna = NNA(PE,accelerator, xlnk)
NETLIST=['alexnet_tf','resnet50','vgg16']
s = input('Select model name in list:\n1.AlexNet\n2.Resnet50\n3.VGG16\n/')
model_name = NETLIST[int(s)-1]
model_name = '../seq/model/' + model_name + '.yonet'
seq = Seq(PE,nna, model_name)

while True:
    print('\n\n##############################################################################################')
    filename=[]
    for i in range(PE):
        f= input('Input image1 file: data/')
        file='../seq/data/' + f + '.jpg'
        filename.append(file)
    if(filename=='exit'):
        break
    #filename = 'data/tiger.jpg'
    image = seq.load_pictureX(filename)
    stat(image, 'image')
    
    t = time.time()
    prob = seq.build()
    print('Time(s): %.2f' % (time.time()-t))

    # output
    output= seq.prob
    inds = argsort(prob)
    for i in range(PE):
        print("image"+str(i+1)+":")
        for j in range(5):
            print(class_names[inds[i][-1-j]],prob[i][inds[i][-1-j]])