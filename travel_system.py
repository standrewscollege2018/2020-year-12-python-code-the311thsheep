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

#prints options and 
#asks user to choose an option
def ask_for_data(what_choosing, l):
    print ("\n choose", what_choosing, "for your trip: ")
    for i in range(0, len(l)):
        print(i+1, ") ", l[i][0], ", $", l[i][1])
    print (">>>: ")
        
        

    
#user chooses start point    
start_point = get_correct_input(ask_for_data("a start point", start_point_list), len(start_point_list))
print ("you chose ", start_point_list[start_point])
#adds choice to choices_list
choices_list.append(start_point_list[start_point])
start_point_cost = start_point_list[start_point][1]



#user chooses destination    
destination = get_correct_input(ask_for_data("a destination", destination_list), len(destination_list))
print ("you chose ", destination_list[destination])
#adds choice to choices_list
choices_list.append(destination_list[destination])
destination_cost = destination_list[destination][1]
#adds accomodation to choices list
choices_list.append(accomodation_list[destination])
accomodation_cost = accomoadtion_list[destination][1]


#choose how many nights they will be staying 
trip_length = get_correct_input("how many nights will you be staying here? ") + 1 
print ("you said you would be staying for", trip_length, "nights")
choices_list.append(trip_length)

print (choices_list)
  

if trip_length > 2:
    trip_cost = start_point_cost + destination_cost + (accomodation_cost * 0.8 * trip_length)
else:
    trip_cost = start_point_cost + destination_cost + (accomodation_cost * trip_length)
    
print("your trip costs :"