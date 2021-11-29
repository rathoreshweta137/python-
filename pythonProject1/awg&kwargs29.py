# def function_name_print(a,b,c,d,e):
#     print(a,b,c,d,e)
#
# function_name_print("Harry", "Shweta","Priya","Shalini", "yash")

# or naaam add krne ka ye sahi tareeka nahi
# isse behtar tareeke se hum add krte skte h args or kwrags se
# normal argument ko phele rkhna h ...nahi to error aaega..its convention ..
 
def funargs(normal, *args, **kwargs):
    print(normal)

    for item in args:
        print(item)
    print("\nnow i would like to introduce some heroes")

    for key, value in kw.items():
        print(f"{key} is a {value}")
    # print(type(args)) #convention hota hain , tupple hi jaega ..
    # print(args[0])

har = ["Harry", "Shweta","Priya","Shalini", "yash", "programmer"]
normal = "there are normal students ."
kw = {"Rohan":"monitor", "Harry":"Fitness monitor"}
funargs(normal,*har)

# args and kwargs optional hote hain dena h toh do ..aapki marzi






















