# f = open("Shweta8.txt", "a")
# a = f.write("Shweta is a amazing girl\n")
# print(a)
# f.close()
# new file is made in which we can wrote anything by
# f.write.... name of file is f = open() ..jo likhoge

# append mode = add written things to already given file
# "w " means jo naya likh rahe hain use likho ..baki bhul jao

# handle read and write both
f =open("Shweta8.txt", "r+")
print(f.read())
f.write("Thankyou")

# read and write dono ek sth hi hogaya