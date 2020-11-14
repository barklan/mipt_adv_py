# Сопрограммы, coroutine, корутины
# GIL - для CPython
class SpecialFormatException(Exception):
    pass
def sample_coroutine():
    x = 0
    mode = 1
    while True:
        try:
            if mode == 1:
                x = yield str(x)*5
            elif mode == 2:
                x = yield 'Original yield: {0} --- {0}'.format(str(x)*5)
            print(x)
        except SpecialFormatException:
            mode = 2
            x = yield 'Pathetic parody: {0} --- {0}'.format(str(x)*5)
            print(x)


cor = sample_coroutine()
next(cor)
print(cor.send(5))
print(cor.throw(SpecialFormatException()))
print(cor.send(10))
print(cor.send(20))
cor.close()
print(cor.send(30))

