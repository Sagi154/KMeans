import sys
import pprint
from kmeans import *

FILE_PATH = "tests/tests/input_"

# 1. k=3, max_iter = 600
# 2. k=7, max_iter = not provided
# 3. k=15, max_iter = 300


def main():
    file_number = 1;
    file_name = f"{FILE_PATH}{file_number}.txt"
    k_means_algorithm(file_name,3000, 60000)
    # compare_output()

def compare_output():
    file_number = 1
    file_name = f"{FILE_PATH}{file_number}.txt"
    file_output = f"tests/tests/output_{file_number}.txt"
    vectors = []
    with open(file_output, 'r') as file:
        # Read the entire content of the file into a string
        arr = [line.rstrip().split(",") for line in file.readlines()]
        vectors = [[float(item) for item in vector] for vector in arr]
    vectors2 = k_means_algorithm(file_name, 3, 600)
    flag2 = True
    for i in range(len(vectors)):
        for j in range(len(vectors[i])):
            if not vectors[i][j] == vectors2[i][j]:
                print("Ido is a bitch")
                flag2 = False
    if flag2:
        print("Ido is still a big bitch and the code is bien")
            # print(vectors2[i][j])
        # print(vectors[i] == vectors2[i])


if __name__ == "__main__":
    main()


