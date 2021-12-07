
# creating the dictionary
marks={}
temp_marks={}
num = int(input("How many students do you wish to add to the database: "))
for i in range (num):
    user_li=[]
    print()

    #inputting required data
    name = input("Enter the student's name: ")
    roll = int(input("Enter the student's roll number: "))
    student_marks = int(input("Enter the student's marks: "))

    #creating list
    user_li.append(name)
    user_li.append(student_marks)

    # adding values to a temp dictionary
    temp_marks={roll:user_li}

    # updating main dictionary with temp dicitionary's values
    marks.update(temp_marks)

print("Dictionary of students: ",marks)

# displaying names above 75 in a tabular format


print()
print("Students with marks above 75: ")
print("*****************************")
print()
for key in marks:
    if marks[key][1] > 75:
         print(marks[key][0]," - ",marks[key][1])
    else:
         continue
