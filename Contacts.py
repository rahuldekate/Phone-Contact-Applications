# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:29:12 2019

@author: RAHUL
"""

Dict = {'name' : '', 'phone' : ''}
 
def add():
    name = input("Enter Contact name\n - ")
    
    add = False
    if name in Dict :
        print("Name already exists")
    else:
        add = True
    if add==True:
        phone = input("Enter Phone number\n - ")
        Dict[name]=phone
        print("Contact added successfully!!!")
    main()
    
def search():
    ele = input("Enter contact name\n - ")
    if ele.lower() in Dict:
        print("Phone Number ::" ,(str(Dict[ele.lower()])))
    else:
        print("Contact not found")
    main()

    
def delete():
    dele=input("Enter Contact to be Deleted\n -")
    if dele in Dict :
        del Dict[dele]
        print("Contact deleted successfully!!!\n")
    else:
        print("Contact does not exist\n")   
    main()

    
def view():
    print(Dict)
    main()

    
def update():
    up=input("Enter contact to be updated\n")
    if up.lower() in Dict:
        num2=input("Enter new number\n -")
        Dict[up]=num2
        print("Contact updated successfully!!!\n")
    else:
        print("Contact does not exist\n")
    main()

            
def choice():
    ch = input(""" 
                            
************ P H O N E   C O N T A C T S ***************
  
********************************************************             
         1:Add a Contact
         2:Search a Contact
         3:Delete a Contact
         4:Update a Contact
         5:View all Contacts
         6:Exit
********************************************************       
 Enter Choice ::
         """)
    if ch == '1':
        print("Adding....")
        add()
    elif ch == '2':
        print("Searching...")
        search()
    elif ch == '3':
        print("Deleting....")
        delete()
    elif ch == '4':
        print("Updating....")
        update()
    elif ch == '5':
        print("Viewing....")
        view()
    elif ch== '6':
        print("..... E X I T I N G ......\n")
    else:
        print("Invalid response\n")
        main()
        
 
def main():
        Quit = input("Would you like to continue (y/n) \n - ")
        if Quit == 'n':
            print("..... E X I T I N G .....\n")
        elif Quit == 'y':
            choice()
        else:
            print("Invalid response")
            main()

choice() 
