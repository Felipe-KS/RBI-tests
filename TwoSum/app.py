numbers = [1,3,5,7,9]
target = 12

def findTwoSum(numbers:list , result:int):
    length = len(numbers)-1
    p1 = 0
    response = []
        
    while p1 != length + 1:
        p2 = length
        while p2 != -1:
            if p2 == p1 or numbers[p1] + numbers[p2] > result:
                p2 -= 1
            elif numbers[p1] + numbers[p2] == result:
                response.append(str(p1) + ", " + str(p2))
                break
            elif numbers[p1] + numbers[p2] < result:
                break                
        p1 += 1
    
    if response == []:
        response = ['-1,-1']

    return response

r = findTwoSum(numbers, target)
for i in r:
    print(i)