#STRING = is datatype in python..
#         string is combination of characters enclosed in DQM.

mystr = "Shweta is good girl"
print(mystr)

# python mai index 0 se start hoti h ..
# s=0
# h=1
# w=2
# e=3
# t=4
# a=5
#  =6   ...1 tab ka index 6 hai ...
# i=7

print(mystr[2])  #slicing krdi..[]... 2 par w hai tu w print ho gya..
print(mystr[7])
print(mystr[6])   # 1 tab print kiya h , we cannt see it..

print(mystr[0:4])

# RULE OF SLICING
# agr [0:4] likha h so 0 included h or 4 excluded ..mtlb 0,1,2,3 k characters aaenge
# slicing = str ka tukda...

print(mystr[0:6])              #ab smj aaya shweta ?

print(len(mystr))              #length pta chal jati h string ki ...
                               #if len()is 19 then characters will 18...
print(mystr[0:19])

print(mystr[0:100])             # observe diff. shweta...

print(mystr[0:6:2])             # :2 ka mtlb =ek chor k ek in given length

print(mystr[0:])                # sirf 0:likh do tu pc puri length lelelega
print(mystr[:6])                # aaage 0 na lagao tu woh apne aap 0 assume krke dega ans..
print(mystr[::])
print(mystr[0:19:1])             # dono ki baat = h ...


# ADVANCE SLICING
print(mystr[::2])
print(mystr[::3])              # ab 3 -3 letter skip krega
print(mystr[::2500])           # ab jitna max. krta h woh kr dia


 # NEGATIVE INDICES....(Copy mai bna lo shweta )
 # L=-1
 # R=-2
 # I=-3


print(mystr[-4:-1])          # same as print(mystr[15:18]) ...

print(mystr[::-1])           # string ko ulta krne ka acha trika all characters daldo with:-1
print(mystr[::-2])           # string ulti k sth sth ek ek skip bhi krdia...:-2 mai
                             # ya fir phyle skip krlo positive krke phir ulta krlo..

print(mystr.isalnum())      # false aaya kyuki mystr mai space chuta hua hai ...

# alpha=spaces nhi hone chaiye ...

print(mystr.isalpha())       #false aaega kyuki num. nhi h or alpha bhi nhi hai kyuki spce aagyi..

print(mystr.endswith("girl"))  #true aagya kyuki mystr girl se end ho rhi hai ..agr kch or hota tu f aata

print(mystr.count("s"))
print(mystr.count("o"))

print(mystr.capitalize())   # first letter capital kr dega ..

print(mystr.find("good"))    #mtlb 10 index se good strat ho rha hai..

print(mystr.lower())         # puri string lower case m aagyi
print(mystr.upper())         #puri string upper case m aagyi

print(mystr.replace("good", "pretty"))   # good = pretty aagya bas