

# Restaurant menu system start

def start():
    init = input("""
    WELCOME TO PYTHON RESTAURANT

    What would you like to do :

    1. Log into Admin Panel
    2. Book a table
    3. Order meals
    4. View Menu Only

    >>>""")
    if init == "1":     # This will redirect the client to the admin panel
        admin()
    elif init == "2":
        book_table()    # This will redirect the client to the table booking section
    elif init == "3":
        order_meal()    # This will redirect the client to order a meal
    elif init == "4":
        menu()
    else:
        # This will throw an error if the user did not pick a correct choice
        print("Invalid Choice")
        start()


# Admin panel function

def admin():
    pin = input("""     
    
    Pls Input Your Pin?
    
    input  " X " to remain to main menu

    >>""")
    if pin == "2304":   # This asks the client for their pin to authenticate if the client is a staff of the restaurant......only staffs should know this pin
        log = input("""

        Login Succesfull !!!

        Welcome to the Restaurant admin dashboard !!!

        >>>""")

    elif pin == "x":   # if this option is picked it means the client does not know the pin and is not a staff, the client is redirected back to the main menu
        return start()

    else:             # This keeps throwing an error as long as the client keeps inputting a wrong pin
        print("Error: Invalid Pin")
        return admin()


# This function is for table booking. Things like name and email are asked for before allowing clients pick aan available table

def book_table():
    name = input("""
    
    Pls input your name:

    Input " X to return to main menu "
    
    >>""")
    if name == "x":
        return start()  # This returns the client back to the main menu

    email = input("""
    
    Pls input your email:

    Input " X to return to main menu "
    
    >>""")
    if email == "x":
        return start()

    date = input("""
    
    What date should we expect you :

    Input " X to return to main menu "
    
    >>""")
    if date == "x":
        return start()

    time = input("""
    
    At what time should we expect you :

    Input " X to return to main menu "
    
    >>""")
    if time == "x":
        return start()

    tables = input("""

    What table would you like to book :

    2       4       5   

    6       7       8

    10       13     15

    input  " X " to return to main menu

    >>>""")
    if tables == "x":
        return start()
    else:   # After client has commpletely filled all these informations these is printed unto the terminal
        print('>>>>> Dear,', name, 'your table no', tables, 'has been booked for ',
              date, 'at', time, 'and a confirmation email has been sent to', email)


def order_meal():

    fooditems = ""  # Empty Cart, as items are being selected, they are added to these variable which will be printed out when cart is selected

    totalcharge = 0  # No Food item in cart to add up total charge, as meals are being added to cart, these is being increased by the food price

    timetaken = 0   # this is just the approximate  time it takes to prepare and deliver the meal, each meal has its own time,
    # and these will be filled by the highest time for a meal the client chooses

    # These are variables that carries a meal, its price, the time to prepare & deliver it, when they are chosen they are added to the cart var ( fooditems )
    item1 = "1. Delicious Pasta in red sauce       ₦ 2,300"
    t1 = 10
    p1 = 2300
    item2 = "2. Nigerian Jollof Rice               ₦ 5,000"
    t2 = 10
    p2 = 5000
    item3 = "3. Spaghetti and Fish Stew            ₦ 2,000"
    t3 = 15
    p3 = 2000
    item4 = "4. Eba and Ogbono Soup                ₦ 3,000"
    t4 = 18
    p4 = 3000
    item5 = "5. Catfish Pepper Soup                ₦ 1,500"
    t5 = 12
    p5 = 1500
    item6 = "6. Banga Soup and Starch              ₦ 3,000 "
    t6 = 18
    p6 = 3000
    item7 = "7. Amala and Efo riro                 ₦ 2,000"
    t7 = 16
    p7 = 2000
    item8 = "8. Egusi Soup and Semolina            ₦ 3,000"
    t8 = 15
    p8 = 3000
    item9 = "9. Beans And Boli                     ₦ 1,000"
    t9 = 10
    p9 = 100
    item10 = "10. Yam and Fish Stew                 ₦ 1,500"
    t10 = 16
    p10 = 170
    while(True):        # This while loop continues printing out the menu for the client to keep adding meal items to cart
        print("""
        
        ******************************************************************************************

                                                Python   -  Restaurant
                                                *****  Nigerian  *****

                                1. Delicious Pasta in red sauce          ₦ 2,300
                                2. Nigerian Jollof Rice                  ₦ 5,000
                                3. Spaghetti and Fish Stew               ₦ 2,000
                                4. Eba and Ogbono Soup                   ₦ 3,000

                                                *****Specials*****

                                5. Catfish Pepper Soup                   ₦ 1,500
                                6. Banga Soup and Starch                 ₦ 3,000
                                7. Amala and Efo riro                    ₦ 2000

                                                *****Low Price Delicacies*****

                                8. Egusi Soup and Semolina               ₦ 3000
                                9. Beans And Boli                        ₦ 1,000
                                10. Yam and Fish Stew                    ₦ 1500

        ******************************************************************************************
        To add meals to cart select the meal number...keep selecting to keep adding  more to cart

        S. Show cart
        X. Checkout
        E. Exit
        """)

        opt = input(
            "Please enter a meal no to add it to cart or choose an option :")
        if opt == "1":
            # This adds var 1 to cart, var 1 contains a meal item
            fooditems = fooditems + "\n"+item1
            # This adds up price of meal in var 1 to the total price already in cart
            totalcharge = totalcharge+p1
            if t1 > timetaken:              # this checks if the time to prepare and deliver var 1 meal item is greater than the highest time to prepare in the cart
                # If the time is greater, the var 1 timing overrides the one previously in the cart.
                timetaken = t1
        elif opt == "2":
            fooditems = fooditems + "\n"+item2  # This is repeated for var 1 to var 10
            totalcharge = totalcharge+p2
            if t2 > timetaken:
                timetaken = t2
        elif opt == "3":
            fooditems = fooditems + "\n"+item3
            totalcharge = totalcharge+p3
            if t3 > timetaken:
                timetaken = t3
        elif opt == "4":
            fooditems = fooditems + "\n"+item4
            totalcharge = totalcharge+p4
            if t4 > timetaken:
                timetaken = t4
        elif opt == "5":
            fooditems = fooditems + "\n"+item5
            totalcharge = totalcharge+p5
            if t5 > timetaken:
                timetaken = t5
        elif opt == "6":
            fooditems = fooditems + "\n"+item6
            totalcharge = totalcharge+p6
            if t6 > timetaken:
                timetaken = t6
        elif opt == "7":
            fooditems = fooditems + "\n"+item7
            totalcharge = totalcharge+p7
            if t7 > timetaken:
                timetaken = t7
        elif opt == "8":
            fooditems = fooditems + "\n"+item8
            totalcharge = totalcharge+p8
            if t8 > timetaken:
                timetaken = t8
        elif opt == "9":
            fooditems = fooditems + "\n"+item9
            totalcharge = totalcharge+p9
            if t9 > timetaken:
                timetaken = t9
        elif opt == "10":
            fooditems = fooditems + "\n"+item10
            totalcharge = totalcharge+p10
            if t10 > timetaken:
                timetaken = t10
        # If the client chooses this ( e ) it breaks off the 'while' loop which allows multiple items to be added to the cart
        elif opt == "e":
            break
        # if the clients chooses this ( s ) it prints out the cart ( which are the meals added to the var 'food items '), in a formatted manner
        elif opt == "s":
            print(fooditems)
            print("-"*90)
            print("\t\t\t Total = ₦ "+str(totalcharge))
            input()
        # If the clients chooses this ( x ), this will checkout the user
        elif opt == "x":
            address = input("Pls type in your address >>>")
            print(fooditems)
            print("-"*90)
            print("\t\t\t\t\t ₦ "+str(totalcharge))
            if totalcharge > 0:
                print("Your food will arrive at", address, " in a maximum of ",
                      timetaken, "minutes")  # timetaken is the time it will will take to prepare & deliver the most complex meal in the cart
                print("You can pay on delivery...")
                input()
            else:           # This throws an error if there is nothing in the clients cart
                print(
                    ">>>>>>> Nothing in your cart. Please select the food items you would like to order")
                input()
        else:               # This throws an error if the client selected a meal no that does not exists on the menu
            print("Invalid food choice/option selection")
            input()

    print("""
        ******************************************************************************************
                            Thank you for visiting the Python Restaurant
                                    Hope you enjoy your food
        ******************************************************************************************
    """)

    # This function just shows the clients the menu


def menu():
    print("""
           ******************************************************************************************

                                                Python Restaurant
                                                *****  Nigerian  *****

                                     Delicious Pasta in red sauce          ₦ 2,300
                                     Nigerian Jollof Rice                  ₦ 5,000
                                     Spaghetti and Fish Stew               ₦ 2,000
                                     Eba and Ogbono Soup                   ₦ 3,000

                                                *****Specials*****

                                     Catfish Pepper Soup                   ₦ 1,500
                                     Banga Soup and Starch                 ₦ 3,000
                                     Amala and Efo riro                    ₦ 2000

                                             *****Low Price Delicacies*****

                                     Egusi Soup and Semolina               ₦ 3000
                                     Beans And Boli                        ₦ 1,000
                                     Yam and Fish Stew                     ₦ 1500

        ******************************************************************************************

        1. Return to main menu
        2. Order a meal
       """)
    r = input(">>>")
    if r == "1":        # if the clients decides to return to the main menu this will execute the main menu function start()
        return start()
    elif r == "2":      # if after previewing the menu they decide to order a meal, this executes the order meal function order_meal()
        return order_meal()
    else:               # if the client enters a choice that is not correct this throws an error
        print("Invalid Choice")
        return menu()


start()  # This will start the application when this python file is run on the terminal
