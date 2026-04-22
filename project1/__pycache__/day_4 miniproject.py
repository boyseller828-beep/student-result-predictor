import numpy as np
#generate marks for 5 students
subjects = ['Science', 'Maths', 'English']
marks = np.random.randint(50,100,size=(5,3))
print("Marks:\n",marks)                          

print('Average marks per student :', np.mean(marks,axis =1))
avr_subject = np .mean(marks,axis=0
)
top_student = np.argmax(np.mean(marks, axis=1))
print("Top student index:", top_student)
for i in range(len(subjects)):
    print(subjects[i],':',avr_subject[i])
print('Highest marks',np.max(marks))
print('lowest marks',np.min(marks))























