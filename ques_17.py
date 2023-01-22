x = 5

for i in range(x):
    for j in range(x):
        if ((i==x//2) or (j==x//2)): # or (j-i%2==0 and j>x//2)):
            print("*   ",end='')
        elif((j-i)%2==0 and j>x//2 and j<x-1):
            print("*   ",end='')
        else:
            print("    ",end='')
    print()
