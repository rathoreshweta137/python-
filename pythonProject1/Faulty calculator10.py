 # exercise 2 = faulty calculator
 # 45*3 = 555, 56+ 9 = 77, 56/6 =4

print("Enter your first number")
i1 = int(input())
print("Enter your second number")
i2 = int(input())
print("So enter your operator ","+,-,*,/" )
operator = input()

if i1==45 and i2==3 and operator== "*":
    print("555")
elif i1==56 and i2==9 and operator=="+":
    print("77")
elif i1==56 and i2==6 and operator=="/":
    print("4")
elif operator=="+":
    i3=i1+i2
    print(i3)
elif operator=="-":
    i4=i1-i2
    print(i4)
elif operator=="*":
    i5=i1*i2
    print(i5)
elif operator=="/":
    i6=i1/i2
    print(i6)
print("Thankyou for using calculator")


