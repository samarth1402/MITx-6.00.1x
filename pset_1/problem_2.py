#Write a program that prints the number of times the string 'bob' occurs in s

#automatic input
s=input("enter string of lowercase characters ")

len_s = len(s)

bobcount = 0

for index in range(len_s):
    if s[index:(index+3)] == 'bob':
        bobcount+=1
        index+=2
        
print(bobcount)
        
        