students=[]
def add_students():
    print('Enter  new student: ')
    name=input('Name:')
    age=input('Age:')
    Grade=input('Grade:')
    try:
        age=int(age)
        Grade=int(Grade)
    except ValueError:
        print('Age and Grade must be intergers. Please try again.')
        return
    #dictory for students
    student={'Name':name, 'Age':age, 'grade':Grade}
    students.append(student)
    print(f'Student{name},has been successfully added')
def student_display():
    if not students:
        print('No student record found')
        return
    for student in students:
        print(f"Name: {student['name']},'Age':{student['age']},{student['Grade']}")
def main():
    while True:
        print('Student Mangement system')
        print('1.Add student name:')
        print('2.Display student records')
        print('3.Exiting program')
        choice=input('Enter your choice(1,2,3)')
        if choice=='1':
            add_students()
        elif choice=='2':
            student_display()
        elif choice=='3':
            print('Exiting the program')
            break
        else:
            print('Invalid choice.Please enter a valid choice')
if __name__=='__main__':
    main()
student_list=[]
def addstudent():
    while True:
        #prompt the user to add their details
        name=input('Enter Your name: ')
        age=input('Enter your age: ')
        grade=input('Enter your grade: ')
        #validate age and grade are intergers
        if not age.isdigit() or not grade.isdigit():
            print('The age and grade fields must be digit values!')
            print('Please enter thr values again.')
            continue
        #create a dict to hold the students details
        student={'Name':name,'Age':int(age),'Grade':int(grade)}
        #store the student details into the list we created above
        student_list.append(student)
        #create a loop for entry until the user opts out
        newstudent=input('Add another student to thr system? Press Y for Yes and N for No')
        if newstudent !='Y':
            #IF THE KEY PRESSED id not Y, then exit the loop
            break
def displaystudents():
    if not student_list:
        print('No records found')
        return

    print('Student Details: ')
    for student in student_list:
            print(f"name: {student['name']} Age:{student['age']} Grade{student['grade']}")
            print()
        #main loop presents a menu to user to allow them to choose different values based on their input
def main():
        while True:
            print('Press 1 to Add student details')
            print('Press 2 to view student details')
            print('Press 3 to exit the system')
            #get the user input
            userinput=input('Please select your choice: ')
            if userinput =='1':
                addstudent()
            elif userinput=='2':
                displaystudents()
            elif userinput=='3':
                break
            else:
                print('Invalid option. Enter 1 or 2 or 3')
if __name__=='__main__':
    main()
