f = open("Shweta.txt")
# print(f.tell())
print(f.readline())
f.seek(0)
print(f.readline())
# asa krke hum file ki sari line print ho jaegi
f.close()