##program to genetate password .
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the pypassword generator.")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
###easy way ::::in this way password will be in random order like kjjk123#%
#password = ""
#for char in range(1, nr_letters + 1) :
    #password += random.choice(letters)

#for num in range(1,nr_numbers + 1):
    #password += random.choice(numbers)
#for num in range(1,nr_symbols + 1):
    #password += random.choice(symbols)   
#print(password)     

###hard way :::: in this way password will not be in random it will be mixed.
password_list = []
for char in range(1, nr_letters + 1) :
    password_list += random.choice(letters)

for num in range(1,nr_numbers + 1):
    password_list += random.choice(numbers) ##random choise use to choise random number from list
for num in range(1,nr_symbols + 1):
    password_list += random.choice(symbols)   
random.shuffle(password_list) ##random shuffle is used to shuffle the list.
password_final =""
for chara in password_list    :
    password_final += chara
print(f"your final password is: {password_final}")    