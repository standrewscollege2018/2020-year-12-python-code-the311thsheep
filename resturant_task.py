"""resturant task"""
"""can enter order or edit specials"""
"""started 10/3/2020 by Sophia"""


"""asks again if user enters str or out of range value when asking for int"""
def get_correct_input(prompt, length = 10000):
    while True:
        try:
            value = int(input(prompt))-1
        except ValueError:
            print ("sorry i didnt understand that, try entering a number")
        else:
            if value in range (0, length):
                break 
            else:
                print ("that value is not in range")        
    return value 


"""prints options from a list """
def print_list_options(l):
    for i in range(0, len(l)):
        print(i+1, ") ", l[i][0], ", $", l[i][1])
        
"""print specials options"""
def print_specials_options(l):
    l_specials = 0
    print ("SPECIALS")
    for i in range(0, len(specials_list)):
        if specials_list[i][1] == l and specials_list[i][0] == True:
            print(i+len(l)+1, specials_list[i][2], ", $", specials_list[i][3])
            l_specials = l_specials+1
    return l_specials
        
        

#list of entrees ["dish name", price]
entrees_list = [["Nachos", 12], ["Rice", 15], ["Apple Slices", 2]]
#list of mains ["dish name", price]
mains_list = [["burger", 20], ["Soup", 22], ["Toastie", 18]]
#list of deserts ["dish name", price]
deserts_list = [["Ice cream", 10], ["Cake", 13],["Cheesecake", 15]]


#list of specials[is_available, what_course, dish_name, price]
specials_list = [[True, entrees_list, "Cerial of the day", 15]]
        
entrees = []
    
    
while True:
    #asks user to enter order or enter specials
    ask = get_correct_input("What would you like to do?\n 1) Enter order\n 2) Edit specials\n>>>: ", 2)
     
    #enter order 
    if ask == 0:
        print ("What course?\n 1) Entree\n 2) Main\n 3) Desert")
        ask = get_correct_input(">>>: ", 3)
        
        
        #asks user what entrees they want 
        if ask == 0:
        #prints entrees 
            print_list_options(entrees_list)
        #prints availables entree specials and assigns number of available entree specials to variable 'len_entree_specials'
            len_entree_specials = print_specials_options(entrees_list)
        #asks user and assigns user choice to variable 'ask'
            entrees_input = get_correct_input(">>>: ", len(entrees_list)+len_entree_specials)
        #aks user how many of this item they would like 
            quantity = get_correct_input("How many of these would you like?\n>>>: ", 5)
        
        
            print(" 1)Confirm order\n 2) Order more entriees\n 3) Cancel order")
            ask = get_correct_input(">>>: ", 3)
            if ask == 0:
                #assigns to entriees list
                entrees.append([entrees_list[entrees_input], quantity])
                print (entrees)
                break
            elif ask == 1:
                continue
           
                
            
        elif ask == 1:
            print()
        
        
    #edit specials
    if ask == 1:
        print ("Enter username ")