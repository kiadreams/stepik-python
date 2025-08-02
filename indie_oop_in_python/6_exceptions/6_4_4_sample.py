try:
    raise KeyError('Где же')
except KeyError as first:
    try:
        raise IndexError('ты теперь')
    except IndexError as second:
        try:
            raise NameError('воля')
        except NameError as third:
            raise Exception('вольная?') from second