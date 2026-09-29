patient = {"Ana" :[80, 90, 100, 300, 230, 500, 333,],
           "Ben" :[120, 140, 130, 90, 150, 200, 250],
           "Carlo" :[80, 90,95, 99,75, 66, 78]}
for patient, reading in patient.items():
    print("\nPatient", patient)

    for value in reading:
        if value > 120:
            print(value, "- High")
        else:
            print(value, "- Normal")

    maxi = max(reading)
    mini = min(reading)
    avg = sum(reading)/len(reading)
    diff = maxi - maxi
    print("Max:", maxi,
          "\nMin:", mini,
          "\nAverage:", avg,
          "\nDifference:", diff)
