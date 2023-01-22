x = 5 

for i in range(x):
    if i<x//2+1:
        for j in range(x):
            if j==x-i-3 or j==i+2 :
                print("*   ",end='')
            else:
                print("    ",end='')
        print()
        
    if i >= x//2+1 and i < x:
        for j in range(x):
            if j==i-2 or j==x-i+1 :
                print("*   ",end='')
            else:
                print("    ",end='')
        print()
