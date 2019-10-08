import matplotlib as mpl
mpl.use('TKAgg')
import matplotlib.pyplot as plt
import numpy as np

def test():
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2*np.pi*t)
    plt.plot(t, s)

    plt.title('About as simple as it gets , folks')
    plt.show()

def test_2():
    random_arr4 = np.random.random(12)
    print(random_arr4)

def test_np_type():


# test()
