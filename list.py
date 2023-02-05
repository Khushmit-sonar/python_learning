import random

names_string = input("Give me everybody's name, seperated by comma.")
name = names_string.split(",") 
num_items = len(name)
random_choise = random.randint(0, num_items -1)
person_who_will_pay_a_bill = name[random_choise]
print(f"{person_who_will_pay_a_bill}, will pay the bill today. ")

##or

person_who_will_pay = random.choice(name)
print(f"{person_who_will_pay}, will pay the bill today. ")

