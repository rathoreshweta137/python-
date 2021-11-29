a = 5
b = 7
c = sum((a,b)) # sum function k andar list honi chaiye ya tupple hona chaiye means iterable hona chaiye..
print(c) # sum = builtin function

# userdefine fuction = jo user khud define krta h
# uske lie hume def keyword use krna pdta h
def function1():
    print("Hello you are in function1")

(function1())  #baar baar print likhne ki need nhi h ..
(function1())  # sirf function1 likhne se kaam ho jaega
(function1())  # ye asa function h jo nahi koi input le rha tha or na koi ouput , kch return nhi kr rha

def function2(a,b):
    print("Welcome you are in function2",a+b )
function2(a,b)  # 12 value tamees se nhi di , agr mjhe var. mai chaiye tu ?

def function3(a,b):
    """This function will calculate average of two number
    this function doesnt work for 3 numbers"""

    average = (a+b)/2
    print(average)
    return average
print(function3.__doc__)  # doc bta dega ki function type

# return statement is optional ..
# return fn. ki help se answer variable m store ho gya
# agr m ab print wali statement hata bhi du , still i will get 6 due to stored

v = function3(5,7)
print(v)

# DOCSTRING = function k andar , phyli line par jo string likhi hoti h use docstring khte h
# doc bta dega function type
# if many peoples work on a project then we can easily know ki kisi or ne  is function k lie koi warning tu nhi di..ya msg



