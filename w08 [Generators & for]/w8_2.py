def my_fib(n):
    if n > 0:
        a_k = 1
        yield a_k
        if n > 1:
            b_k = 1
            yield b_k
            if n > 2:
                k = 2
                while k != n:
                    c_k = a_k + b_k
                    yield c_k
                    a_k, b_k = b_k, c_k
                    k += 1


for i in my_fib(0):
    print(i)