from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in n:
        yield i


g1 = gen1('Sergey')
g2 = gen2(5)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(tasks)
    except StopIteration:
        pass