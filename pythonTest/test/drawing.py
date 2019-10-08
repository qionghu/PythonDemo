import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np
import math



def showLinear():
    x = np.arange(1, 11)

    for index in x:
        print(x[index-1])


    y = 2 * x + 5

    # title and description on the interface
    plt.title("straight line")
    plt.xlabel("x axis caption")
    plt.ylabel("y axis caption")

    plt.plot(x, y, 'vm')
    plt.show()

def showSineCurve():
    x = np.arange(0, 3 * np.pi, 0.1)
    #for index in x:
    #    print(index)
    #print(x)
    y = np.sin(x)
        
    plt.title("sine curve")
    plt.xlabel("x axis")
    plt.ylabel("y axis")

    plt.plot(x, y)
    plt.show()
         
def showMultiMap():
    x = np.arange(0, 3*2*np.pi, 0.05)

    y_sin = np.sin(x)
    y_cos = np.cos(x)

    plt.subplot(2, 1, 1)
    plt.plot(x, y_sin)
    plt.title('Sine')

    plt.subplot(2, 1, 2)
    plt.plot(x, y_cos)
    plt.title('Cosine')

    plt.show()

def showBar():
    x = [4, 7, 11]
    x_2 = [5, 8, 12]

    y = [12, 13, 18]
    y_2 = [3, 9, 26]

    plt.bar(x, y, align = 'center')
    plt.bar(x_2, y_2, color = 'r', align = 'center')

    plt.title('bar graph')

    plt.show()

def showHistogram():
    a = np.random.random(size=100)
    # print('before a : ', a)
    a =  map(lambda x: math.floor(x*100) , a)
    a = list(a)
    np.histogram(a, bins = [0,20,40,60,80,100])
    hist, bins = np.histogram(a, bins = [0,20,40,60,80,100])
    print(hist)
    print(bins)
    plt.hist(a, bins=[0, 20, 40, 60, 80, 100])
    plt.title('histogram')
    plt.show()
    # a = list(a)
    # print(a)

showHistogram()

# showBar()

# showMultiMap()
        
# showSineCurve()

# showLinear()
