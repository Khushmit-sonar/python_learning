import math
def paint_calc(height, width, cover):
    calculation = math.ceil(height * width / cover)
    print(f"you will need {calculation} cans")







test_h = int(input("Enter the Height of Wall: "))
test_w = int(input("Enter the Width of Wall: "))
coverage = 5

paint_calc(height =test_h, width=test_w, cover = coverage) 




