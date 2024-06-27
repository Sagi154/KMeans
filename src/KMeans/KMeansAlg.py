import math

EPSILON = 0.0001

class Cluster:
    def __init__(self, centroid):
        self.sum = 0
        """
        sum of vector's coordinates
        """
        self.centroid = centroid
        self.size = 0
        """
        temp size for each rotation
        """

    def get_size(self):
        return self.size

    def get_sum(self):
        return self.sum

    def get_centroid(self):
        return self.centroid

    def set_size(self, new_size):
        self.size = new_size

    def set_sum(self, new_sum):
        self.sum = new_sum

    def add_xi(self, vect_xi):
        for i in range(len(vect_xi)):
            self.sum[i] += vect_xi[i]
        self.size += 1

    def update_centroid(self):
        new_centroid = [0 for i in range(len(self.centroid))]
        for i in range(len(self.sum)):
            new_centroid[i] = self.sum[i] / self.size
        self.centroid = new_centroid

    def set_centroid(self, new_centroid):
        self.centroid = new_centroid

    def reset_sum_and_size(self):
        self.sum = [0 for i in range(len(self.centroid))]
        self.size = 0


    def calculate_euclidean_distance(self, vect_xi):
        sum = 0
        for i in range(len(vectXi)):
            sum += Math.pow(vectXi[i] - self.centroid[i])
        return math.sqrt(sum)

def initialize_centroids(vect_arr, K):
    clusters = [Cluster(vectArr[i]) for i in range(K)]
    return clusters

def k_means_algorithm(vect_arr, K, iter_limit = 200):
    clusters = initialize_centroids(vectArr, K)
    """
    Initialize starting K clusters
    """
    iter_number = 0
    flag = False

    while iter_number <= iterLimit and not flag:
        iter_number += 1
        for xi in vectArr:
            """
            Assign every xi to the closest cluster k
            """
            min_cluster: Cluster = calculateClosestCluster(clusters, xi)
            min_cluster.add_xi(xi)
        flag = True
        # Update centroids
        for cluster in clusters:
            """
            Update the centroids and check for convergence
            """
            prev_cluster_centroid = cluster.get_centroid()
            cluster.update_centroid()
            if flag:
                convergence = cluster.calculate_euclidean_distance(prev_cluster_centroid)
                if convergence >= EPSILON:
                    flag = False


def calculate_closest_cluster(clusters, vect_xi):
    min_eucledian_distance = sys.maxint
    min_cluster = None
    for cluster in clusters:
        temp_ed = cluster.calculate_euclidean_distance(vectXi)
        if temp_ed < min_eucledian_distance:
            min_eucledian_distance = temp_ed
            min_cluster = cluster
    return min_cluster


