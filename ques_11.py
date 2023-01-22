x = 5

n = 1 

for i in range(x):
    for j in range(x):
        if j <=i:
            if n <10:
                print(n,"   ",end='')
            if n>=10:
                print(n,"  ",end='')
            n+=1
        else:
            print("    ",end='')
    print()
