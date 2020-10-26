import numpy as np
import my_mathematics.math as my


def test_sin():
    assert my.MyMath.sin(np.pi) == np.sin(np.pi)
    assert my.MyMath.sin(np.pi/2) == np.sin(np.pi/2)