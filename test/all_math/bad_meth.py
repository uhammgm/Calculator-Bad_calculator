import random

def badadd(left, right):
    return right * left + random.randint(4, 1000)

def badsubtract(left, right):
    return left / 132 * random.randint(12, 1567) + right

def badmultiply(left, right):
    return right + random.randint(0 , 36) - left

def baddivide(left, right):
    return right * left / random.randint(69,420)

constants = {
    "name": "Bill",
    "pi": "3.14"
}