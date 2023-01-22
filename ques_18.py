x=5

for i in range(x):
    for j in range(x):
        if j==i or j+i==x-1:
            print("*   ",end='')
        elif i==0 or i==x-1:
            print("*   ",end='')
        elif i>x//2 and j<i and j+i>x-1:
            print("*   ",end='')
        else:
            print("    ",end='')
    print()
