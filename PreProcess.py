# -*- coding:utf-8 -*-
# Created by steve @ 17-10-15 上午8:36
'''
                   _ooOoo_ 
                  o8888888o 
                  88" . "88 
                  (| -_- |) 
                  O\  =  /O 
               ____/`---'\____ 
             .'  \\|     |//  `. 
            /  \\|||  :  |||//  \ 
           /  _||||| -:- |||||-  \ 
           |   | \\\  -  /// |   | 
           | \_|  ''\---/''  |   | 
           \  .-\__  `-`  ___/-. / 
         ___`. .'  /--.--\  `. . __ 
      ."" '<  `.___\_<|>_/___.'  >'"". 
     | | :  `- \`.;`\ _ /`;.`/ - ` : | | 
     \  \ `-.   \_ __\ /__ _/   .-` /  / 
======`-.____`-.___\_____/___.-`____.-'====== 
                   `=---=' 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
         佛祖保佑       永无BUG 
'''

import numpy as np
import scipy as sp

import matplotlib.pyplot as plt


if __name__ == '__main__':

    file_name = '/home/steve/Data/AttitudeIMU/2.txt'

    data = np.loadtxt(file_name)

    data[:,:3] = data[:,:3] / 10.0

    plt.figure()
    plt.title('attitude')
    for i in range(3):
        plt.plot(data[:,i],'-.',label = str(i))
    plt.legend()
    plt.grid()



    plt.figure()
    data[:,3:6] = data[:,3:6] / (16034.53 /9.8)

    plt.title(' ')
    for i in range(3):
        plt.plot(data[:,i+3],'-.',label = str(i))
    plt.legend()
    plt.grid()

    print(np.linalg.norm(data[0,3:6]))





    plt.show()