# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 15:48:20 2018

@author: ASUS
"""
import tensorflow as tf
import numpy as np
#导入或者随机定义训练的数据x和y
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data * 0.1 + 0.3
Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0))
biases = tf.Variable(tf.zeros([1]))
y = Weights * x_data + biases
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.initialize_all_variables()
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
sess.run(init)
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step,sess.run(Weights),sess.run(biases))