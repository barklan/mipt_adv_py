# Сопрограммы, coroutine, корутины
# GIL - для CPython
def sample_coroutine():
    print('Init')
    x = 0
    while True:
        # ---->
        x = yield str(x)*5
        # yield str(x)*5
        print(x)


print('initialize outside')
cor = sample_coroutine()
print('First next')
next(cor)
print('send signal')
# <----
print(cor.send(5))
next(cor)
# <----
print(cor.send(10))

