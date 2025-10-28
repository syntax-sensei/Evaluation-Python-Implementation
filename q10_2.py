import threading

tot = 0
lock = threading.Lock()


def calculate(st, end):

    global tot

    s = 0
    for i in range(st, end):
        s += i * i

    with lock:
        tot += s


num = 1000000

steps = num // 2

threads = []

for i in range(0, num, steps):
    th = threading.Thread(target=calculate, args=(i + 1, i + steps + 1))

    threads.append(th)
    th.start()

for th in threads:
    th.join()

print(tot)
