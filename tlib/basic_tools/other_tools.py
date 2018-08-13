_done = []
_done_id_counter = 0
def doOnce(func, *args, id=None):
    if id is None:
        id = _done_id_counter
        _done_id_counter += 1
    if id not in _done:
        _done.append(id)
        func(*args)