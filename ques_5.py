x=5
for i in range(x):
    for j in range(x):
        if (j<=x//2 +i) and (i<=x//2 +j) and (i+j>=x-x//2 -1) and (i+j<=x+x//2 -1) :
            print("*",end='')
        else:
            print(" ",end='')
    print()
