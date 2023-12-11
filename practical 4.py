userInput = input("Enter the character: ")

if userInput[0].islower() :
    print("Lowercase Character")
elif userInput[0].isupper():
    print("Uppercase Character")
elif userInput.isdigit():
    print("Digit")
    userInput=int(userInput)
    dict = {1:"One", 2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven", 8:"Eight",9:"Nine"}
    print(dict[userInput])
else:
    print("Special Character")
