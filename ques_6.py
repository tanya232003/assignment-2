x = 5 

for i in range(x):
    if i<x//2:
        for j in range(x+2):
            if j>=x-2-i and j<=3+i :
                print("    ",end='')
            else:
                print("*   ",end='')
        print()
        
    if i >= x//2 and i < x:
        for j in range(x+2):
            if j>=i-1 and j<=x+2-i :
                print("    ",end='')
            else:
                print("*   ",end='')
        print()
