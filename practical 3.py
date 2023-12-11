def printPattern(row):
    for i in range(1,row+1):

        print(" "*(row-i), end="")
        print("*"*(i-1),end="")
        print("*"*i)
    
    for i in range(1,row):

        print(" "*(i), end="")
        print("*"*(row-i-1),end="")
        print("*"*(row-i))



row = eval(input("Enter the number of rows you want: "))
printPattern(row)
