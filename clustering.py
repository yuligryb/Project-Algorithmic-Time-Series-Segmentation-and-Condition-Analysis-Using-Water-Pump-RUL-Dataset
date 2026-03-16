import numpy as np

def split_cluster(data,indices):

    center = np.mean(data,axis=0)

    dist = np.linalg.norm(data-center,axis=1)

    median = np.median(dist)

    left = indices[dist <= median]
    right = indices[dist > median]

    if len(left) == 0:
        left = indices[:len(indices) // 2]
        right = indices[len(indices) // 2:]

    return left,right

def recursive_cluster(data,k):

    clusters = [np.arange(len(data))]

    while len(clusters) < k:

        new_clusters = []

        for cluster_indices in clusters:

            subset = data[cluster_indices]
            left,right = split_cluster(subset,cluster_indices)
            new_clusters.append(left)
            new_clusters.append(right)

        clusters = new_clusters[:k]

    return clusters