import random
import numpy as np

class Network(object):

    def __init__(self, layers):
        """The list ``layers`` contains the number of neurons in the
        respective layers of the network.  For example, if the list
        was [2, 3, 1] then it would be a three-layer network, with the
        first layer containing 2 neurons, the second layer 3 neurons,
        and the third layer 1 neuron.  The biases and weights for the
        network are initialized randomly, using a Gaussian
        distribution with mean 0, and variance 1.  Note that the first
        layer is assumed to be an input layer, and by convention we
        won't set any biases for those neurons, since biases are only
        ever used in computing the outputs from later layers."""
        self.num_layers = len(layers)
        self.layers = layers
        self.weights = [np.random.randn(layers[i], layers[i-1] + 1) for i in range(1, len(layers))]

    def feedforward(self, X):
        """Return the output of the network if ``a`` is input."""
        outputs = [X]
        for i in range(self.num_layers-1):
            outputs.append([z(outputs[i], w) for w in self.weights[i]])
        return outputs

    def backprop(self, x, y):
        """Return a tuple ``(nabla_b, nabla_w)`` representing the
        gradient for the cost function C_x.  ``nabla_b`` and
        ``nabla_w`` are layer-by-layer lists of numpy arrays, similar
        to ``self.biases`` and ``self.weights``."""
        newW = [np.zeros(w.shape) for w in self.weights]
        activations = self.feedforward(x)
        delta = np.dot(dCost(activations[-1], y), activations[-1])
        newW[-1] = np.concatenate((np.ones(len(activations[-2])), activations[-2]))
        for i in xrange(2, self.num_layers):
            print self.weights[-i+1]
            print delta
            sigPrime = [dSigmoid(activation) for activation in activations[-i + 1]]
            print sigPrime
            print np.dot(self.weights[-i + 1].transpose(), delta)
            # print sigPrime
            # print np.dot(self.weights[-i + 1].transpose(), delta)
            delta = np.dot(np.diag(sigPrime), np.dot(self.weights[-i + 1].transpose(), delta))
            print newW
            newW[-i] = np.dot(delta, np.concatenate(np.ones(activations[-i-1])[1].shape(), activations[-i-1]).transpose()) #bias is just delta
        return newW

    def updateBatch(self, batch, rate):
        """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The ``batch`` is a list of tuples ``(x, y)``, and ``rate``
        is the learning rate."""
        newW = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch: #can vectorize
            newW = np.add(newW, self.backprop(x, y))
        self.weights = np.subtract(w, np.dot(rate/len(batch), newW))

    def gradientDescent(self, training_data, epochs, batch_size, rate, test_data=None):
        """Train the neural network using mini-batch stochastic
        gradient descent.  The ``training_data`` is a list of tuples
        ``(x, y)`` representing the training inputs and the desired
        outputs.  The other non-optional parameters are
        self-explanatory.  If ``test_data`` is provided then the
        network will be evaluated against the test data after each
        epoch, and partial progress printed out.  This is useful for
        tracking progress, but slows things down substantially."""
        if test_data: n_test = len(test_data)
        n = len(training_data)
        for i in xrange(epochs):
            random.shuffle(training_data)
            batches = [training_data[k:k + batch_size] for k in xrange(0, n, batch_size)]
            for batch in batches: #can vectorize
                self.updateBatch(batch, rate)
            if test_data:
                print "Epoch {0}: {1} percent accuracy".format(i, self.evaluate(test_data) * 100)
            else:
                print "Epoch {0} complete".format(i)

    def evaluate(self, test_data):
        accuracy = 1.0
        for (x, y) in test_data:
            accuracy = accuracy + abs(np.subtract(self.feedForward(x)[-1], y))/y
        return accuracy/len(test_data)

def dCost(output_activations, y):
    """Return the vector of partial derivatives \partial C_x /
    \partial a for the output activations."""
    return output_activations[0] - y #fix formatting

def sigmoid(z):
    """The sigmoid function."""
    return 1.0 / (1.0 + np.exp(-z))

def dSigmoid(sigz):
    """Derivative of the sigmoid function."""
    return sigz * (1 - sigz)

def z(inputs, weights):
    return sigmoid(np.dot(inputs, weights[1:]) + weights[0])

net = Network([2, 3, 1, 1])
net.gradientDescent([[[0, 1], 1], [[1, 2], 2], [[2, 3] ,3], [[3, 4], 4]], 3, 2, 1)
