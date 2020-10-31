s = 'Hello World'

print(s[1:])
print(s[:4])
print(s[:])

# We can also use negative indexing to go backwards.


# Grab everything, but go in steps size of 1
# s[::1] Out[22]: 'Hello World'

# Grab everything, but go in step sizes of 2
# s[::2] Out[23]:'HloWrd'

# We can use this to print a string backwards
# s[::-1] Out[24]: 'dlroW olleH'

'''It's important to note that strings have an important property known as immutability.
   This means that once a string is created, the elements within it can not be changed or replaced'''

str1 = 'jai'
# str1[0] = 's' //not allowed
print(str1)
str1 = str1 + ' shankar'
print(str1)
letter = 'a'
print(letter * 10)
name = 'jai.shankar.mishra'
# built-in functions
print(name.split('.'))
# format string
print('Insert another string with curly brackets: {}'.format('The inserted string'))

print('The {2} {1} {0}'.format('fox', 'brown', 'quick'))
print('The {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

# formatting
'''
There are three ways to perform string formatting.

*The oldest method involves placeholders using the modulo % character.
*An improved technique uses the .format() string method.
*The newest method, introduced with Python 3.6, uses formatted string literals, called f-strings.
Since you will likely encounter all three versions in someone else's code, we describe each of them here.
'''

# float follows "{value:width.precision f}"
result = 100 / 7
print(result)
print("the result is: {r:1.3f}".format(r=result))
print(f"the result is: {result:{1}.{5}}")

# string f literals #python3.6
print("my fname is {}".format(name))
print(f"my fname is {name}")

'''
Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. 
This fits more closely with scientific notation and statistical analysis. 
Unfortunately, f-strings do not pad to the right of the decimal, even if precision allows it:


num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
My 10 character, four decimal number is:   23.4500
My 10 character, four decimal number is:     23.45
If this becomes important, you can always use .format() method syntax inside an f-string:

num = 23.45
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:10.4f}")
My 10 character, four decimal number is:   23.4500
My 10 character, four decimal number is:   23.4500
'''

# indexing and slicing in strings
string = 'abcdefghi'
print(string[::2]) # steps of 2
print(string[2:6])
