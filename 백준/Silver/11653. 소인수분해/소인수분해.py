n = int(input())
i = 2

while n != 1:
    if (n%i) == 0:
        print(i)
        n = n // i
    else:
        if i == 2:
            i+=1
        else:
            i+=2
