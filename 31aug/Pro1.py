from school import Student

students = list()

while True:
    print("\n1. Add Student")
    print("2. Search Student")
    print("3. Add Exam")
    print("4. Exit")
    choice = input(">> ")
    if choice=='4':
        break
    elif choice=='1':
        ob = Student()
        ob.input()
        students.append(ob)
    elif choice=='2':
        roll = input("\nRoll : ")
        for stud in students:
            if stud.roll==roll:
                stud.show()
                break
        else:
            print("\nNo Student Found !")            
    elif choice=='3':
        roll = input("\nRoll : ")
        for stud in students:
            if stud.roll==roll:
                stud.addExam()
                break
        else:
            print("\nNo Student Found !")   

