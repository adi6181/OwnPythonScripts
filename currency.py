EUR = 1
USD = 1.13
INR = 0.85
RUB = 74.65

def currencyConverter():
    choosenCurrency = input("Do you wish to convert your euros into \n1)USD \n2)RUB \n3)GBP\n\n")
    print(("-" * 36) + "\n")
    print (choosenCurrency, "\n\n" + ("-" * 36))

    # USD
    if (choosenCurrency) == "1":
        eurAmount = round(float(input("How many euros do you wish to convert into USD?\n\n")))
        print(("-" * 36) + "\n")
        print(eurAmount, "euro is", round((eurAmount) * 1.13, 2), "US dollar.\n\n" +("-" * 36), "\nThank you for using!")

    # RUB
    elif (choosenCurrency) == "2":
        eurAmount = round(float(input("How many euros do you wish to convert into RUB?\n\n")))
        print(("-" * 36) + "\n")
        print(eurAmount, "euro is", round((eurAmount) * 74.65, 2), "US dollar.\n\n" +("-" * 36), "\nThank you for using!")

    # INR
    elif (choosenCurrency) == "3":
        eurAmount = round(float(input("How many euros do you wish to convert into GBP?\n\n")))
        print(("-" * 36) + "\n")
        print(eurAmount, "euro is", round((eurAmount) * 0.85, 2), "US dollar.\n\n" +("-" * 36), "\nThank you for using!")

    # Fail
    else:
        print("Error, Please try again. \nEnter 1 for USD")

currencyConverter()