import numpy as np
marks = np.array([
    [80,70,90],
    [60,75,85],
    [90,88,86],
    [70,60,65]
])
names = ['A', 'B', 'C', 'D']
avg = np.mean(marks, axis=1)
for i in range(len(avg)):
    print(f"Student {names[i]} average :", avg[i])
    if avg[i]>=85:
        print('result : passed ✅',avg[i])
    else:
        print('result :failed ❌',avg[i])
topper = np.argmax(avg)
print("Topper is:", names[topper])





