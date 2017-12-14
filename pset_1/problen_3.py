#Write a program that prints the longest substring of s in which the letters occur in alphabetical order

#automatic input 
s = input("enter string of lowercase characters ")

len_s = len(s)

temp_sub=s[0]

sub = ""

for index in range(len_s - 1):
    #if the next character comes after in alphabet order than the present one
    if s[index + 1] >= s[index] :
        #then that next character is part of temp substring
        temp_sub += s[index + 1]
    #otherwise
    else:
        # if temp substing is biggest substring, it becomes sub
        if len(temp_sub) > len (sub) :
            sub = temp_sub
        # now we start finding the next substring 
        #starting with the character that broke the prev sub string
        temp_sub = s[index + 1]
        
#loop again repeated for case where we exit the for loop with temp_sub bigger than sub
if len(temp_sub) > len(sub):
    sub = temp_sub

print("Longest substring in alphabetical order is:",sub)
        
        