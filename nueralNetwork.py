layers=[2,2,2]
neurons=[]
parameters=[]
X=[0,0]
paramaters.push([])
for i in layers:
    paramaters.push([])
def activation_function(x):
    return (1/(1+e**(-x)))
def z(inputs,params):
    return dot(inputs,params)
