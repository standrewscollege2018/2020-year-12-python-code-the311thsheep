"""travel system"""
"""21/02/2020"""
"""Sophia"""

#list of starting points
#start_point_list[place][connecting_flight_cost]
start_point_list = [["Auckland", 0], ["Wellinton", 50], ["Christchurch", 75]]

#destinations list
#destination_list[place][flight_cost]
destination_list = [["Sydney", 326], ["Tonga", 378], ["Shanghai", 1436], ["London", 2376]]

#accomodation list
#accomodation_list[place][cost]
accomodation_list = [["Sydney", 120], ["Tonga", 40], ["Shanghai", 60], ["London", 80]]

#user choices list
choices_list = []

#asks again if user enters str or 
#out of range when asking for int
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

#asks user to choose an option
def ask_for_data(what_choosing, l):
    print ("choose a ", what_choosing, "for your trip: ")
    for i in range (0, len(%l)):
        print(i, ") ", l[i][0], ", $", l[i][1])
        
    
get_correct_input(ask_for_data("start point", start_point_list), len(start_point_list))


  
    #add a student 
    #new_choice = input()
    #new_score = int(input("type the score of the new student: "))
    #students.append([new_student, new_score])
    #prints all students
    #print_students()