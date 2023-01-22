x=5

for i in range(x):
    for j in range(x):
        if i==x//2 or j==x//2:
            print("*   ",end='')
        elif (i==0 and j<x//2 and i<x//2):
            print("*   ",end='')
        elif (i==x-1 and j>x//2 and i>x//2):
            print("*   ",end='')
        elif (j==0 and j<x//2 and i>x//2):
            print("*   ",end='')
        elif (j==x-1 and j>x//2 and i<x//2):
            print("*   ",end='')
        else:
            print("    ",end='')
    print()
