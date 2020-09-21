#import statistics as stat
import statistics as stat
#from statistics import median, mean
import sys

import time
import random
import functools

from itertools import cycle
a = [itm for itm in range(2,1000,3) if itm & 1]


def statistics():
    return 0

# print(median(a))
# print(mean(a))

# print(stat.__doc__)

def my_calc():
   return None

def my_sum(x,y):
    return x+y

def my_pow(x,y):
    return x ** y

proc = {
    'sum': my_sum,
    'pow': my_pow
}


# def f_even(ii : float) -> float:
#     if ii % 2:
#         return ii
#     else:

# if len(sys.argv) > 3:
#     _, f, x, y = sys.argv
#     print(proc[f](float(x), float(y)))
# x= 2
# y = 3
# f = pow
# print(proc['pow'](float(x), float(y)))

tmp = ['one','two','three','four','five']
# for itm in cycle(range(10)):
#     print(itm)
#     time.sleep(1)
#     num = random.shuffle(tmp,1)
#     print(num)

a = [itm for itm in range(2,8)]

def my_s(*args):
    return args[-1] + my_s(*args[:-1]) if args else 0

print(my_s())
