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
    data[:, :3] = data[:, :3] / 10.0

    plt.figure()
    plt.title('attitude rad')
    for i in range(3):
        plt.plot(data[:, i], '-.', label=str(i))
        if i is 1:
            data[:,i] = data[:,i] * -1.0

    plt.legend()
    plt.grid()

    # acc
    print('before nomr:', np.linalg.norm(data[0, 3:6]))
    data[:, 3:6] = data[:, 3:6] / (16384.0) * (9.8)

    plt.figure()
    plt.title('gravity m/s^2')
    for i in range(3):
        plt.plot(data[:, i + 3], '-.', label=str(i))
        if i is 1:
            data[:,i+3] = data[:,i+3] * -1.0
    plt.legend()
    plt.grid()

    print('norm of acc is :', np.linalg.norm(data[0, 3:6]))
    # print(data[0,3:6].shape)


    data[:, 6:9] = data[:, 6:9] / (32.8) * np.pi / 180.0
    plt.figure()
    plt.title('gyr rad/s ')

    for i in range(3):
        plt.plot(data[:, i + 6], '-.', label=str(i))
        if i is 1:
            data[:,i+6] = data[:,i+6] * -1.0
    plt.grid()
    plt.legend()

    out_data = np.zeros([data.shape[0], 10])

    out_data[:, 1:7] = data[:, 3:9] * 1.0
    out_data[:, 7:10] = data[:, :3] * 1.0

    for i in range(1, out_data.shape[0] - 1):
        out_data[i, 0] = out_data[i - 1, 0] + 0.01

    # for i in [2,5,8]:
    #     i = i-1
    #     out_data[:,i] = out_data[:,i] * -1.0

    np.savetxt(dir_name + "ImuData.csv", out_data, delimiter=',')



    plt.figure()
    print(min(data[:, 2]), max(data[:, 2]))
    plt.hist(data[:, 0], 90)

    plt.figure()
    plt.title('mag norm')
    plt.plot(np.linalg.norm(data[:,9:12],axis=1))

    plt.figure()
    plt.title('mag normalized')
    mag_norm = np.linalg.norm(data[:,9:12],axis=1)

    for i in [9,10,11]:
        plt.plot(data[:,i]/mag_norm,'-*',label=str(i))
    plt.grid()
    plt.legend()

    plt.figure()
    plt.title('mag arctan2(x,y)')
    plt.plot(np.arctan2(data[:,9],data[:,10])/np.pi * 180.0,'+r')



    plt.grid()

    plt.show()
