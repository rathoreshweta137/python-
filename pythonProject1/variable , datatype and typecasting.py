# VARIABLE = container to store a value or string etc..eg of horlicks daba chini

var1= "hello world "  # string variable ( jaisa ka taisa store krna chata hun)
var2= 4              #integer variable
var3= 36.7           #floating variable (decimal wala)
var4= "shweta"
print(var1)

print(type(var1))     #type puch rhe h hum var1 ka ..jo ki str aaega ...
print(type(var2))     #type puch rhe h hum var2 ka ..jo ki int aaega...
print(type(var3))     #type puch rhe h hum var3 ka ..jo ki float aaega...

print(var2+var3)      # no. aps m add hogye ..kyuki ho skte the ..so no error

# if we print(var1+var2) then this will show error bc one is string var.
# and other is integer var.

print(var1+var4)          # string var. aps m add ho jaenge ..

# type pta krne k lie print(type(var1)) krna prega ...

          # string ko hum DQM mai likhte h ...

var5="32"
var6="54"
print(var5+var6)        #2 strings ko aps m add kiya ja rh h..
print(var5 + var6)

#kya hum str() ko int() m convert kr skte h ?
# jee haan, by typecasting
print(int(var5) + int(var6))       #isme plus kr dia


print(10 * "hello world")
print(10* "hello world\n")

print(100*int(var5))

print(100*int(var5)+ int(var6))

print("Enter Your Number")
inpnum = input()    #isse hum jo bhi no. dalnege woh as a str() inpnum var. m chla jaega ..as a int() nhi jaega

print("You entered ", int(inpnum)+10)

# input() mai string nikalta h..so mai direct inpnum+10 nhi kr skti ..int() m convert krna prega...

print("Enter first number")
var7= input()
print("You entered ", var7)
print("Enter second number")
var8= input()
print("You entered", var8)
print("Final addition is", int(var7)+int(var8))