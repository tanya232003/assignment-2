x=5
for i in range(x):
    for j in range(x):
        if (j==x//2 +i) or (i==x//2 +j) or (i+j==x-x//2 -1) or (i+j==x+x//2 -1) :
            print("*   ",end='')
        else:
            print("    ",end='')
    print()
