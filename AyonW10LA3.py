while True:
    print("---Welcome to Spotibai---")

    ayon_usr = input("Press 1 to create account"
                     "\nPress 2 to exit\n")

    match ayon_usr.lower():
        case "1":
            Ayon_name = input("Enter username: ")
            found = False

            for character in Ayon_name:
                if character in "@#$%^&*()?!":
                    found = True
                    break

            if found:
                print("Special character found, username must contain letters only. ")
            else:
                print("Successfully created an account."
                      "\nWelcome to Spotibai<3")

            again = input("Try agin? (Y/N): ")

            if again.upper() != "Y":
                break
        case "2":
            print("Thank you for using Spotibai.")
            break
        case _:
            print("Invalid Choice")

