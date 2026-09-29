while True:
    word = input("Enter a word: ")
    letter = input("Enter a character to search for: ")

    found = False

    for character in word:
        if character.lower() == letter.lower():
            found = True
            break

    if found:
        print("Character found: ")
    else:
        print("Character not found.")

    again = input("Try agin? (Y/N): ")

    if again.upper() != "Y":
        break

students = {"Ana": (90,85,82),
            "Kirk": (72, 73, 78,)}
for name, grade in students.items():
    print(name,*grade)
