# to count how many numbers between 1 and 100 are divisible by 3 and prints the count.

cnt=0
for i in range( 1 , 101 ):
     if( i % 3 == 0 ):
          cnt+=1
print(cnt , " numbers are divisible by 3 between 1 and 100")

