print("-----AyonHut-----")
AyonFlav = input("Enter the pizza flavor \nHawaiian"
                 "\nPepperoni"
                 "\nCheese"
                 "\nHam&Cheese"
                 "\nFourCheese \n").lower()

if AyonFlav == "hawaiian":
    print("You selected Hawaiian Pizza.")

    AyonSize = input("Enter the size \nSmall"
                 "\nMedium"
                 "\nLarge").lower()
    if AyonSize == "small":
        Ayonprice = 250
    elif AyonSize == "medium":
        Ayonprice = 350
    elif AyonSize == "large":
        Ayonprice = 450
    else:
        Ayonprice = 0
        print("Invalid Price")

elif AyonFlav == "pepperoni":
    print("You selected Pepperoni Pizza.")

    AyonSize = input("Enter the size \nSmall"
                 "\nMedium"
                 "\nLarge").lower()
    if AyonSize == "small":
        Ayonprice = 250
    elif AyonSize == "medium":
        Ayonprice = 350
    elif AyonSize == "large":
        Ayonprice = 450
    else:
        Ayonprice = 0
        print("Invalid Price")

elif AyonFlav == "cheese":
    print("You selected Cheese Pizza.")

    AyonSize = input("Enter the size \nSmall"
                 "\nMedium"
                 "\nLarge").lower()
    if AyonSize == "small":
        Ayonprice = 250
    elif AyonSize == "medium":
        Ayonprice = 350
    elif AyonSize == "large":
        Ayonprice = 450
    else:
        Ayonprice = 0
        print("Invalid Price")

elif AyonFlav == "fourcheese":
    print("You selected FourCheese Pizza.")

    AyonSize = input("Enter the size \nSmall"
                 "\nMedium"
                 "\nLarge").lower()
    if AyonSize == "small":
        Ayonprice = 500
    elif AyonSize == "medium":
        Ayonprice = 550
    elif AyonSize == "large":
        Ayonprice = 600
    else:
        Ayonprice = 0
        print("Invalid Price")

elif AyonFlav == "ham&cheese":
    print("You selected Ham&Cheese Pizza.")

    AyonSize = input("Enter the size \nSmall"
                 "\nMedium"
                 "\nLarge\n").lower()
    if AyonSize == "small":
        Ayonprice = 150
    elif AyonSize == "medium":
        Ayonprice = 200
    elif AyonSize == "large":
        Ayonprice = 250
    else:
        Ayonprice = 0
        print("Invalid Price")
else :
    Ayonprice = 0
    print("Invalid pizza flavor.")

if Ayonprice > 0:
        print("Pizza Price:",Ayonprice)









































