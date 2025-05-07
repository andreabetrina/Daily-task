# python program to remove the vowels in a string.
str = " Hello Andreaaa!"
emptystr= " "
vowels = "aeiouAEIOU"
for ch in str:
     if ch not in vowels:
          emptystr += ch
print ( str ,":" ,emptystr )
