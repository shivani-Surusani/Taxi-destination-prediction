#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  model.py
import pickle
import pandas as pd
import numpy as np
from Cluster import clust
from transformation import transform
X=transform() #numpy array containing input vectors for each ride
y=clust() #Labels for each ride(Cluster under which it exists
n_examples = len(X)
nninput_dim =2 #26
nnoutput_dim =2 #2072
learn_rate = 0.01
r_lam= 0.01
def calculate_loss(model):
  W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
  zzz1 = X.dot(W1) + b1
  aaa1 = np.tanh(zzz1)
  zzz2 = aa1.dot(W2) + b2
  expo_scor = np.exp(zzz2)
  probabs = expo_scor / np.sum(expo_scor, axis=1, keepdims=True)
  correct_logprobabs = -np.log(probabs[range(n_examples), y])
  dataloss = np.sum(correct_logprobabs)
  dataloss += r_lam/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
  return 1./n_examples * dataloss
def predict(model, x):
  W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
  zzz1 = x.dot(W1) + b1
  aaa1 = np.tanh(zzz1)
  zzz2 = aa1.dot(W2) + b2
  expo_scor = np.exp(zzz2)
  probabs = expo_scor / np.sum(expo_scor, axis=1, keepdims=True)
  return np.argmax(probabs, axis=1)
def build_model(nn_hdim, num_passes=20000, print_loss=False):
  np.random.seed(0)
  W1 = np.random.randn(nninput_dim, nn_hdim) / np.sqrt(nninput_dim)
  b1 = np.zeros((1, nn_hdim))
  W2 = np.random.randn(nn_hdim, nnoutput_dim) / np.sqrt(nn_hdim)
  b2 = np.zeros((1, nnoutput_dim)) 
  model = {}
  for i in xrange(0, num_passes):
    # Forward propagation
    zz1 = X.dot(W1) + b1
    aa1 = np.tanh(zz1)
    zz2 = aa1.dot(W2) + b2
    expo_scor = np.exp(zz2)
    probabs = expo_scor / np.sum(expo_scor, axis=1, keepdims=True)
    # Backpropagation
    delta3 = probabs
    delta3[range(n_example), y] -= 1
    dW2 = (aa1.T).dot(delta3)
    db2 = np.sum(delta3, axis=0, keepdims=True)
    delta2 = delta3.dot(W2.T) * (1 - np.power(aa1, 2))
    dW1 = np.dot(X.T, delta2)
    db1 = np.sum(delta2, axis=0)
    dW2 += r_lam * W2
    dW1 += r_lam * W1
    # Gradient descent parameter update
    W1 += -learn_rate * dW1
    b1 += -learn_rate * db1
    W2 += -learn_rate * dW2
    b2 += -learn_rate * db2
    # Assign new parameters to the model
    model = { 'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
  print "Loss after iteration %i: %f" %(i, calculate_loss(model))
  return model
build_model(500, num_passes=20000, print_loss=False)
