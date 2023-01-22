x = 5

for i in range(x):
    for j in range(x):
        if j>=x//2 and (j<=x//2 +i) and (i+j<=x+x//2 -1) :
            print("*   ",end='')
        elif i==x//2:
            print("*   ",end='')
        else:
            print("    ",end='') 
            
    print()
