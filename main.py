# use: plot values of time and place and calculate acceleration plot
import matplotlib.pyplot as plt
import numpy as np

# initialization of values
t_values = [0, 1, 3]
x_values = [5, 5, 65]

# initialization of acceleration function
def func_x_acc(t,x_0,v_0,a):
    return x_0 + v_0*t + 0.5 * a * t * t

def func_v(t,v_0,a):
    return v_0 + a * t

t_eval = np.linspace(0,3,100) # 100 datapoints between 0 and 3

plt.plot(t_eval,func_x_acc(t_eval,5.,-10.,20.))
plt.scatter(t_values,x_values,marker='x',color='red')
plt.xlabel('t in s')
plt.ylabel('x in m')
plt.title('t-x-plot')
#plt.savefig('x_vs_t_uniformAcceleration.png') #uncomment this line to save png file locally
plt.show()

plt.plot(t_eval,func_v(t_eval,-10.,20.))
plt.xlabel('t in s')
plt.ylabel('v in m/s')
plt.title('t-v-diagram')

plt.show()
