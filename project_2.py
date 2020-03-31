#Linh

import sys

rest_data = "costa_restaurants.txt"
#change the variable name to differentiate menu data

menu_dict = "menu_index.txt" # dictionary of menu and index

def greetings() -> str:
    print("Hello! Welcome to Costa Mesa Bussiness Owner Portal")
    print("***********Where should we eat tonight?************")
    print("-------------------Menu Feature--------------------")
    name = str(input("What is your restaurant name? "))
    return name

#this function opens a file in the same directory, reads the file, and returns
#a list of LISTS comprised of the lines from the file
#(CHANGE) instead of list of string in quiz 4
def read_file(file : str) -> list:
    my_list = []

    try:
        with open(file) as fin:
            for line in fin:
                line_list = line.split(",")
                my_list.append(line_list)
        return my_list
    
    except OSError:
        print("Cannot open", file)
    
#(CHANGE) this function takes a restaurant name and a list of reataurant as
#parameters to check for duplication
def duplicate(name : str, rest_list : list) -> bool:
    for each_list in rest_list:
        if name.casefold() == each_list[0].casefold():
            return True
        else:
            return False  

#this function asks user to enter a menu pdf file and check if that file is a
#pdf file, then return the file name
def menuFile() -> str:
    menu_file = str(input("Enter the menu pdf file: "))

    while menu_file.endswith(".pdf") == False:
        print("You must provide a pdf file!")
        menu_file = str(input("Enter the menu pdf file: "))

    return menu_file    

def add_menu(rest_name : str, menu_name : str, file : str):
    try:
        fin = open(file, 'r+')
        for line in fin:
            line_list = line.split(",")
            if line_list[0].casefold() == menu_name.casefold():
                if line_list[-1].casefold() == menu_name.casefold():
                    print("The menu is already in our data!")
                else:
                    fin.write(menu_name)
                    break

    except OSError:
         print("Cannot open", file)           
    
def import_menu(file : str, menu_path : str):
    index = 0
    
    try:
        fin = open(file, 'w+')
        for line in fin:
            index += 1
        new_line = str(++index) + " " + menu_path
        fin.write(new_line)
        fin.close()
        
    except OSError:
        print("Cannot open", file)
        
def new_restaurant(name : str): # this function prompts the user to enter new 
                      # information and return a list of those information
                      # (CHANGE) instead of a string in quiz 4, also checking
                      # for required fields 
    print("This restaurant is not in our data.")
    print("Please provide these information:")

    my_list = []
    my_list.append(name)
    
    address = str(input("Address: "))
    my_list.append(address)
    
    zipCode = str(input("Zip code: "))

    if zipCode != "":
        while (zipCode.isnumeric() == False) or (len(zipCode) != 5):
            print("Invalid zip code! Enter again")
            zipCode = str(input("Zip code: "))

    my_list.append(zipCode)
    
    vegetarian = str(input("Does it serve vegetarian?(yes/no) "))
    while vegetarian == "":
        print("You cannot skip this information!")
        vegetarian = str(input("Does it serve vegetarian?(yes/no) "))
    my_list.append(vegetarian)
    
    vegan = str(input("Does it serve vegan?(yes/no) "))
    while vegan == "":
        print("You cannot skip this information!")
        vegan = str(input("Does it serve vegan?(yes/no) "))
    my_list.append(vegan)
    
    gluten_free = str(input("Does it serve gluten-free?(yes/no) "))
    while gluten_free == "":
        print("You cannot skip this information!")
        gluten_free = str(input("Does it serve gluten-free?(yes/no) "))
    my_list.append(gluten_free)
    
    return my_list

def add_list(rest_list : list, menu_name : str, file : str):
    try:
        fin = open(file, 'r+')
        fin.read()
        fin.write('\n')
        seperator = ", "
        new_line = seperator.join(rest_list)
        fin.write(new_line)
        menu_name = ", " + menu_name
        fin.write(menu_name)
        fin.close()
        
    except OSError:
        print("Something's wrong. Cannot open", file)

def add_more() -> bool:
    answer = str(input("Do you want to add another menu?(yes/no) "))
    try:
        if answer.casefold() == "yes":
            return True
        elif answer.casefold() == "no":
            print("Thank you for using Menu Feature. Good bye!")
            return False

    except:
        print("Unexpected answer. Good bye!")

if __name__ == "__main__":    
    #1.Greetings and ask for restaurant name
    rest_name = greetings()

    #2.check if the restaurant already existed
        # 2.1.open and read data file
    my_list = read_file(rest_data)
    
        # 2.2.check duplicate
    check = duplicate(rest_name, my_list)
    
        # 2.3.if existed:
    if check == True:
        
            # 2.3.1.ask for menu file
        menu_name = menuFile()
    
            # 2.3.2.add menu name to data file
        add_menu(rest_name, menu_name, rest_data)
    
            # 2.3.3. add menu file to dictionary file
        menu_path = "costa_menus/%s" % menu_name
        import_menu(menu_dict, menu_path)
    
        # 2.4.if not existed:
            # 2.4.1.ask for new information and make a list
    else:
        new_list = new_restaurant(rest_name)
        
            # 2.4.2.ask for menu file
        menu_name = menuFile()
        
            # 2.4.3.add the list  and menu name to data file
        add_list(new_list, menu_name, rest_data)
        
            # 2.4.4.add menu file to dictionary file
        menu_path = "costa_menus/%s" % menu_name
        import_menu(menu_dict, menu_path)
        
    #3.ask if user wants to add more menu for another restaurant
    answer = add_more()
        # 3.1.if yes: ask for the restaurant name and go back to step 2.2
    while answer:
        name = str(input("What is your restaurant name? "))
        my_list = read_file(rest_data)
        check = duplicate(rest_name, my_list)
        if check == True:
            menu_name = menuFile()
            add_menu(rest_name, menu_name, rest_data)
            menu_path = "costa_menus/%s" % menu_name
            import_menu(menu_dict, menu_path)
        else:
            new_list = new_restaurant(rest_name)
            menu_name = menuFile()
            add_list(new_list, menu_name, rest_data)
            menu_path = "costa_menus/%s" % menu_name
            import_menu(menu_dict, menu_path)
            answer = add_more()
        # 3.2.if no: end program
        
        
    
            
                  
    
