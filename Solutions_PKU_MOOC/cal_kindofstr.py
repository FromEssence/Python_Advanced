import string

s = 'ww-m/23 4j)'
letter = 0
space=0
digit=0
other=0
for c in s:
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit += 1
    else:
        other += 1

print("There are %d letters,%d spaces,%d digits and %d other characters in your string."%(letter,space,digit,other))
        

