import sys
import pprint
from KMeansAlg import *


def main():
    k_means_algorithm(3, 600)
    # compare_output()

def compare_output():
    file_name = "output_3.txt"
    vectors = []
    with open(file_name, 'r') as file:
        # Read the entire content of the file into a string
        arr = [line.rstrip().split(",") for line in file.readlines()]
        vectors = [[float(item) for item in vector] for vector in arr]
    print(vectors)
    vectors2 = k_means_algorithm(15, 300)
    flag2 = True
    for i in range(len(vectors)):
        for j in range(len(vectors[i])):
            if not vectors[i][j] == vectors2[i][j]:
                print("Ido is a bitch")
                flag2 = False
    if flag2:
        print("Ido is still a bitch")
            # print(vectors2[i][j])
        # print(vectors[i] == vectors2[i])


if __name__ == "__main__":
    main()


