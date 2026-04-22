from sklearn. cluster import KMeans
import numpy as np

X = np.array([[1,40],
              [2,50],
              [3,60],
              [4,65],
              [7,88],
              [8,90],
              ])


model = KMeans(n_clusters=3)
model.fit(X)

for i in range (len(X)):

    print(f'student{i+1} -> Group {model.labels_[i]}')

print(model.cluster_centers_)















