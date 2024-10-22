a1=int(input("Enter a number: "))
for i in range(a1,10):
    if i%2 == 0:
        print(i)
print("-----------")
a=int(input("Enter a number: "))
while a<10:
    a+=1
    if a%2 != 0:
        continue
    print(a)

