import numpy as np
from matplotlib import pyplot as plt

def linearRegression(alpha = 0.01, num_iters = 400):
    data = np.loadtxt("data.txt", delimiter=",", dtype=np.float64)
    y = data[:, -1]
 #   print(" y : ", y)
    parameterData = data[:, 0:-1]
#    print("before parameterData : ", parameterData)
    normalizationData = normalization(parameterData)

#    print("parameterData : \n", parameterData)
#    print("normalizationData : \n", normalizationData)

def normalization(data): 
    dataArr = np.array(data)

    col = dataArr.shape[1]  # total number of cols

    averageEachCol = np.array((1, col))
    sigmaEachCol = np.array((1, col))       # standard deviation

    averageEachCol = np.mean(dataArr, 0)    # second parameter 0 is column ,
# 1 is row
    sigmaEachCol = np.std(dataArr, 0)

    for i in range(col):
        dataArr[:, i] = (dataArr[:, i] - averageEachCol[i])/sigmaEachCol[i]

    return dataArr

def main():
    linearRegression(0.01, 400)


if __name__ == "__main__":
    main()
