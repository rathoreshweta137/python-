import time #time module hain..

initial = time.time() #gives no. of tick ..1 tick =  1sec


k = 0
while(k<50):
    time.sleep(4)   #4 sec ke liye so jaega ...4sec k liye ruk jaega ..phir print krega
    k+=1
    print("This is harry bhai")
print("While loop ran in", time.time() - initial, "seconds")

initial2 = time.time()     #time ko  yaha reset kar diya...taai k ghr wala eg
for i in range(50):
    print("This is harry bhai")
print("For loop ran in", time.time()- initial2, "seconds")


localtime = time.asctime(time.localtime(time.time()))
print(localtime)











