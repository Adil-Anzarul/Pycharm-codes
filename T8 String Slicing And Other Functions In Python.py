mystr="Adil Anzarul is a good boy"
print(mystr)
"""for printing a character"""
print(mystr[3])
"""for printing substring """
print(mystr[0:3])  # syntax here in mystr[m:n]  from m to n-1 ie n is excluded
" to find length of string"
print(len(mystr))

#print(mystr[80]) it will show error but
print(mystr[0:100])#it will not show error
print(mystr[0:])#print the entire string
print(mystr[:4])# it will take zero

""" but if we want to escap character ek ek (alternately)  then"""
print(mystr[0:5:2])
print(mystr[:])
"""it will print the entire string"""
print(mystr[::])
""" by default tisra wala ko 1 maan leta hai"""
print(mystr[::2])


"""negative index 
    count from reverse and start with -1
      like -1 -2 -3 ....."""

"""to reverse string"""
print(mystr[::-1])


print(mystr[::-2])#it first reverse and then escape ek ek character

print(mystr.isalnum())
print((mystr.isalpha()))
print(mystr.endswith("boy"))
print(mystr.endswith("Boy"))
print(mystr.count("o"))
print(mystr.capitalize())#it capitalize first letter
print(mystr.find("is")) # for searching ,it return the index no.
print(mystr.lower())# whole string to lower case
print(mystr.upper())# whole string to upper
print(mystr.replace("is","are"))

