# Program to count the number of Vowels and Consonants.
str = "Helloo Andreaaa!"
vow = 0
cnt = 0
vowels = "aeiouAEIOU"
for ch in str:
     if ch in vowels :
          vow += 1
     else:
          cnt +=1
print (" No of Vowels : ", vow)
print (" No of Consonants : ", cnt)
