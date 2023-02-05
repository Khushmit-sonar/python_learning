student_heights = input("Input the list of student heights: \n").split()
print(student_heights)
for n in range(0 , len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)    

total_height =0
number_of_student = 0
for students in student_heights:
    total_height += students
    number_of_student +=1
print(total_height) 
print(number_of_student)   

average_student_height = total_height / number_of_student
print(f"Average student height is, {average_student_height}")
