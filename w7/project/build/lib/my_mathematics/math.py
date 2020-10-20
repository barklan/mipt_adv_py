import numpy as np
import cmath
import math

class MyMath:
    __complex = False
    pi = np.pi

    @classmethod
    def get_nm(cls):
        return cls.__name__

    @staticmethod
    def sin(x):
        return np.sin(x)

    @classmethod
    def get_complex(cls):
        return cls.__complex

    @classmethod
    def sqrt(cls, x):
        if cls.get_complex():
            result = cmath.sqrt(x)
            return result.real, result.imag
        else:
            if x < 0:
                raise ValueError("Hey, you are working with real valued math!")
            if x >= 0:
                return np.sqrt(x)




class MyComplexMath(MyMath):
    __complex = True

    @classmethod
    def get_complex(cls):
        return cls.__complex



