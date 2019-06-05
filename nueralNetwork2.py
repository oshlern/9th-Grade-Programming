from __future__ import division
import random, math
import numpy as np
layers=[2,2,2,2,2]
X=[1,-1]
def initParams(X, layers):
    params = [np.random.randn(layers[i], layers[i-1]+1) for i in range(1, len(layers))]
    return params

def activationFunction(x):
    return (1/(1+math.exp(-x)))

def z(inputs, params):
    # print inputs, params
    return activationFunction(np.dot(inputs, params[1:])+params[0])

def out(X, layers, params):
    outputs = [X]
    for i in range(len(layers)-1):
        outputs.append([z(outputs[i], weights) for weights in params[i]])
    return outputs
params = initParams(X, layers)
print out(X, layers, params)[-1]

def cost(output, y):
    return output-y

def dz(i, params, inputs, z):
    eToDot = math.exp(-dot(inputs, params))
    return x[i] * eToDot / math.pow(1 + eToDot, 2)

# Get derivative error with respect to w[i, j]
