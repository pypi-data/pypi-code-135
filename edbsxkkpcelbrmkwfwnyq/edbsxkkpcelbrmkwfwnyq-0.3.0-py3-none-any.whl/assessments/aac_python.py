from testing import submission
import random

def test():

    a = random.random()
    b = random.random()
    assert submission.my_math.add( a, b ) == a+b
    assert submission.my_math.add(4,5) == 9
    assert submission.my_math.add(-1.2, 1.0) == -0.2

