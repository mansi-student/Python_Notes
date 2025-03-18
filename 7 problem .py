'''
for n=3
  *
 ***
*****
'''

n=int(input("enter a number:"))
for i in range (1,n+1):
    print(" "*(n-i),end=" ")                        #i=lines utni jitne me stars print honge input k baad jese n=3 so , 3 lines m print honge
    print("*"*(2*i-1),end=" ")
    print(" ")