string = input("Enter the string: ")
char = input("Enter the character: ")

freq = 0
for i in string:
    if char.lower() == i.lower():
        freq+=1


print("The frequency of the character in the string is ", freq)
toBeReplaced= input("Enter the character to be replaced: ")
replacedBy= input("Enter the character to be replaced by: ")
print(string.replace(toBeReplaced, replacedBy))


toBeRemoved = input("Enter the character you want to remove: ")
print(string.replace(toBeRemoved,"",1))
print(string.replace(toBeRemoved,""))
