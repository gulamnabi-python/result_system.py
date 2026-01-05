students = []

while True:
    print("\n1. Add Student Result")
    print("2. View All Results")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Student Name: ")
        m1 = int(input("Marks 1: "))
        m2 = int(input("Marks 2: "))
        m3 = int(input("Marks 3: "))

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 50:
            grade = "C"
        else:
            grade = "Fail"

        students.append({
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        })

        print("✅ Student result added")

    elif choice == "2":
        for s in students:
            print("\nName:", s["name"])
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])

    elif choice == "3":
        print("Program closed ❌")
        break

    else:
        print("Invalid choice ❗")
