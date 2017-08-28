# I was asked to code this during a Phone Interview
#
# With the condition that it NOT be in Perl ... I chose Python but didn't get too far.
#
#
# Write a function that takes a string and returns the longest substring of repeated characters.
#
# E.g. string = "abarrrrug" would return "rrrr", "AAabccba" would return "cc",
#  "quickbrownfox" would return the empty string.
#
# We never got to other edge conditions like "aaabbbb".
#
# I was forced to ask, "How often is this a problem for you guys?
#  Or are you pulling this out of the ether?" (I hate companies that act like they are Google)
#4:53pm

s='aaabbbb'
for i in range(len(s)):
    z=i
    cs=s[z]
    while True:
        if z == len(s) - 1: break
        if s[z] != s[z + 1]:break
        cs=cs+s[z+1]
        z+=1
    if len(cs)>=len(ls): ls=cs
if len(ls)==1: ls=''
print(ls)

#5:07pm