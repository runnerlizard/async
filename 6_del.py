def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBla(Exception):
    pass


def subgen():
    while True:
        try:
            message = yield
        except BlaBla:
            print('kuku')
        else:
            print('///////////', message)


@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBla as e:
    #         g.throw(e)
    yield from g
