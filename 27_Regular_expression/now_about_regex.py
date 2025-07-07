# A regular expression (or regex) in Python is a special sequence of characters 
# used to search, match, or manipulate text based on patterns. 
# It’s like giving Python a flexible rulebook for finding strings that fit a certain shape.

# To use regex in Python, you need the built-in re module:
# import re

# Common Functions in re
# Function	    What It Does
# re.search()	Finds the first match anywhere in the string
# re.match()	Checks if the string starts with the pattern
# re.findall()	Returns all matches as a list
# re.sub()	    Replaces matched patterns with something else
# re.split()	Splits string by the pattern

# Metacharacters (Special Symbols)
# Symbol	  Meaning	                    Example
# .	          Any character except newline	a.b matches acb, a1b
# ^	          Start of string	            ^Hello
# $	          End of string	                world$
# *	          0 or more repetitions	        ab*c matches ac, abc, abbc
# +	          1 or more repetitions	        ab+c
# ?	          0 or 1 repetition	            ab?c
# {n}	      Exactly n repetitions	        a{3} matches aaa
# []	      Set of characters	            [aeiou]
# `	`	      Either/or	                    `cat	dog`
# \d	      Digit (0–9)	                \d{2} matches 23
# \w	      Word character                (a–z, A–Z, 0–9, _)	\w+


import re

pattern = "[A-Z]+yclone"

text = '''
    Cyclone Weird Faith has been described as an indie rock, indie folk, 
    and indie pop album. The album features sparse, acoustic arrangements 
    that highlight Diaz's lyrics and vocals, and it addresses themes of love,
    trust, and intimacy. Critics positively reviewed the album, cyclone Dyclone
    particularly praising Diaz's emotional songwriting. It was featured on 
    several year-end lists and was nominated for two Grammy Awards.
'''

# Finds the first match anywhere in the string
match1 = re.search(pattern,text)
print(match1)
print("---------------------------------------------------------")

# search for all matches of a pattern in a string and returns them as an iterator of match objects
match2 = re.finditer(pattern,text)
for match in match2:
    print(match)
print("---------------------------------------------------------")

# .span() is a method of a match object that returns a tuple with the start and end positions of the matched substring.
match3 = re.finditer(pattern,text)
for match in match3:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])
print("---------------------------------------------------------")

