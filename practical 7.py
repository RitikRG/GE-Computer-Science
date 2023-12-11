string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

if string2 in string1:
    indeciesList=[]
    start=0
    while start<len(string1):
        temp = string1.find(string2, start)
        if temp == -1:
            break
        else:
            indeciesList.append(temp)
            start=temp
        start+=1

    print(indeciesList)
else:
    print(-1)
