from array import *


def left_join(ar1, ar2):
    res = []
    for i in ar1:
        if i not in ar2:
            res.append(i)
    res = array('i', res)
    return res
