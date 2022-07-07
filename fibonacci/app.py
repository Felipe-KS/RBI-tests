count = 1
fibo = 0
fibo2 = 1
print(fibo)
while count < 100:
    result = fibo + fibo2
    fibo = fibo2
    fibo2 = result
    print(result)
    count += 1 