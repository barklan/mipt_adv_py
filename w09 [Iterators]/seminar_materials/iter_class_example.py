class MyVectorIterator:
    def __init__(self, x, y, z):
        self.__coords = [x, y, z]
        self._pos = -1

    def __iter__(self):
        return self

    def __getitem__(self, index):
        return self.__coords[index]

    def __setitem__(self, index, new_value):
        if type(new_value) not in (int, float):
            raise ValueError('Not a number')
        self.__coords[index] = new_value

    def __next__(self):
        if self._pos == 2:
            raise StopIteration()
        self._pos += 1
        return self.__coords[self._pos]


v = MyVectorIterator(1, 2, 3)
for coord in v:
    print(coord)

print('x coordinate is:', v[0])
print('z coordinate is:', v[2])
v[2] = 'abc'
print('z coordinate is:', v[2])

