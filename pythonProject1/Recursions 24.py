def factorial_iterative(n):
    """hello !"""
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

# Working of factorial_recursive()
# 5 * factorial_recursive(4)
# 5 * 4 * factorial_recursive(3)
# 5 * 4 * 3 * factorial_recursive(2)
# 5 * 4 * 3 * 2 * factorial_recursive(1)
# 5 * 4 * 3 * 2 * 1 = 120


number = int(input("Enter the number \n"))
print("Factorial using Iterative method",factorial_iterative(number))
print("Factorial using recursion method", factorial_recursive(number))

# Quiz
# 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n == 0:
        return  0
    elif n == 1:
        return 1
    else:
        return (fibonacci(n-1)+ fibonacci(n-2))
number = int(input("Enter your number"))
print(fibonacci(number))


# which method should we use ? recursive ya iterative ?
# recursive main debugging krte time prblm hogi ..bascis easy hota hain...easy chizo k lie acha haion but hard program main problem aati hain
# iterative method point to point hota hain , bss thora code jyda likhna hota hain











