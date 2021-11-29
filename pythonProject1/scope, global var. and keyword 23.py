l =10 #global variable
def function(n):
    # l = 5 # local variable
    m = 8   # local variable
    global l
    l = l+45
    print(l, m)
    print(n, "I have printed")
# hum global mai change permisson k bdd hi kr skte hain
function("This is me")
print(l)
# function mai phyle local dundha then globally dundha ..
# print(m) is not defined here because it is defined in local variable

x = 999
def shweta():
    x = 17
    def rohan():
        global x
        x = 98
    print("before calling rohan()", x)
    rohan()
    print("after calling rohan()", x)

shweta()
print(x)

# important vedio




















