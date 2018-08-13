def _flatten_once(l):
    res = []
    for inner_list in list2d:
        res += inner_list
    return res


def flatten(l, max_num_iterations=1):
    icap = max_num_iterations
    if icap == 1:
        return _flatten_once(l)
    else:
        i = 1
        while list in [type(x) for x in res] and i <= icap:
            l = _flatten_once(l)
            i += 1
        return l


def rangelen(l):
    return range(len(l))
_rl = rangelen


def pairs(d):
    return [(k, d[k]) for k in d.keys()]


def ipairs(l):
    return [(i, l[i]) for i in _rl(i)]


def average(l):
    return sum(l) / len(l)


def tryGetAt(l, i, default_val=None):
    if i in _rl(l):
        return l[i]
    else:
        return default_val


def tryGetVal(d, k, default_val=None):
    if k in d.keys():
        return d[k]
    else:
        return default_val


def filter(l, f):
    res = []
    for e in l:
        if f(e):
            res.append(e)
    return res