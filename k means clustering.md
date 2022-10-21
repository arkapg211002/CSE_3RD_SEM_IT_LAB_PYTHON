## Write a script in Python for Normal Data Point clustering.
```python
'''
Write a script in Python for Normal Data Point clustering.
'''

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample data
centers = [[1, 1], [-1, -1], [1, -1]]
X, labels_true = make_blobs(n_samples=300, centers=centers, cluster_std=0.5,
                            random_state=0)

# Compute clustering with Means
k_means = KMeans(init='k-means++', n_clusters=3, n_init=10)
k_means.fit(X)
k_means_labels = k_means.labels_
k_means_cluster_centers = k_means.cluster_centers_
k_means_labels_unique = np.unique(k_means_labels)

# Plot result
colors = ['#4EACC5', '#FF9C34', '#4E9A06']
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
for k, col in zip(range(len([[1, 1], [-1, -1], [1, -1]])), colors):
    my_members = (k_means_labels == k)
    cluster_center = k_means_cluster_centers[k]
    ax.plot(X[my_members, 0], X[my_members, 1], 'w',
            markerfacecolor=col, marker='.')
    ax.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
            markeredgecolor='k', markersize=6)
ax.set_title('KMeans')
ax.set_xticks(())
ax.set_yticks(())
plt.show()


```
![output]()
