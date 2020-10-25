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
