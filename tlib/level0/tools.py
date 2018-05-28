def selectFromArray(array, condition_func):
    res = []
    for e in array:
        if condition_func(e):
            res.append(e)
    return res


def getListItem(list, index, default):
    if len(list) > index:
        return list[index]
    else:
        return default


once_done = []


def doOnce(id, func):
    if not once_done.__contains__(id):
        once_done.append(id)
        func()


def average(_iter):
    try:
        _list = list(_iter)
    except TypeError:
        # I know that this can occur
        raise
    return sum(_list) / len(_list)


def map_value(val, start1, stop1, start2, stop2):
    range1 = stop1 - start1
    range2 = stop2 - start2
    percent = (val - start1) / range1
    return (percent * range2) + start2
