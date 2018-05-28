import re


def selectFromArray(array, condition):
    res = []
    for e in array:
        if condition(e):
            res.append(e)
    return res

def getListItem(list, index, default):
    if len(list) > index:
        return list[index]
    else:
        return default

done = []
def doOnce(id, func):
    if not done.__contains__(id):
        done.append(id)
        func()

def average(l):
    if type(l) in (tuple, list):
        return sum(l) / len(l)


def map_value(val, start1, stop1, start2, stop2):
    range1 = stop1 - start1
    range2 = stop2 - start2
    percent = (val - start1) / range1
    return (percent * range2) + start2
