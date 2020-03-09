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
        
        

#list of entrees ["dish name", price]
entrees_list = [["Nachos", 12], ["Rice", 15], ["Apple Slices", 2]]
#list of mains ["dish name", price]
mains_list = [["burger", 20], ["Soup", 22], ["Toastie", 18]]
#list of deserts ["dish name", price]
deserts_list = [["Ice cream", 10], ["Cake", 13],["Cheesecake", 15]]


#list of specials[is_available, what_course, dish_name, price]
specials_list = [[True, entrees_list, "Cerial of the day", 15]]
        
    #asks user for input 
    
#asks user to enter order or enter specials
ask = get_correct_input("What would you like to do?\n 1) Enter order\n 2) Edit specials\n>>>: ", 2)
 
#enter order 
if ask == 0:
    print ("What course?")
    print_list_options(entrees_list)
    for i in range(0, len(specials_list)):
        print(i+len(entrees_list)+1 )
    
    
#edit specials
if ask == 1:
    print ("Enter username ")