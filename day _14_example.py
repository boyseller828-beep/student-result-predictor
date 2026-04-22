from sklearn.cluster import KMeans
import numpy as np
#hours,marks
X = np.array([[1,40],
              [2,50],
              [3,55],
              [4,60],
              [5,70],
              [6,80],
              ])
model = KMeans(n_clusters=2)
model.fit(X)
print('cluster :',model.labels_)





































