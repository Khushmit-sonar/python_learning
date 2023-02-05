row = int (input("Enter how many rows you want: "))
char = input("Enter the character you want to print")

for x in range(row +1):
    print('')
    for y in range(x):
        print(char, end="")