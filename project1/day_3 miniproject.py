import numpy as np

num = int(input('enter number of student '))
mark_list = []
#take mark input
for i in range(num):
    marks = float(input('enter the mark {i+1}:'))
    mark_list.append(marks)
marks = np.array(mark_list)    





print('Marks :',marks)
print('avarage :',np.mean(marks))
print('highest :',np.max(marks))
print('lowest :',np.min(marks))

















