x = 5 

for i in range(x):
    for j in range(x):
        if j<x-i-1:
            print("    ",end='')
        else:
            print("*   ",end='')
    print()
