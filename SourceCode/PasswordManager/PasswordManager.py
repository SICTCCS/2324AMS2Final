
from Account import Account
import random
masterpassword="admin"
masterusername="admin"
username =" "
password = " "
user = " "
#TODO: this version relys on multiple lists to store all of the data, modify it to save all
#   accounts into one list instead.
userEntryList=[]
usernameList = []
firstNameList = []
lastNameList = []
passwordList = []
cateList=[]
i=0

def viewByCate():
  categoryToFind = str(input("What Category do you want to look for "))
  for i in range(len(userEntryList)):
    if userEntryList[2] == categoryToFind:
      print(userEntryList[2])

def buildCateList():
  for i in range(len(userEntryList)):
    if not userEntryList[2] in cateList:
      cateList.append(userEntryList[2])

def saveToText():
    print(userEntryList)
    for user in userEntryList:
        fileToWriteTo = open(f"{userEntryList[0]}_{userEntryList[1]}_{userEntryList[2]}.txt","w")
        fileToWriteTo.write(user.__str__())    #print does the __str__ for you -> write does not
        fileToWriteTo.close()

def login():
    username =" "
    password = " "
    i=0
    while username!= masterusername and password!= masterpassword and i!=3:
            print("You only have three tries")
            username = input("username: ")
            password = input("password: ")
            if username == masterusername and password == masterpassword:
                print("you are signing in ")
            else:
                i+=1
                print("too many trys")
# print("too many trys")

def addEntry():
  ui=input("Do you want to make an account or an entry ")
  if ui == "account":
    username = input("What do you want your username to be ")
    password = input("What password do you want ")
    first = input("What is your first name ")
    last = input("What is your last name ")
    usernameList.append(username)
    passwordList.append(password)
    # TODO:  Currently this edition, saves their firstname and lastname this isn't necessary
    firstNameList.append(first)
    lastNameList.append(last)
    print(f"{username}\n{password}\n{first}\n{last}")
  elif ui == "entry":
    username=input("What do you want your username to be ")
    password=input("what do you want your password to be ")
    category=input("What category is this under ")
    userEntryList.append(username)
    userEntryList.append(password)
    userEntryList.append(category)
 
 
sign=input("Whould you like to sign in or register? ")
if sign=="sign in":
    login()
else:
    addEntry()
    print("Please sign in")
    login()
 
 
# menu = '''
# "add"
# "edit"
# "remove"
# "view all"
# "view by category"
# '''

# def viewByCate():
    
    
# def buildCateList():
# print(menu)
# '''

#     if ui == login
#         login()
#     else:
#         register()
#         login()
# '''
# def addEntry():
menu='''
What would you like to do?
    "add"
    "edit"
    "remove"
    "view all"
    "view by category"
    "random generated password"
    "exit"
'''
user = input(menu)

while user !="quit":
  
    if user == "add":
        addEntry()
        saveToText()
        print(menu)
        user=input("what would you like to do ")

    elif user == "edit":
        #This is broken, but will fix in another rev
        first = ""
        last = ""
        idToEdit = int(input("Which account needs to be edited?   "))
        print(username==usernameList[idToEdit].get_user_name())
        if(username==usernameList[idToEdit].get_user_name()):
          print(password==passwordList[idToEdit].get_password())
          if(password==passwordList[idToEdit].get_password()):
            print(first==firstNameList[idToEdit].get_first())
            if(first==firstNameList[idToEdit].get_first()):
              print(last==lastNameList[idToEdit].get_last())
              if(last==lastNameList[idToEdit].get_last()):
                newEntry=input("What is the new entry")
                userEntryList[int(idToEdit)].set_entry(newEntry)
              
    elif user == "remove":
        idToRemove=input("Which account needs to be removed?  ")
        del userEntryList[int(idToRemove)]
    elif user == "view all":
        #TODO:  This infinite loops...
        print(userEntryList)
    elif user == "view by category":
        #TODO: Make sure this doesn't run unless there is at least one category
        buildCateList()
        viewByCate()

    elif user == "random generated password":
        #TODO:  This needs to be a function that is in another file

        #TODO:  Remove this long tuple and setup a range of numbers
        characters1 = (33,64,35,36,37,38,40,41,42,43,45,48,49,50,51,52,53,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122)        #numbers and letters(lowercase and uppercase)
        specialCharacters = (33,35,36,37,38,40,41,42,43,45,64)      #special characters on the keyboard


        password = ""
            
        capitalLetters = int(input("How many capital letters do you want in your password?"))        #asking for characters
        lowerCase = int(input("How many lowercase letters do you want in your password?"))
        numbers = int(input("How many numbers do you want in your password?"))               #asking for numbers
        special = int(input("How many special characters do you want in your password?"))    #asking for special characters like !

        passwordLength = capitalLetters+ lowerCase + numbers + special
        if (capitalLetters <= 0) or (lowerCase <=0) or (numbers <=0 ) or (special <= 0) or passwordLength < 8:              #keeping user from putting in negative 
            while passwordLength < 8 or capitalLetters < 8 or lowerCase < 8 or numbers < 8 or special < 8:
                    print("Password requires at least one uppercase letter, lowercase letter, number, and special character")
                    capitalLetters = int(input("How many capital letters do you want in your password?"))        #asking for characters
                    lowerCase = int(input("How many lowercase letters do you want in your password?"))
                    numbers = int(input("How many numbers do you want in your password?"))               #asking for numbers
                    special = int(input("How many special characters do you want in your password?")) 
                    
                    passwordLength = capitalLetters+ lowerCase + numbers + special
            while passwordLength > 0: 
                i = random.randint(48,122)          #choosing randomly between the ascii chart for characters
                if i in range(48,57):
                    if numbers != 0:
                            numbers -=1 
                            password += chr(i)      #stands for the random choice 
                            passwordLength -=1          #subtracting 1 password length (it repeats from numbers till lowercase)
                elif i in range(65,90):
                    if capitalLetters != 0:
                            capitalLetters -=1
                            password += chr(i)
                            passwordLength -=1
                elif i in range(97,122):
                    if lowerCase != 0:
                            lowerCase -=1 
                            password += chr(i)
                            passwordLength -=1
                elif i in specialCharacters:            #running a special characters
                    if specialCharacters != 0:
                            password += chr(i)          #adding the random special character to the password
                            passwordLength -=1          #subtracting by 1 in the password
        else:
            while passwordLength > 0: 
                i = random.randint(48,122)          #choosing randomly between the ascii chart for characters
                if i in range(48,57):
                    if numbers != 0:
                            numbers -=1 
                            password += chr(i)      #stands for the random choice 
                            passwordLength -=1          #subtracting 1 password length (repeats from numbers to lowercase)
                elif i in range(65,90):
                    if capitalLetters != 0:
                            capitalLetters -=1
                            password += chr(i)
                            passwordLength -=1
                elif i in range(97,122):
                    if lowerCase != 0:
                            lowerCase -=1 
                            password += chr(i)
                            passwordLength -=1
                elif i in specialCharacters:
                    if specialCharacters != 0:
                            password += chr(i)
                            passwordLength -=1
                print(password)                             #printing the random generated password
    elif user == "exit":
        #TODO save the information to a text file
        continue
else:
    print("Invalid input")
user=input(menu)