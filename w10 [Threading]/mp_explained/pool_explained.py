from multiprocessing import Pool


def cube(x):
    return x**3


if __name__ == '__main__':
    pool = Pool(processes=4)  # создаем пул из 4 процессов
    # в apply можно передать несколько аргументов
    results = [pool.apply(cube, args=(x,)) for x in range(1,7)]  # раскидываем числа от 1 до 7 по 4 процессам
    print(results)

    pool = Pool(processes=4)
    # то же самое, но с map. разбивает итерируемый объект (range(1,7)) на chunks и раскидывает аргументы по процессам
    results = pool.map(cube, range(1,7))
    print(results)

    pool = Pool(processes=4)
    results = [pool.apply_async(cube, args=(x,)) for x in range(1,7)]
    output = [p.get() for p in results]
    print(output)