# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 13:07:28 2018

@author: Johnny
"""

import gzip

import struct as st

import matplotlib.pyplot as plt

import numpy as np

with gzip.open('C:/pythonwork/dataset/train-images-idx3-ubyte.gz','rb')as f1:
    buf1=f1.read()
    
with gzip.open('C:/pythonwork/dataset/train-labels-idx1-ubyte.gz','rb')as f2:
    buf2=f2.read()
    
    
def get_training_label_data(num):

    label_index=0

    label_index+=st.calcsize('ii')

    #print('label的初始index=',label_index)

    #y_predict=[]

    #test=st.unpack_from('b',buf2,label_index)

    #print(type(test))

    y_predict=st.unpack_from(str(num)+'b',buf2,label_index)

    return y_predict

#讀出多張28x28的圖片資料
def get_training_image(num):

    image_index_2=0

    image_index_2+=st.calcsize('>IIII')

    x_training_data=[]

    for i in range(num):

        image_box=st.unpack_from('>784B',buf1,image_index_2)

        image_array=np.reshape(image_box,(28,28))

        x_training_data.append(image_array)

        image_index_2+=784

    return x_training_data


if __name__=='__main__':
    
    imageNum=15

    y_predict=get_training_label_data(imageNum)
    
    y_predict=np.reshape(y_predict,(imageNum,1))
    
    print('y_predict:',y_predict.shape)

    x_training_data=get_training_image(imageNum)
    
    x_training_data=np.reshape(x_training_data,(imageNum,28,28))
    
    print('x_training_data',x_training_data.shape)

    fig=plt.gcf()
    
    fig.set_size_inches(10,10)
    
    for i in range(imageNum):
        
        if imageNum>5:
            plt.subplot((imageNum//5)+1,5,i+1)
        else:
            plt.subplot(1,imageNum,i+1)

        plt.imshow(x_training_data[i])

        plt.title('label data=%s'%str(y_predict[i]))

    #plt.imshow(x_training_data[2],cmap='gray')