
from sklearn.cluster import KMeans
import numpy as np

#data:hours studied
x = np.array([[1],[2],[3],[54],[78],[87],[124]])
model = KMeans(n_clusters=3, random_state=42)
model.fit(x)

labels = model.labels_
print("Clusters:", labels)





















