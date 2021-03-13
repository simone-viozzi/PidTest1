import math
import numpy as np
import matplotlib.pyplot as plt


class Pid:
    k = 0
    ki = 0
    kd = 0
    
    oldInput = 0
    integral = 0
    
    def __init__(self, k, kc, kd):
        self.k = k
        self.kc = kc
        self.kd = kd
    
    def control(self, curr_input):
        derived = curr_input - self.oldInput
        self.integral += curr_input
        
        self.oldInput = curr_input
        
        return self.k * curr_input + self.kc * derived + self.ki * self.integral
        


if __name__ == '__main__':
    print("hello py")
    np.random.seed(19680801)
    
    steps = np.arange(0, 10, 0.01)
    
    sinValues = [math.sin(s) for s in steps]
    nse = (np.random.randn(len(steps)) / 10)
    
    p = Pid(0.01, 0.1, 0.001)
    
    outputs = []
    
    for s in range(len(steps)):
        inputValue = sinValues[s] + nse[s]
        
        control = p.control(inputValue)
        
        output = inputValue - control
        outputs.append(output)
    
    plt.plot(steps, (sinValues + nse))
    plt.show()
    
    plt.plot(steps, (sinValues + nse), steps, outputs)
    plt.show()
