students = {}
number = int(input("Enter number of students: "))
for i in range(number):
    print("\nStudent", i + 1)
    name = input("Enter Name: ")
    g1 = float(input("Enter Grade 1: "))
    g2 = float(input("Enter Grade 2: "))
    g3 = float(input("Enter Grade 3: "))
    students[name] = (g1 , g2, g3)

print("\n=== Student Records ===")
highest = 0
namehighest = ""
tally = 0
for name, grades in students.items():
    average = sum(grades)/len(grades)
    print(name, *grades, "Average: ", round(average,2))
    #find highest average
    if average > highest:
        highest = average
        namehighest = name
    #count grades below 75
    for grade in grades:
        if grade < 75:
            tally = 1
print("\n=== Results === ")
print(f"Students {namehighest} got the highest average: {highest:.2f}")
print(f"there are {tally} grades which are below 75")