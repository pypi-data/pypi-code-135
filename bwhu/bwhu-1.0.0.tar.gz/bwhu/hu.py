def body():
    print('May I into your body?')
    import time
    lst = ["@@", "#", "/%", "***"]
    for i in range(40):
        j = i % 4
        print("\b" + lst[j], end="")
        time.sleep(0.3)
    print('\n')
    time.sleep(2)
    print('COME!')
    time.sleep(1)
    print('IN!')
    time.sleep(1)
    print('NOW!')


def soul():
    print('May I into your soul?')
    import time
    lst = ["\\", "|", "/", "———"]
    for i in range(40):
        j = i % 4
        print("\b" + lst[j], end="")
        time.sleep(0.3)
    print('\n')
    time.sleep(2)
    print('YES!')
    time.sleep(1)
    print('YES!')
    time.sleep(1)
    print('YES!')

def myheart():
    import numpy as np
    import matplotlib
    matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt
    import math
    from tqdm import trange
    import time
    for i in trange(10):
        time.sleep(1)

    pi = math.pi

    x = np.linspace(-3.3 ** 0.5, 3.3 ** 0.5, 6001).reshape(-1, 1)
    y = (x ** 2) ** (1 / 3) + 0.9 * np.sqrt(3.3 - x ** 2) * np.sin(40 * pi * x)

    plt.plot(x, y, color='r')
    plt.xlim(-3, 3)
    plt.axis('off')
    frame = plt.gca()
    # y 轴不可见
    frame.axes.get_yaxis().set_visible(False)
    # x 轴不可见
    frame.axes.get_xaxis().set_visible(False)
    plt.savefig('心形波浪')

    plt.show()