login_details = {}
print("===========welcome to R.R.C.G Restaurant===========\n===========Register Below to be able to order food===========")
login_details["username"] = input("username: ")
login_details["password"]  = input("password: ")
print(login_details)
print("===========This is our menu list===========")
menu_list ={
            "one":"1. Amala only",
            "two":"2. Amala and Ewedu with beef",
            "three":"3. Amala and Ewedu with Gbegiri with beef and chicken",
            "four":"4. Amala and Egusi with chicken",
            "five":"5. White Rice with Chicken",
            "six":"6. jollof rice only",
            "seven":"7. fried rice only with chicken",
            "eight":"8. jollof and fried rice chicken",
            "nine":"9. Ghana jollof rice with chicken",
            "ten":"10. pasteries"}
print(menu_list)
print("Please NOTE that #500 is the delivery fee")
order = int(input("ENTER A NUMBER TO ORDER: "))
while True:
    if order == 1:
        print(menu_list["one"])
        print("The price is #700")
        break
    elif order == 2:
        print(menu_list["two"])
        print("The price is #1500 per plate")
        break
    elif order == 3:
        print(menu_list["three"])
        print("The price is #3500 per plate")
        break
    elif order == 4:
        print(menu_list["four"])
        print("The price is #1500 per plate")
        break
    elif order == 5:
        print(menu_list["five"])
        print("The price is #500 per plate")
        break
    elif order == 6:
        print(menu_list["six"])
        print("The price is #1500 plate")
        break
    elif order == 7:
        print(menu_list["seven"])
        print("The price is #1500 per plate")
        break
    elif order == 8:
        print(menu_list["eight"])
        print("The price is #1500 per plate")
        break
    elif order == 9:
        print(menu_list["nine"])
        print("The price is #1500 per plate")
        break
    elif order == 10:
        print(menu_list["ten"])
        print("The price is #2500 per plate")
        break
    else:
        print("SORRY WE DO NOT HAVE THAT ON THE LIST")
        break
    Address = input("ENTER YOUR ADDRESS: ")
    print("Please Proceed to make your payment")
    print("Do you want to Pay with Your Debit Card or Pay on Delivery")
    payment = input("ENTER PAYMENT METHOD: ")
    if payment.upper() == "DEBIT CARD":
        print("Add ------Credit or Debit Card+++++++")
        money = int(input("Enter Card Number: "))
    elif payment.upper() == "PAY ON DELIVERY":
        print("======== PLEASE ENSURE YOU PAY TO THE DELIVERY MAN :) ========")
        print("YOUR FOOD WOULD GET YOU IN THE NEXT 20 MINUTES, /nIF NOT PLEASE CONTACT OUR CUSTOMER CARE 08034351010 OR 08136071724")
        print("TO ORDER MORE FOOD PLEASE RESTART THE PROCESS AGAIN !!!!!!!")
        print("======== THANKS FOR EATING WITH US :) ========")
