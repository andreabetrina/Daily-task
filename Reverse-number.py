# to print reverse of a number
n = 26
reverse=0
while ( n > 0 ):
     num= n%10
     reverse=reverse*10+num
     n=n//10
print("Reverse of the given is number is :")
