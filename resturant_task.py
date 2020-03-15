"""resturant task"""
"""can enter order or edit specials"""
"""started 10/3/2020 by Sophia"""


"""asks again if user enters str or out of range value when asking for int"""
def get_correct_input(prompt, length = 5):
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

"""add specials to available specials list"""
def add_to_today(l, course_specials_list):
    for i in range(0, len(course_specials_list)):
        #if special is currently available
        if course_specials_list[i][0] == True:
            #adds to available today list 
            l.append(course_specials_list[i])
            #deletes boolean
            del(l[-1][0])    


"""prints options from a list """
def print_list_options(l):
    for i in range(0, len(l)):
        print(i+1, ") ", l[i][0], ", $", l[i][1])
        
"""print specials options"""
def print_specials_options(l, course_specials_list):
    print ("SPECIALS")
    for i in range(0, len(course_specials_list)):
        #prints index and name of special and price
        print(i+len(l)+1, ") ", course_specials_list[i][0], ", $", course_specials_list[i][1])
            
        
"""add to order"""
def add_to_order(course_input, course_list, course_specials_list, quantity):
    
    #assigns item and quantity to order list
    #if order is not a special
    if course_input < len(entrees_list):
        order[0].append([course_list[course_input], quantity])
    #if prder is a special
    else:
        order[0].append([course_specials_list[course_input-len(course_list)], quantity])
           

"""prints order"""
def print_order(course):
    if course == 0 and order[0] != None:
        print ("ENTREES:")
    elif course == 1 and order[1] != None:
        print ("MAINS:")
    elif course == 2 and order[2] != None:
        print ("DESSERTS:")
    for i in range(0, len(order[0])):
        print (order[course][i][0][0], "x", order[course][i][1] , "= $", (order[course][i][0][1]*order[course][i][1]), "($", order[course][i][0][1], "each)\n")
    



#list of entrees ["dish name", price]
entrees_list = [["Nachos", 12], ["Rice", 15], ["Apple Slices", 2]]
#list of mains ["dish name", price]
mains_list = [["burger", 20], ["Soup", 22], ["Toastie", 18]]
#list of deserts ["dish name", price]
deserts_list = [["Ice cream", 10], ["Cake", 13],["Cheesecake", 15]]


#list of specials[is_available, dish_name, price] including not available 
all_entree_specials_list = [[True, "Cerial of the day", 15], [False, "fish of the day", 20], [True, "omlette of the day", 13]]
all_mains_specials_list = [[True, mains_list, "soup of the day", 16]]
all_desserts_specials_list = []

#list of specials available today
entree_specials_list = []
mains_specials_list = []
desserts_specials_list = []

#list order is saved to [entrees], [mains], [desserts]  
order = [[], [],[]]



ask = get_correct_input("What would you like to do?\n 1) Enter order\n 2) Edit specials\n>>>: ", 2)
#enter order 
if ask == 0:
    
    #adds current specails to available list 
    add_to_today(entree_specials_list, all_entree_specials_list)
    add_to_today(mains_specials_list, all_mains_specials_list)
    add_to_today(desserts_specials_list, all_desserts_specials_list)
               
    
    
    print ("What course?\n 1) Entree\n 2) Main\n 3) Desert")
    ask_course = get_correct_input(">>>: ", 3)
    
    
    #asks user what entrees they want
    if ask_course == 0:
        print (entree_specials_list)
        ENTREES = True
        while ENTREES == True:
        #prints entrees 
            print_list_options(entrees_list)
        #prints availables entree specials and assigns number of available entree specials to variable 'len_entree_specials'
            print_specials_options(entrees_list, entree_specials_list)
        #asks user and assigns user choice to variable 'ask'
            entrees_input = get_correct_input(">>>: ", len(entrees_list)+len(entree_specials_list))
        #aks user how many of this item they would like 
            quantity = get_correct_input("How many of these would you like?\n>>>: ") + 1
        

            print(" 1) Confirm order\n 2) Order more entriees\n 3) Cancel order")
            ask_reloop = get_correct_input(">>>: ", 3)
            if ask_reloop == 0:
                add_to_order(entrees_input, entrees_list, entree_specials_list, quantity)
                break        
            elif ask_reloop == 1:
                add_to_order(entrees_input, entrees_list, entree_specials_list, quantity)
            else:
                break 
       
            
    #asks user what mains they want    
    elif ask_course == 1:
        print()
        
print ("your order is :\n")



for i in range(0, len(order[0])):
    print (order[0][i][0][0], "x", order[0][i][1] , "= $", (order[0][i][0][1]*order[0][i][1]), "($", order[0][i][0][1], "each)")


#edit specials
if ask == 1:
    print ("Enter username ")