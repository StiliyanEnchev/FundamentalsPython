divisor = int(input())
boundary = int(input())
N = ''
for num in range(boundary + 1):
    if num % divisor == 0 and num > 0:
        N = num
print(N)
