from .collection_tools import flatten, pairs


def split_at_delimeters(s, delim_list):
    split = [s]
    for delim in delim_list:
        split = [x.split(delim) for x in split]
        split = flatten(split)
    return split


def replace_multiple(s, repl_dict):
    res = s
    for k, v in pairs(repl_dict):
        res = res.replace(k, v)
    return res