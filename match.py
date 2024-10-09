a = int(input("Enter your marks: "))

match a:
    case a if a >= 90:
        print("Grade: A")
    case a if 80 <= a < 90:
        print("Grade: B")
    case a if 50 <= a < 80:
        print("Grade: C")
    case _:
        print("Invalid marks")
