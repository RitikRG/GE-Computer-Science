def evenCubes(userInput):
    userInputList = userInput.split(",")
    cubesList=[]
    for i in userInputList:
        if i.strip().isdigit():
            temp = int(i)
            if temp%2==0:
                cubesList.append(temp**3)
    print(cubesList)


userInput = input("Enter the list of elements separated by ',': ")

evenCubes(userInput)
