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

    dir_name = '/home/steve/Data/AttitudeIMU/'
    file_name = dir_name + '2.txt'

    data = np.loadtxt(file_name)
    data = data.astype(float)

    # att
    data[:,:3] = data[:,:3] / 10.0

    plt.figure()
    plt.title('attitude rad')
    for i in range(3):
        plt.plot(data[:,i],'-.',label = str(i))
    plt.legend()
    plt.grid()



    # acc
    print('before nomr:', np.linalg.norm(data[0,3:6]))
    data[:,3:6] = data[:,3:6] / (16384 )* (9.8)

    plt.figure()
    plt.title('gravity m/s^2')
    for i in range(3):
        plt.plot(data[:,i+3],'-.',label = str(i))
    plt.legend()
    plt.grid()

    print('norm of acc is :',np.linalg.norm(data[0,3:6]))
    # print(data[0,3:6].shape)


    data[:,6:9] = data[:,6:9] /(32.8) * np.pi / 180.0
    plt.figure()
    plt.title('gyr rad/s ')

    for i in range(3):
        plt.plot(data[:,i+6],'-.',label =str(i))
    plt.grid()
    plt.legend()


    out_data = np.zeros([data.shape[0],9])

    out_data[:,0:6] = data[:,3:9] * 1.0
    out_data[:,6:9] = data[:,:3] *1.0

    np.savetxt(dir_name+"ImuData.csv",out_data)




    plt.show()