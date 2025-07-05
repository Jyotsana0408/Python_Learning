# import  --->
# it lets you use code that’s already written somewhere else—like a toolbox full of functions, formulas, or helpers.


# Type                       ||   Example           ||  Description
# ------------------------------------------------------------------------------------
# Full module                ||	import math	        ||  Access with math.sqrt()
# Specific item	             || from math import pi	||  Use pi directly
# Aliased import             || import numpy as np	||  Shorten long names
# Import all (not advised)   ||	from math import *	||  Imports everything—can cause name conflicts


# Absolute vs Relative Imports--->

# Absolute: from utils import helper (recommended)
# Relative: from . import helper (used inside packages)

# Relative imports use dots:
# . = current package
# .. = parent package

# --------------------------------------------------------------------------------------------


# your code

# from math import * --> not recommended
import math
from math import sqrt, pi
import pandas as pd 
# from welcome import greet,name
import welcome as wc

print(math.floor(5.432))
 
result = sqrt(9) *pi
print(result)

print(pd.__version__)

print(dir(math))
print(type(math))

# greet()  -->  from welcome import greet,name
# print(name)  -->  from welcome import greet,name

wc.greet()
print(wc.name)