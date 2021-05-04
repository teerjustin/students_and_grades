output_list = []
classroom = {
    "Tom": { 
        "Math": 0,
        "English": 0,
        "History": 0,
    },
    "Sam": {
        "Math": 0,
        "English": 0,
        "History": 0,
    },
}

number_of_students = int(input("How many students do you have? "))
for i in range(number_of_students):
    student = ""
    while True:
        try:
            student = input("Student Name: ")
            if student != "Tom" and student != "Sam":
                print("This is not Tom or Sam: ", student)
                continue

        except:
            pass

        else:
            break

    grade = 0
    while True:
        try:
            grade = int(input("Grade: "))
            if grade < 0 or grade > 100:
                continue

        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue

        else:
            break


    course = ""
    while True:
        try:
            courseValue = int(input("Select a course: 1 - Math, 2 - English, 3 - History: "))
            if courseValue == 1:
                course = "Math"

            elif courseValue == 2:
                course = "English"

            elif courseValue == 3:
                course = "History"
            else:
                print('NOT 1 2 OR 3: ', courseValue)
                continue

        except ValueError:
            print("Sorry, I didn't understand that.")
            #better try again... Return to the start of the loop
            continue

        else:
            break

    classroom[student][course] = grade
    s = "Name: %s, Grade: %d, Course: %s" % (student, grade, course)
    output_list.append(s)

for s in output_list:
    print(s)
    

