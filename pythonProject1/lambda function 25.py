# lambda functions or anonymous function
# lambda is one liner function

# def add(a,b):
#     return a+b

# both are same ..lambda helps us to make it one liner

# add = lambda x, y:x+y
# print(add(4, 5))

# lambda function banane ka new method hai bss

def a_first(a):
    return a[1]

a = [[1,4], [8,23],[5,6]]
a.sort(key=a_first)
print(a)

# key wala function arguement leta hain
# or woh function jo leta hain ye woh kch return krta hain

# a.sort(key=lambda x:x[1]) same
