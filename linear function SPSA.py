import numpy as np
import random

d = int(input("Enter a number of data points: "))
p = 2

np.random.seed(314159)
x = np.arange(d)
yt = 1 + 2*x + np.random.randn(len(x))

#initialize parameters
theta = np.array([4,5])

#initialize meta-parameters
a = 0.2
c = 0.2
A = 1
alpha = 0.602
gamma = 0.101

#function(for now just a linear function)
def feval(_theta_):
    return _theta_[0] + _theta_[1]*x
        
#loss function
def loss(_theta_):
    yp = feval(_theta_)
    cost = ((yt - yp)**2)/(2*d)
    return np.sum(cost)/d
print(loss(theta))

#SPSA algorithm
n = int(input("How many iterations do you want to perform?"))

for k in range(n):
    ak = a/(A+k+1)**alpha
    ck = c/(k+1)**gamma
    delta = np.ones(p) - 2*(np.random.randint(1,3,p) -1)
    thetaplus = theta + ck*delta
    thetaminus = theta - ck*delta
    yplus = loss(thetaplus)
    yminus = loss(thetaminus)
    ghat = (yplus - yminus)/(2*ck*delta)
    theta = theta - ak*ghat
    print(theta)
    
