x = 5 

for i in range(x):
    if i<x//2+1:
        for j in range(x):
            if j>=x-3-i and j<=x-3+i :
                print("*   ",end='')
            else:
                print("    ",end='')
        print()
        
    if i >= x//2+1 and i < x:
        for j in range(x):
            if j>=i-x+3 and j<=x+1-i :
                print("*   ",end='')
            else:
                print("    ",end='')
        print()
