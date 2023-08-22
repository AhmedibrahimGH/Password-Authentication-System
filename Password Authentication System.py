Number_of_Tries = 3

User_Password = "Ahmed130"

User_input = input("Enter Your Password My Booy: ").strip()

while User_input != User_Password:
    Number_of_Tries -= 1  # Drease the Value by one.

    print("Wrong Password Try Again Mf!!")

    print(
        f"Number of left Tries is { 'Zero' if Number_of_Tries ==0 else Number_of_Tries }"
    )  # here we use short if to put condition if tries reach to zero if will print Zero , Otherwise Print Number of Tries.

    # Ask user To Enter New Password if He enters Password in Wrong Way
    User_input = input("Enter Your Password My Booy: ").strip()

    # Here We put the condition if Number of tries reach to zero , it will execute what is inside the condition.
    if Number_of_Tries == 0:
        print("you Can't try Again. ")
        break  # End the loop if Number_of_Tries Become Zero {0}
