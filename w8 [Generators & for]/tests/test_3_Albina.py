import sys, random
sys.path.append('..')
from w8_3 import my_zip, my_map, my_enumerate


def square(value):
    return value * 2

def test_for_zip(data1, data2):
    for i in range(5):
        list_zip = []
        list_my_zip = []
        for values in zip(data1[i:], data2[i:]):
            list_zip.append(values)
        for values in my_zip(data1[i:], data2[i:]):
            list_my_zip.append(values)
        assert list_my_zip == list_zip

def test_for_zip2(data1, data2, data3):
    for i in range(5):
        list_zip = []
        list_my_zip = []
        for values in zip(data1[:i], data2[:i], data3[:i]):
            list_zip.append(values)
        for values in my_zip(data1[:i], data2[:i], data3[:i]):
            list_my_zip.append(values)
        assert list_my_zip == list_zip

def test_for_map(data1, data2, data3):
    for i in data1, data2, data3:
        list_map = list(map(square, i))
        list_my_map = list(my_map(square, i))
        assert list_map == list_my_map

def test_for_enumerate(data1, data2, data3):
    for data in data1, data2, data3:
        j = random.randint(0, 1000)
        list_enum, list_my_enum = [], []
        for num, item in enumerate(data, j):
            list_enum.append([num, item])
        for num, item in my_enumerate(data, j):
            list_my_enum.append([num, item])
        assert list_my_enum == list_enum
