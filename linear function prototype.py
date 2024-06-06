import math
import random

#initial input of guess for two parameters
p1 = float(input("Type in parameter 1 guess"))
p2 = float(input("Type in parameter 2 guess"))

x = [0,1,2,3,4,5]
y = [0,0,0,0,0,0]
ny = [0,0,0,0,0,0]

#draw linear function
def linear_function(x_axis):
    for i in range(len(x_axis)):
        y_axis = p1 + p2*i
        y[i] = y_axis
        
linear_function(x)
print("x =",x)
print("y =",y)

#target function
tp1 = -7
tp2 = 8
ty = [0,0,0,0,0,0]
def t_linear_function(x_axis):
    for i in range(len(x_axis)):
        y_axis = tp1 + tp2*i
        ty[i] = y_axis
t_linear_function(x)

#cost function
def cost_function(i1,j1,i2,j2):
    return math.sqrt((i1-j1)**2) + math.sqrt((i2-j2)**2)
L0 = cost_function(float(y[1]),float(ty[1]),float(y[2]),float(ty[2]))

print("target y =",ty)
print("cost function = ",L0)

#random step
delta1 = random.randint(-2,2)
delta2 = random.randint(-2,2)

np1 = p1 + delta1
np2 = p2 + delta2

#new linear function with loss L1
def new_linear_function(x_axis):
    for i in range(len(x_axis)):
        y_axis = np1 + np2*i
        ny[i] = y_axis
new_linear_function(x)
L1 = cost_function(float(ny[1]),float(ty[1]),float(ny[2]),float(ty[2]))

print("New y =", ny)
print("New cost function =",L1)


#iterate random walk
while L1 > 0:
    if L1 >= L0:
        delta1 = random.randint(-2,2)
        delta2 = random.randint(-2,2)
        np1 = p1 + delta1
        np2 = p2 + delta2
        new_linear_function(x)
        L1 = cost_function(float(ny[1]),float(ty[1]),float(ny[2]),float(ty[2]))
    else:
        p1 = np1
        p2 = np2
        delta1 = random.randint(-2,2)
        delta2 = random.randint(-2,2)
        np1 = p1 + delta1
        np2 = p2 + delta2
        new_linear_function(x)
        L0 = L1
        L1 = cost_function(float(ny[1]),float(ty[1]),float(ny[2]),float(ty[2]))
        print("New parameters =", "p1 =", np1, "p2 =", np2)
        print("New cost function =",L1)
        
print("Best guess parameters are:",
      "p1 =", np1,
      "p2 =", np2
      )
print("Actual parameters are:",
      "p1 =", tp1,
      "p2 =", tp2
      )

        

    
   
    


      
