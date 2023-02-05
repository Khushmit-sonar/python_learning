print("**********************Calculator*********************")
print("Which operation you want to perform")

print("1. +")
print("2.-")
print("3.*")
print("4./")
print("5.//")
print("6.%")
print("7.**")

# input choice
ch=int(input("Enter Choice(1-7): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
elif ch==5:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a//b
    print("Quotient = ",c)
elif ch==6:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a%b
    print("Quotient = ",c)
elif ch==7:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a**b
    print("Quotient = ",c)            
else:
    print("Invalid Choice")