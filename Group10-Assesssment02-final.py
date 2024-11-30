import datetime
import re
import sys

userFirstName = []
userLastName = []
userMobileNumber = []
userPassword = []
userYob = []


def getUserName(userFirstName, userLastName):
    userInputFirstName = input("Please enter your First Name: ")
    userInputLastName = input("Please enter you Last Name:")
    userFirstName.append(userInputFirstName)
    userLastName.append(userInputLastName)


def getUserMobileNumber(userMobileNumber):
    while True:
        userInputNumber = input("Please enter your Mobile Number: ")
        if len(userInputNumber) == 10 and userInputNumber[0] == '0':
            break
        else:
            print(
                "Invalid mobile number. Please ensure that the mobile number has 10 digits and starts with '0'.")
    userMobileNumber.append(userInputNumber)


def getUserPassword(userPassword):
    while True:
        userInputPassword = input("Please enter your Password: ")
        if len(userInputPassword) < 8:                           
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]', userInputPassword) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]', userInputPassword) is None:
            print("Make sure your password has a capital letter in it")
        else:
            while True:
                userReInputPassword = input("Please confirm you Password: ")
                if userReInputPassword == userInputPassword:
                    break
                else:
                    print("Password not matching, Please try again")
            break
    userPassword.append(userInputPassword)


def getUserYob(userYob): #i have modified this too
    while True:
        userInputYob = input("Please enter your year of birth in YYYY format: ")
        if userInputYob.isdigit() and len(userInputYob)==4:
         age = datetime.datetime.now().year - int(userInputYob)
         if age >= 21:
            break
         elif age<= 21:
            print(
                "Age requirement not met. You must be at least 21 years old to sign up.")
        else:
            print("The date of birth you entered is not valid.")
    userYob.append(userInputYob)


def userSignIn(userMobileNumber, userPassword): #i have modified it you can change if thereis better solution
    while True:
        userInputNumber = input("please enter your ID (mobile numbers): ")
        if userInputNumber in userMobileNumber:
            x = userMobileNumber.index(str(userInputNumber))
          
            while True:
                userInputPassword = input("please enter your password: ")
                y = str(userInputPassword)
                if y == userPassword[x]:
                    print("You successfully to logged in to the system.")
                    print("Welcome back", userFirstName[x], userLastName[x])
                    break
                else:
                    print("The password you enterd is wrong please try again.")
            break
        else:
            print("You have not Signed up with this Contact Number, Please Sign Up First")
            print("Please Select from the following:")
            print("1 for Signup.")
            print("2 for Signin.")
            print("3 to Quit.")
            userSelection()
            break
  


# creat reset user password function
def userResetPassword(userMobileNumber, userYob, userPassword):
    print("Please reset the password by entering the below details:")
    # looking for user exits on database
    while True:
        userInputNumber = input(
            "Please enter your Username (Mobile Number) to confirm: ")
        if userInputNumber in userMobileNumber:
            x = userMobileNumber.index(str(userInputNumber))
            break
        else:
            print("Not found your Username (Mobile Number) in systems, please try again")
    # confirm year of birth of user
    while True:
        userInputYob = input(
            "Please enter your year of birth in YYYY format, to confirm: ")
        if userInputYob == userYob[x]:
            while True:
                userInputNewPassword = input(
                    "Please enter your new password: ")
                # compare old pasword with new password
                if userInputNewPassword != userPassword[x]:
                    while True:
                        reEnterPassword = input(
                            "The New Password you just input can use, Please re-enter it: ")
                        # compare new pasword with re-enter new password
                        if reEnterPassword == userInputNewPassword:
                            userPassword.pop(x)
                            userPassword.insert(x, reEnterPassword)
                            break
                        else:
                            print(
                                "Not Matching, please try to re-enter new password: ")
                    break
                else:
                    print("You cannot use the password used earlier.")
            break
        else:
            print("your year of birth not correct, please try again")



def quitApplication():
    print("Thank you for using the application.")
    sys.exit()

def userSelection(): #i did this for task 2
 userSelection = input("Enter your choice: ")
 if userSelection == '1':
     getUserName(userFirstName, userLastName)
     getUserMobileNumber(userMobileNumber)
     getUserPassword(userPassword)
     getUserYob(userYob)
     print("You have successfully Signed up.")
     
 elif userSelection == '2':
     userSignIn(userMobileNumber, userPassword)
     while True:
         print("Please Select from the following:")
         print("1 for Resetting the Password.")
         print("2 for Signout.")

         userSelection = input("Enter your choice: ")
         if userSelection == '1':
             userResetPassword(userMobileNumber, userYob, userPassword)
             break
         elif userSelection == '2':
             break
         else:
             print("Invalid Selection! Try again .")
 elif userSelection == '3':
     quitApplication()
 else:
     print("Invalid Selection! Try again .")


while True:
    print("Please Select from the following:")
    print("1 for Signup.")
    print("2 for Signin.")
    print("3 to Quit.")
    userSelection()