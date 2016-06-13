import numpy as np
# -*- coding: utf-8 -*-

def upgma():

    length = 4
    nan = float("inf")
    # default data set
    distance = np.array([[nan, 0.10, 0.12, 0.21],[0.10, nan, 0.04, 0.13],[0.12, 0.04, nan, 0.11],[0.21, 0.13, 0.11, nan]], dtype = np.float64)
    print distance, '\n'

    min_d = np.zeros(length - 1).reshape(3,1)
    count = 0
    while count < length - 2:
        min_d[length - 2 - count] = np.min(distance) / 2
        min_d_index = np.argmin(distance)
        print min_d, '\n'

        for i in range(length - count):
            if i == min_d_index / (length - count) or i == min_d_index % (length - count):
                distance[i] = (distance[ min_d_index / (length - count) : min_d_index / (length - count) + 1] + distance[ min_d_index % (length - count) : min_d_index % (length - count) + 1 ]) / 2
                break
        for i in range(length - count):
            if i == min_d_index / (length - count) or i == min_d_index % (length - count):
                distance[:, i:i+1] = (distance[0:(length - count), min_d_index / (length - count) : min_d_index / (length - count) + 1] + distance[0:(length - count), min_d_index % (length - count) : min_d_index % (length - count) + 1]) / 2
                break
        distance = np.delete(distance, min_d_index % (length - count), 0)
        distance =  np.delete(distance, min_d_index % (length - count), 1)
        print distance, '\n'
        count += 1

    min_d[length - 2 - count] = np.min(distance) / 2
    print min_d


if __name__ == "__main__":
    upgma()