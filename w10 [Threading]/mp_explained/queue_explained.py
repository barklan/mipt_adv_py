from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])
    q.put(['hey', 'world'])


if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get(), q.get())
    p.join()
