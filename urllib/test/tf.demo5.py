# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 22:51:51 2018

@author: ASUS
"""
#encoding=utf-8
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
#定义一个方法用于添加层
def add_layer(inputs,in_size,out_size,activation_function = None):
    Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='w')
    biases = tf.Variable(tf.zeros([1,out_size])+0.1,name='b')
    Wx_plus_b = tf.add(tf.matmul(inputs,Weights),biases) 
    if activation_function is None:
        outputs = Wx_plus_b  
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
#定义数据集
x_real = np.linspace(-1,1,300)[:,np.newaxis]#[-1,1]之间有300个值，后面[]表示维度，即有300行
noise = np.random.normal(0,0.05,x_real.shape)#噪声均值为0,方差为0.05,与x_data格式相同
y_real = np.square(x_real)-0.5 + noise

xs = tf.placeholder(tf.float32,[None,1],name='x_input')
ys = tf.placeholder(tf.float32,[None,1],name='y_input')
#建造第一层输入层input（1个神经元）：输入1个神经元，隐藏层10个神经元
l1 = add_layer(xs,1,10,activation_function = tf.nn.relu)
#输出层
prediction = add_layer(l1,10,1,activation_function = None)#输出层也是1个神经元
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys-prediction),reduction_indices=[1]))#先求误差平方和的和求平均，reduce_sum表示对矩阵求和，reduction_indices=[1]方向
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)#学习效率0.1,要求小于1
init = tf.initialize_all_variables()#初始化所有变量
sess = tf.Session()
sess.run(init)#激活
#可视化结果
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_real,y_real)
plt.ion()
plt.show()
for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_real, ys: y_real})
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_real})
        # plot the prediction
        lines = ax.plot(x_real, prediction_value, 'r-', lw=5)
        plt.pause(0.3)
