# divisible by 7 or 9, but not both
# and are palindromic numbers (e.g., 121)
#
answer = [
    i
    for i in range(1, 1000)
    if ((i % 7 == 0 and i % 9 != 0) or (i % 9 == 0 and i % 7 != 0))
    and str(i) == str(i)[::-1]
]

print(answer)
