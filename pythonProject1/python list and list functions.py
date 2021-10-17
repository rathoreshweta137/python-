grocery = ["harpic", "chocolate", "vimbar", 56]        #mixed list of string and int..
print(grocery)

print(grocery[0])
print(grocery[1])
print(grocery[3])

# print(grocery[6]) will give error because grocery tu hai hi nahi..

numbers = [2,5,7,11]
print(numbers)
print(numbers[3])

#numbers.sort()         #list short hogyi , ascending order m aagyi
#print(numbers)

#sort and reverse orginal list ko change kr deta hai ...
#but slicing original list ko safe rkti hai ...

#numbers.reverse()      #list revrerse ho gayi...
#print(numbers)

print(numbers[0:4])      #puri list print ho gayi ...length le h humne isly ..
print(numbers[:])        #apne aap le lega computer ...

print(numbers[1:])       # 1: lene se phyla index leave kr dega....baki same
print(numbers[1:3])      # 1 ki vjay se phyla index leave kr dega..or 3 ki vjy se 3rd index leave kr dega
print(numbers[::1])      #same print krega ..
print(numbers[::2])      #ek ek uchal jaega ...
print(numbers[::3])       #2 -2 uchal jaega...

#negative slicing mai koi dusra no. na le ...sirf -1 hi lo

print(min(numbers))

#numbers.append(10)  #append = end mai 10 jod do....
#numbers.append(10)
#print(numbers)

#append end mai jodta h

#numbers = []
#numbers.append(10)
#numbers.append(10)
#print(numbers)

#numbers.insert(0, 32)     #0 index par 32 insert ho gya
#print(numbers)

#numbers.insert(3, 10000)   #3rd index par 10000 insert ho gya
#print(numbers)

#numbers.remove(11)
#print(numbers)

#numbers.pop()
#print(numbers)           #pop= end wala hata diya ...

#numbers[1] = 99
#print(numbers)      change ho gayi value ....
# agr m chati hun ki value change na ho , ye krta h tupple

# MUTUABLE = can change
# IMMUTABLE = cannot change

#  list = mutuable
#  tupple = immutable

#tp = ( 1, 2, 3 ,4)        #tp= alg h list se, yaha paranthesis aa rhe h.. list m sqaure bracket the
#print(tp)

# tp[1] = 88        # error kyuki immutable hota h tp[]

tp = (1,)           # ek extra comma lgana pdta h 1 tp mai ...
print(tp)

a = 1
b = 8
a, b = b, a
#temp = a
#a = b
#b =temp
print(a, b )

# search kro list function in python.....