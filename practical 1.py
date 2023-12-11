def quadraticRoots(userInput):
    coefficientList = userInput.split(',')

    a=int(coefficientList[0].strip())
    b=int(coefficientList[1].strip())
    c=int(coefficientList[2].strip())

    disc = (b*b) - (4*a*c)

    if (disc<0):
        print("No real roots")
    else:
        r1 = (-b + (disc)**0.5)/(2*a)
        r2 = (-b - (disc)**0.5)/(2*a)


        print("Root 1 : ",r1," Root 2 : ",r2)
        
    
userInput = input("Enter the value of a, b and c separated by ',' : ")


quadraticRoots(userInput)
