students = [] 
n = int(input("How many students? "))
for i in range(n):
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))
    students.append((name, grade))
print("\n--- Student Grades ---")
for s in students:
    print(f"Name: {s[0]}, Grade: {s[1]}")
total = sum(g for _, g in students)
print(f"\nClass Average: {total / n:.2f}")