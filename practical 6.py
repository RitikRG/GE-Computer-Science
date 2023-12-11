string1 = input("Enter the value of the first string: ")
string2 = input("Enter the value of the second string: ")
n = eval(input("Enter the value of n: "))

if n>len(string1) or n>len(string2):
    print("Entered n is greater than the length of string itseld")
else:
    newStr1 = string1[:n] + string2[n:]
    newStr2 = string2[:n] + string1[n:]
    print(newStr1)
    print(newStr2)
