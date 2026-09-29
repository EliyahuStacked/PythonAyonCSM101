print("-----AyonHut-----")
AyonFlav = input("Enter the pizza flavor \nHawaiian"
                 "\nPepperoni"
                 "\nCheese"
                 "\nHam&Cheese"
                 "\nFourCheese \n").lower()

match AyonFlav:
    case "hawaiian":
        print("You selected Hawaiian")
        AyonSize = input("Enter the size \nsmall"
                     "\nmedium"
                     "\nlarge\n").lower()
        if AyonSize == "small":
            Ayonprice = 250
        elif AyonSize == "medium":
            Ayonprice = 350
        elif AyonSize == "large":
            Ayonprice = 450
        else:
            Ayonprice = 0
            print("Invalid price")
    case "pepperoni":
        print("You selected Pepperoni")
        AyonSize = input("Enter the size \nsmall"
                     "\nmedium"
                     "\nlarge\n").lower()
        if AyonSize == "small":
            Ayonprice = 250
        elif AyonSize == "medium":
            Ayonprice = 350
        elif AyonSize == "large":
            Ayonprice = 450
        else:
            Ayonprice = 0
            print("Invalid price")
    case "cheese":
        print("You selected Cheese")
        AyonSize = input("Enter the size \nsmall"
                         "\nmedium"
                         "\nlarge\n").lower()
        if AyonSize == "small":
            Ayonprice = 250
        elif AyonSize == "medium":
            Ayonprice = 350
        elif AyonSize == "large":
            Ayonprice = 450
        else:
            Ayonprice = 0
            print("Invalid price")
    case "ham&cheese":
        print("You selected Ham&Cheese")
        AyonSize = input("Enter the size \nsmall"
                         "\nmedium"
                         "\nlarge\n").lower()
        if AyonSize == "small":
            Ayonprice = 120
        elif AyonSize == "medium":
            Ayonprice = 180
        elif AyonSize == "large":
            Ayonprice = 240
        else:
            Ayonprice = 0
            print("Invalid price")
    case "fourcheese":
        print("You selected FourCheese")
        AyonSize = input("Enter the size \nsmall"
                         "\nmedium"
                         "\nlarge\n").lower()
        if AyonSize == "small":
            Ayonprice = 400
        elif AyonSize == "medium":
            Ayonprice = 500
        elif AyonSize == "large":
            Ayonprice = 550
        else:
            Ayonprice = 0
            print("Invalid price")
    case _:
        Ayonprice = 0
        print("Invalid Flavour")
if Ayonprice > 0:
    print("Pizza Price:", Ayonprice)

