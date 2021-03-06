import numpy as np # linear algebra
import math

class LogisticRegressionModel:
    def __init__(self, inputSize = 2, learningRate = 0.1):
        self.W = np.random.randn(inputSize)
        self.b = np.random.randn()
        self.dW = np.zeros(self.W.shape)
        self.db = 0.
        self.X = np.zeros(self.W.shape)
        self.Y = 0.
        self.A = 0.
        self.learningRate = learningRate
        self.loss = 0.
        
    def sigmoid(self, x):
        return 1 / (1 + math.e ** (-x))
    
    def forward(self, X):
        self.X = X
        self.A = self.sigmoid(np.dot(self.W.T, self.X) + self.b)
        return self.A
    
    def clear_grad(self):# of no use currently
        self.dW = np.zeros(self.W.shape)
        self.db = 0
        
    def compute_loss(self, Y):
        self.Y = Y
        self.loss = self.Y * np.log(self.A) + (1 - self.Y) * np.log(1 - self.A)
        return self.loss
    
    def backward(self):
        self.dW = (self.A - self.Y) * self.X
        self.db = (self.A - self.Y)
        
    def optimize(self):
        self.W = self.W - self.learningRate * self.dW
        self.b = self.b - self.learningRate * self.db
        
        
# demonstration
model = LogisticRegressionModel()
model.forward(np.array([1, 2]))
print(model.A, model.W, model.dW, model.b, model.db)
model.compute_loss(1)
print(model.loss)
model.backward()
print(model.A, model.W, model.dW, model.b, model.db)
model.optimize()
print(model.A, model.W, model.dW, model.b, model.db)
