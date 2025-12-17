from random import randint
iterable = [randint(1,100) for _ in range(15)]
iterator = iterable.__iter__()
print(iterator)