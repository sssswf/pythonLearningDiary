# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:41:12 2018

@author: ASUS
"""

import tensorflow as tf
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
c = tf.multiply(a,b)
with tf.Session() as sess:
    print(sess.run(c,feed_dict={a:[3.],b:[5.]}))