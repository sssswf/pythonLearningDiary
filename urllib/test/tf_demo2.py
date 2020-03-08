# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:20:06 2018

@author: ASUS
"""
import tensorflow as tf
state = tf.Variable(0)
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)

init = tf.initialize_all_variables()
with tf.Session() as sess:
    sess.run(init)
    for i in range(4):
        sess.run(update)
        print(sess.run(state))