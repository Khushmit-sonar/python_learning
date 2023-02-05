num = input("enter a number: ")
try:
    new = int(num)
except:
    new = -1


if new > 0:
    print("nice work")
else:
    print("its a wrong number")            