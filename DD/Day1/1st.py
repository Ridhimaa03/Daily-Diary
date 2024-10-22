import random
l=["stone","paper","scissor"]
p2=random.choice(l)
p1 = input("Enter choice P1: ")
print ("Player 2 has chosen ", p2)
a = "stone"
b ="paper"
c ="scissor"
if p1 == a and p2 == a:
    print("It'a  tie!")
elif p1 == b and p2 == b:
    print("It'a  tie!")
elif p1 == c and p2 == c:
    print("It'a  tie!")
elif p1 == a and p2 == b:
    print("Player two won")
elif p1 == b and p2 == a:
    print("Player one won")
elif p1 == b and p2 == c:
    print("player two won")
elif p1 == c and p2 == b:
    print("player one won")
elif p1 == a and p2 == c:
    print("player one won")
elif p1 == c and p2 == a:
    print("player two won")
else:
    print("Enter valid value")


