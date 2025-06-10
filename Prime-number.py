#to check whether the give number is Prime or not.
n = 26
cnt = 0
num = n//2
for i in range ( 2 , num ):
    if (num%i) == 0:
        cnt+=1
if cnt == 0:
    print ( n, " is a Prime number" )
else:
    print( n, " is not a Prime number" )

