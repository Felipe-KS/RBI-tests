numbers = input("Enter a Integer:")

if not numbers.isnumeric():
    print("Input is not a Integer")
else:
    if len(numbers) == 1:
        print(numbers)
    else:
        numbersList = [x for x in numbers]
        i = len(numbersList)-1
        flag = 0
        while i != 1:
            y = i - 1
            while y != 0:
                if numbersList[i] > numbersList[y]:
                    aux = numbersList[i]
                    numbersList[i] = numbersList[y]
                    numbersList[y] = aux
                    flag = 1
                y -= 1
            if flag == 1: break
            i -= 1
        numbers = "".join(numbersList)
        print(numbers)
