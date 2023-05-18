from bitset import BitSet
from random import randint
from math import log


class FilterBlum:
    def __init__(self, requests_amount: int, error_probability: float):
        def make_hashes():
            tuple_coefficient = [randint(0, array_len - 1) for _ in range(4)]

            def func(args, tuple_coeff=tuple_coefficient):
                return sum(tuple_coeff[j] * args[j] for j in range(4)) % array_len

            return func

        bits_per_elem = int(log(error_probability) // (log(0.5) * log(2)))
        array_len = bits_per_elem * requests_amount

        self.bits = BitSet(array_len)  # Array of bits
        self.hash_amount = int(log(2) * bits_per_elem)  # Amount of hash functions
        self.hash_functions = [make_hashes() for _ in range(self.hash_amount)]  # Array of hash functions

    def lookup(self, val):
        ip_address = val.split(".")
        ip_address = [int(i) for i in ip_address]
        for func in self.hash_functions:
            index = func(ip_address)
            if self.bits[index] == 0:
                return False
        return True

    def insert(self, val):
        ip_address = val.split(".")
        ip_address = [int(i) for i in ip_address]
        for func in self.hash_functions:
            index = func(ip_address)
            self.bits[index] = 1


a = FilterBlum(10, 0.02)
# a.insert('192.168.5.255')
# b = [192, 168, 5, 255]
# for i in range(5):
#     for func in a.hash_functions:
#         print(func(b))
#     print("==========================================")

a.insert('192.168.5.0')
a.insert('255.255.255.0')
a.insert('169.254.254.255')
a.insert('73.252.124.218')
a.insert('240.240.223.155')
a.insert('156.65.240.55')
a.insert('43.123.249.114')
a.insert('148.104.213.121')
a.insert('169.167.232.11')

print(a.lookup('169.254.254.255'))
print(a.lookup('240.240.223.155'))
print(a.lookup('193.187.131.113'))
print(a.lookup('213.90.13.6'))
