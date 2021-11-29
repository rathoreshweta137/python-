# F strings

me = "shweta"
you = 3
a = "This is %s %s"%(me, you)
print(a)
# string formatting ka tareeka h
# this is so confusing method if we have 10 -20 variables

var1 = "shweta rathore"
var2 = 6
A = "this is {1} {0}"
B = A.format(var1,var2)
print(B)
# ye bhi acha tareeka h string formatting ka but isse bhi reading mess up ho jati h
# so f strings are introduced


import math
var3 = "jimmy"
var4 = 8
a = f"this is {var3} {var4} {math.cos(60)}"
print(a)
# f string = fast string









































