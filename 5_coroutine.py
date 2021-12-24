def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():
    x = 'Ready to accept message'
    message = yield x
    print('Subgen received:', message)


class BlaBla(Exception):
    pass


@coroutine
def aver():
    count = 0
    summ = 0
    average = None
    while True:
        try:
            x = yield average
        except StopIteration:
            print('Done')
            break
        except BlaBla:
            print('blabla')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count)
