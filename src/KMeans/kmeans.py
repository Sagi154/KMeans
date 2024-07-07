import math
import sys

EPSILON = 0.001


class Cluster:
    def __init__(self, centroid: list):
        self.sum: list = [0.0 for i in range(len(centroid))]
        """
        sum of vector's coordinates
        """
        self.centroid: list = centroid
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
            new_centroid[i] = float(self.sum[i]) / self.size
        self.centroid = new_centroid

    def set_centroid(self, new_centroid):
        self.centroid = new_centroid

    def reset_sum_and_size(self):
        self.sum = [0 for i in range(len(self.centroid))]
        self.size = 0

    def calculate_euclidean_distance(self, vect_xi):
        sum = 0
        for i in range(len(vect_xi)):
            sum += math.pow(vect_xi[i] - self.centroid[i], 2)
        return math.sqrt(sum)

    def __repr__(self):
        return str(self.centroid)


def initialize_centroids(vect_arr, K):
    clusters = [Cluster(vect_arr[i]) for i in range(K)]
    return clusters


def read_input(file_name):
    with open(file_name, 'r') as file:
        # Read the entire content of the file into a string
        arr = [line.rstrip().split(",") for line in file.readlines()]
        vectors = [[float(item) for item in vector] for vector in arr]
        return vectors


def validity_check(file_name, K, iter_limit=200):
    if not 1 < iter_limit < 1000:
        print("Invalid maximum iteration!")
        return 0
    vectors = read_input(file_name)
    vectors_count = len(vectors)
    if not 1 < K < vectors_count:
        print("Invalid number of clusters!")
        return 0
    return vectors


def k_means_algorithm(vectors, K, iter_limit=200):
    clusters = initialize_centroids(vectors, K)
    """
    Initialize starting K clusters
    """
    iter_number = 0
    flag = False
    while iter_number <= iter_limit and not flag:
        iter_number += 1
        for xi in vectors:
            """
            Assign every xi to the closest cluster k
            """
            min_cluster: Cluster = calculate_closest_cluster(clusters, xi)
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
            cluster.reset_sum_and_size()
    if flag:
        for cluster in clusters:
            cluster.set_centroid([float("%.4f" % xi) for xi in cluster.get_centroid()])
        centroids = [cluster.get_centroid() for cluster in clusters]
        return centroids


def calculate_closest_cluster(clusters, vect_xi):
    min_eucledian_distance = sys.maxsize
    min_cluster = None
    for cluster in clusters:
        temp_ed = cluster.calculate_euclidean_distance(vect_xi)
        if temp_ed < min_eucledian_distance:
            min_eucledian_distance = temp_ed
            min_cluster = cluster
    return min_cluster


def parse_arguments():
    if len(sys.argv) == 4:
        K = int(sys.argv[1])
        iter_limit = int(sys.argv[2])
        file_name = sys.argv[3]
        return K, iter_limit, file_name
    elif len(sys.argv) == 3:
        K = int(sys.argv[1])
        file_name = sys.argv[2]
        iter_limit = 200
        return K, iter_limit, file_name


def main():
    K, iter_limit, file_name = parse_arguments()
    try:
        vectors = validity_check(file_name, K, iter_limit)
        if vectors == 0:
            return
        centroids = k_means_algorithm(vectors, K, iter_limit)
        for centroid in centroids:
            print(",".join(str(element) for element in centroid))
    except Exception as e:
        # print(f"error: {e}")
        print("An Error Has Occurred")


if __name__ == "__main__":
    main()
