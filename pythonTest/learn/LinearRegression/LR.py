from __future__ import print_function
import numpy as np
from matplotlib import pyplot as plt

def linearRegression(alpha=0.01, num_iters=400):
    print("加载数据...")

    data = loadtxtAndcsv_data("data.txt", ",", np.float64)  #读取数据
    X = data[:, 0:-1]  #X对应0到倒数第二列
    y = data[:, -1]     # y对应最后一列
    m = len(y)          # 总的数据条数
    col = data.shape[1] # data的列数
    
    #print("before normalization data : \n", data)

    X, mu, sigma = featureNormaliza(X)  # 归一化
    #plot_X1_X2(X)   # 画图看一下归一化效果

#    print("mu : ", mu)
#    print("sigma : ", sigma)
#    print("\n data after normalization : \n", X)

    X = np.hstack((np.ones((m, 1)), X))  # 再X前面加一列

#    print("\n 执行梯度下降算法....")

    theta = np.zeros((col, 1))
    y = y.reshape(-1, 1)    # 将行向量转化为列

    theta, J_history = gradientDescent(X, y, theta, alpha, num_iters)

    plotJ(J_history, num_iters)

    return mu, sigma, theta # 返回均值mu, 标准差 sigma, 和学习的结果 theta


# load text, csv file
def loadtxtAndcsv_data(fileName, split, dataType):
    return np.loadtxt(fileName, delimiter=split, dtype=dataType)
u
# normalization
def featureNormaliza(X):
    X_norm = np.array(X)   #将X转化为numpy数组对象， 才可以进行矩阵的运算

    mu = np.zeros((1, X.shape[1]))
    sigma = np.zeros((1, X.shape[1]))

    mu = np.mean(X_norm, 0)
    sigma = np.std(X_norm, 0)

    print("featureNormaliza mu : ", mu)
    print("featureNormaliza sigma : ", sigma)

    for i in range(X.shape[1]):
        X_norm[:, i] = (X_norm[:, i] - mu[i])/sigma[i]  
    return X_norm, mu, sigma 

# 画二维图
def plot_X1_X2(X): 
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()

# 梯度下降算法
def gradientDescent(X, y, theta, alpha, num_iters):
    m = len(y)
    n = len(theta)

    temp = np.matrix(np.zeros((n, num_iters)))
    
    J_history = np.zeros((num_iters, 1)) 

    print("gradientDescent X : ", X)

    for i in range(num_iters):
        h = np.dot(X, theta)
        print("\n grad i : ", i)
        print("\n gradientDescent h: ",h)
        temp[:, i] = theta - ((alpha/m)*(np.dot(np.transpose(X), h-y)))
        print("\n grad  temp[: , i]: ", temp[:, i])
        theta = temp[:, i]
        J_history[i] = computerCost(X, y, theta)
        print('\n J_history[i]', J_history[i])
    return theta, J_history

# 计算代价函数
def computerCost(X, y, theta):
    m = len(y)
    J = 0

    J = (np.transpose(X*theta - y))*(X*theta - y)/(2*m) #计算代价J
    return J

# 画每次迭代代价的变化图
def plotJ(J_history, num_iters):
    x = np.arange(1, num_iters+1)
    plt.plot(x, J_history)
    plt.xlabel("Iteration count")
    plt.ylabel("Generation value")
    plt.title("cost varies with the number of iterations")
    plt.show()


def testLinearRegression():
    mu, sigma, theta = linearRegression(0.01, 400)
    print("\n 计算的theta值： ", theta)
    print("\n 预测的结果：", predict(mu, sigma, theta))

def predict(mu, sigma, theta):
    result = 0

    predict = np.array([1650, 3])
    norm_predict = (predict - mu)/sigma
    final_predict = np.hstack((np.ones((1)), norm_predict))

    result = np.dot(final_predict, theta)
    return result

if __name__ == "__main__":
    testLinearRegression()

