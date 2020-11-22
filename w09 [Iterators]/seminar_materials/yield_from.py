def generator1():
    for i in range(5):
        yield "Generator 1: {}".format(i)

def generator2():
    for i in range(5):
        yield "Generator 2: {}".format(i)

def generator():
    # for i in generator1():
    #     yield i
    # for i in generator2():
    #     yield i
    yield from generator1()
    yield from generator2()

for i in generator():
    print(i)

