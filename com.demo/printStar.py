#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# Python 3.4

n=5
s="*"

for x in range(1,n):
    for y in range(1,n-x):
        print(" ",end="")
    for z in range(1,2*x):
        print(s,end="")
    print("")
    
for x in range(1,n-1):
    for p in range(n-x,n):
        print(" ",end="")
    for q in range(1,(n-x-1)*2):
        print(s,end="")
    print("")
   