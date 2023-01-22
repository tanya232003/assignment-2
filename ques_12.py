x= 5
a=0
b=1

for i in range(x):
    for j in range(x):
        if i==0 and j==0:
            print(a,"    ",end='')
        elif j==0 and i==1:
            print(b,"    ",end='')
        elif j<=i:
            c=a+b
            a,b = b,c
            if c <10:
                print(c,"    ",end='')
            if c>=10 and c<100:
                print(c,"   ",end='')
            if c>=100:
                print(c,"  ",end='')
        else:
            print("  ",end='')
            
    print()
