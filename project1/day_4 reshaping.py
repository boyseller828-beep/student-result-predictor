import numpy as np
#1D array to 2D array



n = np.array([5,10,15,20,25,30])
print('1D array :',n)
#reshape
reshaping=n.reshape(2,3)
print('reshaped array (two dimentional) =\n',reshaping)
print('--------------------------------')
#reshaping 3D array to 1D array
n = np.array([[[5,10,15],[20,25,30]],[[35,40,45],[50,55,60]]])
print('3D array = \n',n)
rearr=n.reshape(-1)
print(rearr)
print('---------------------------------')




























