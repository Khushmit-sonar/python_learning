import random
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
random_numbers = input("how many random numbers do u want")
for row in range(0,random_numbers):
    random_integerr = random.randint(0,numbers)
    print(random_integerr)










random_integer = random.randint(1,10) ##random.randint function is used for displying random values.
print(random_integer)

random_float =  random.random()
print(random_float)


random_side = random.randint(0,1)
if random_side == 1:
    print("Head")
else:
    print("Tails")    
