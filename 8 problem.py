n=int(input("enter a number:"))
for i in range (1,n+1):                        #i=lines utni jitne me stars print honge input k baad jese n=3 so , 3 lines m print honge
    print("*"*i,end=" ")
    print(" ")

'''                              pattern=;
    ***
    * *                     for n=3
    ***
    '''
n=int(input("enter a number:"))
for i in range (1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")