x= 5

for i in range(x):
    for j in range(x):
        if j==0 or j==(x-1):
            print("*   ",end='')
        elif (j==i and i>=x//2) or (i+j==x-1 and i>=x//2):
            print("*   ",end='')
        else:
            print("    ",end='')
    print()
