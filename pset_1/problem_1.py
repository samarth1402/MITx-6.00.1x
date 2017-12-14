# Write a program that counts up the number of vowels contained in the string s.

#automatic input
s = input("enter a string ")

count_vowels = 0

for letter in s:
    if letter in ('a','e','i','o','u'):
        count_vowels+=1

print (count_vowels)
