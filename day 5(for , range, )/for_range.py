
##program to print 1 to 11

for numbers in range(1, 11):
    print(numbers)

##write a program that calculates the sum of all the even numbers from 1 to 100 , including 1  to 100.

even = 0
for even_numbers in range (2,101,2):
    #print(even_numbers)
    even += even_numbers
print(f"the sum of total even numbers are: {even}")    

##write a program that automatically prints the solution of FizzBuzz
print("*****************************************************")
for game in range(1,101):
    if (game % 3 == 0)  and (game % 5 == 0):
        print("FizzBuzz")
    elif game % 3 ==0:
        print("Fizz")
    elif game % 5 ==0 :
        print("Buzz") 
    else:
        print(game)         