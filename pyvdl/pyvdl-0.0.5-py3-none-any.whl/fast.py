try :
    from numba import njit,prange
except ImportError as e :
    print("install <numba> module")
    raise e
if __name__=='__main__' :
    pass
else :
    from .libs import *


# @njit(parallel=True)
# def test(n1, n2):
#    w = 0
#    for i in prange(n2):
#        w += n1
#    return w
# print(test(5, 25))
def f(x,y) :
    i = x if x > 0 else -x
    j = y if y > 0 else -y
    return (i + j) // 2


def fastRender(f,width,heigth,x=0,y=0) :
    f = njit(f)

    @njit(parallel = True)
    def body() :
        w = np.empty((heigth,width))
        for j in prange(width) :
            for i in prange(heigth) :
                w[i,j] = int(f(i - width / 2 + x,j - heigth / 2 + y))
        return w

    return body


def toRgb(col) :
    w = np.empty((len(col),len(col[0])),dtype = tuple)
    for i in range(len(col)) :
        for j in range(len(col[1])) :
            c = col[i,j]
            w[i,j] = c,c,c
    return w
# r = fastRender(f, 250, 250)() # syntax: vl.fastRender(func, width, heigth, x=0, y=0)()
# r = toRgb(r)
# cv2.imwrite("test.png", r)

# cv2.error: OpenCV(4.6.0) :-1: error: (-5:Bad argument) in function 'imwrite'
# > Overload resolution failed:
# >  - img data type = 17 is not supported
# >  - Expected Ptr<cv::UMat> for argument 'img'
