import json

phonebook = {}

print("Menu: \n (A)dd Contact \n (S)earch Contact \n (D)elete Contact \n (E)dit Contact \n (Ex)it")

while(True):
    req=input("What do you want to do? ").upper()

    if(req=="A"):
        name=input("What's the name? ").lower()
        number=input("What's the number? ")
        phonebook[name]=number

    elif(req=="S"):
        name=input("Whose number do you want? ").lower()
        number=phonebook.get(name, "Contact not found!!")
        print(f"Here's the number: {number}")

    elif(req=="D"):
        name=input("Whose number do you want to delete? ").lower()
        if name in phonebook:
            del phonebook[name]
            print("Number deleted successfully!!")
        else:
            print("Number not found!!")

    elif(req=="E"):
        name=input("Whose number do you want to update? ").lower()
        new_num=input("Enter the new number: ")
        phonebook[name]=new_num

    elif(req=="EX"):
        print("phonebook saved successfully!!")
        with open("my_contacts.txt", "w") as f:
            f.write(str(phonebook)) 
        print("Phonebook saved to 'my_contacts.txt'. Check your folder!")
        break

    else:
        print("Not a valid operation!!")
    


