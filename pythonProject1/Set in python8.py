s = set()
#print(type(s))   type pta chl jaega ki ye set h ..

s_from_list = set([1,2,3,4])
print(s_from_list)
# print krte hi set print ho jaega ..

# l = [ 1, 2,3, 4]
# s_from_list = set (L)
# print(s_from_list)......baat vahi pregi

"""

how to add element in set ?

"""
s.add(1000)
s.add(1000)  #kch farak nhi pra

# kyuki set unique value ko dekhta h ...

print(s)
# dekho s jo empty set tha usme element add hogya..

s_from_list.add(99)
s_from_list.add(100)
print(s_from_list)

s1 = s.union({45})
print(s,s1)

#intersection bhi easy h ,,

s2 = s.intersection({1000 , 9})
print(s, s2)

print(len(s))
print(max(s_from_list))
print(min(s))

s.remove(1000)
print(s)