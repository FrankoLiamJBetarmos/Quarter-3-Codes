students = []

for i in range(3):
    print(f"\nStudent {i + 1}")
    s = {}

    s["name"] = input("Enter name: ")
    s["age"] = int(input("Enter age: "))
    s["grade"] = input("Enter grade: ")

    students.append(s)

print("\nClass Directory:")

for s in students:
    print(f"{s['name']} | Age: {s['age']} | Grade: {s['grade']}")
