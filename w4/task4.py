import sys
import argparse
import math
 
''' 
    Решето Эратосфена. В списке bits сбрасываются биты,
    имеющие составные номера, биты с простыми номерами == 1.
    i-му по порядку элементу будет соответствовать 1, если 
    i -- простое и 0 иначе. Сложность: nloglog(n).
'''

def bit_sieve(n):
    if n < 2:
        return []
    bits = [1] * n                             # <-- 11...1
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(2, sqrt_n):
        if bits[i - 2]:                        # если i -- простое
            for j in range (i + i, n + 1, i):  # занулить все ему кратные
                bits[j - 2] = 0
    return bits 


def get_prime(k): 
    # k-ое простое не превосходит 1,5 k ln( k ) при k > 1: 
    sieve = bit_sieve(int(1.5 * k * math.log(k)) + 1)
    i = 0
    while k:
        k -= sieve[i]
        i += 1
    return i + 1


def get_primes_before(k):
    return (list(filter(lambda x: all(map(lambda i: x % i != 0,
                                                    range(2, int(x ** 0.5) + 1))),
                                                    range(2, int(k) + 1))))
#  :\


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--show-all', action='store_true', default=False)
    parser.add_argument('-f', '--file', type=argparse.FileType('w', encoding='utf8'))
    parser.add_argument('number', type=int)
    return parser


if __name__ == '__main__':
    parser = createParser()
    args = parser.parse_args()
    
    prime = get_prime(args.number)
    out1 = "{}th prime number is {}".format(args.number, prime)
    print(out1)
    if args.file is not None:
        print(out1, file=args.file)

    if args.show_all:
        before = get_primes_before(prime)
        print(*before)
        if args.file is not None:
            print(*before, file=args.file)

    with open('log.txt', 'a') as log:
        log.write(str(prime) + '\n')

    if args.file is not None:
        args.file.close()
    
    print()