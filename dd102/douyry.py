contact = {}
def display_contact():
    print("Name \t\tcontact number ")
    for key in contact :
        print("{}\t\t{}".format(key,contact.get(key)))
while True :
    choice = int(input("1-add new contact \n 2-search contact \n 3-display contact \n 4-edit contact\n 5-delete contact \n 6-exit \n enter ur choice   "))
    if choice == 1:
        name = input ("enter the contact name ")
        phone = input ("enter the mobile number ")
        contact[name] = phone
    elif choice == 2:
        search_name =  input ("enter the contact name ")
        if search_name in contact :
            print(search_name,"'s contact number is ",contact[search_name])
        else :
            print(search_name , "'s not in the contact book")
    elif choice == 3:
        if not contact :
            print("empty contact book ")
        else :
            display_contact()
    elif choice == 4 :
        edit_contact =  input("enter the contact to be edited ")
        if edit_contact in contact :
            phone=input("the number of the contact")
            contact[edit_contact]=phone
            print("contact updated")
            display_contact()
        else:
            print(edit_contact,"not found in contact book ")
    elif choice == 5 :
        del_contact = input("enter the contact to be deleted ")
        if del_contact in contact :
            confirm = input(" do you want to delet this contact y/n ")
            if confirm == 'y' or 'Y':
                contact.pop(del_contact)
                display_contact()
        else :
            print(del_contact,"not found in contact book ")
    else :
        break 






        