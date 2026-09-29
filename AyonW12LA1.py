while True:
    AyonCLassrec = {"Pearla" :{"StudID": "5001",
                             "Grade":[90,85,86,82,83,90,92]},
                    "Carla" :{"StudID":"5002",
                               "Grade":[56, 75, 80, 84, 75, 85]},
                    "ELi" :{"StudID":"5003",
                            "Grade":[90, 99, 97, 98, 95, 96]
                               }
                    }
    Ayonstud = input("Enter the students's name or id: ")
    found = False
    for AyonCLassrec, student in AyonCLassrec.items():
        if AyonCLassrec.lower() == Ayonstud.lower() or student["StudID"] == Ayonstud:
            grades = student["Grade"]
            print("Student found."
                  "\nThe Student's grades are: ", *grades )
            Ayonaverage = sum(grades)/len(grades)
            print(f"The Average is:  {Ayonaverage:.2f}")
            for grade in grades:
                if grade < 60:
                    print("Candidate for intervention.")
                    break
            mx = max(grades)
            mini = min(grades)
            print("The Highest grade is: ", mx,
                  "\nThe Lowest grade is: ", mini)
            break
    else:
        print("Student not found")
        break





















