import pytest
import random

@pytest.fixture()
def data1():
    return ["Alex", "Bob", "Alice", "John", "Ann"]

@pytest.fixture()
def data2():
    return [25, 17, 34, 24, 42]

@pytest.fixture()
def data3():
    return ["M", "M", "F", "M", "F"]

@pytest.fixture()
def big_datas():
    big_array = []
    n1 = random.randint(1, 10)
    for p in range (n1):
        array = []
        n2 = random.randint(1, 10)
        array = [[] for k in range(n2)]
        for k in range (n2):
            n3 = random.randint(1, 10)
            for j in range (n3):
                    array[k].append(random.randint(1, 1000))
        big_array.append(array)
    return big_array