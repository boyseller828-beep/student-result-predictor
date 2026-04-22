import numpy as np
#dataset
data = np.array([
    [80,70,90],
    [60,75,85],
    [90,88,86],
    [70,60,65]
])


#data analysing
print('marks :\n',data)
print('students avarage marks :',np.mean(data,axis=1))
print('subject avarage marks :',np.mean(data,axis=0))
print('highest marks :',np.max(data))
print('lowest marks :',np.min(data))


