from __future__ import division
import random, math
import numpy as np
layers=[2,2,2]
X=[1,-1]
def initParams(X, layers):
    layers = [len(X)] + layers
    # params = np.random.randn(layers[i], layers[i-1]+1) for i in range(1, len(layers))]
    for i in range(1, len(layers)):
        params += [[[random.random()] * layers[i-1]] * layers[i]]
    return params

def activationFunction(x):
    return (1/(1+math.exp(-x)))

def dot(x, y):
    if len(x) != len(y):
        print "No bueno dot product inputs! " + str(x) + " _and_ " + str(y)
        return
    total = 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return total

def z(inputs, params):
    return activationFunction(dot(inputs, params))

def run(X, layers, params):
    inputs, outputs = X, []
    for i in range(len(layers)):
        outputs = []
        for j in range(layers[i]):
            outputs += [z(inputs, params[i][j])]
        inputs = outputs
    return outputs
params = initParams(X, layers)
print run(X, layers, params)

def cost(output, y):
    return output-y

def dz(i, params, inputs, z):
    eToDot = math.exp(-dot(inputs, params))
    return x[i] * eToDot / math.pow(1 + eToDot, 2)

# Get derivative error with respect to w[i, j]
