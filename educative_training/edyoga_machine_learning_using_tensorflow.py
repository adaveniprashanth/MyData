#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 17:36:12 2020

@author: pj
"""
import tensorflow as tf
print (tf.__version__)
h = tf.constant("hello")
w = tf.constant('zeek')
hw = h+w
# print(hw)

with tf.Session() as sess:
    res = sess.run(hw)
    tf.summary.Filewriter('new-logs',sess.graph)

