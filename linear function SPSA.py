import math
import random

#test data points (true y values)
x = [0,1,2,3,4,5]
yt = [1,3,5,7,9,11]

#predicted y value
yp = [0,0,0,0,0,0]

#initialize parameters
theta = [2,3]

#initialize meta-parameters
a = 0.2
c = 0.2
A = 1
alpha = 1
gamma = 1.5

#function(for now just a linear function)
def feval(x_axis,_theta_):
    for i in range(len(x)):
        y_axis = _theta_[0] + _theta_[1]*i
        yp[i] = y_axis
        
#loss function
def loss(_theta_):
    feval(x,_theta_)
    for i in range(len(x)):
        cost = 0
        count = 0
        cost += math.sqrt((yp[i] - yt[i])**2)
        count += 1
    return cost/count

#SPSA algorithm
n = int(input("How many iterations do you want to perform?"))

for k in range(n):
    ak = a/(A+k+1)**alpha
    ck = c/(k+1)**gamma
    #randomly generate components of delta vector
    delta = [0,0]
    for i in range(len(delta)):
        randint = random.randint(-1,1)
        while randint == 0:
            randint = random.randint(-1,1)    
        delta[i] = randint
    #gradient estimation
    thetaplus = [0,0]
    thetaminus = [0,0]
    for i in range(len(delta)):
        thetaplus[i] = theta[i] + ck*delta[i]
        thetaminus[i] = theta[i] - ck*delta[i]
    yplus = loss(thetaplus)
    yminus = loss(thetaminus)
    ghat = [0,0]
    for i in range(len(ghat)):
        ghat[i] = (yplus - yminus)/(2*ck*delta[i])
    #updating theta estimate
    for i in range(len(theta)):
        theta[i] = theta[i] - ak*ghat[i]
    
    print("theta:", theta,'"correct" theta: [1,2]', "ak:", ak,"ck:",ck)
    
    
