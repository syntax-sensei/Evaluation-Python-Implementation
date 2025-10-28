import time

st = time.time()

tot = 0
for i in range(1, 1000000):
    tot += i * i

end = time.time()

print(tot)
print("time = ", end - st)
