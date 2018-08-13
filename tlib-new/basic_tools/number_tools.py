def range2percent(val, start, stop):
    return (val - start) / (stop - start)


def percent2range(perc, start, stop):
    return (perc * (stop - start)) + start


def range2range(val, start1, stop1, start2, stop2):
    return percent2range(range2percent(val, start1, stop1), start2, stop2)


def clamp(val, _min, _max):
    if _min > _max:
        _min, _max = _max, _min
    return max(_min, min(_max, val))