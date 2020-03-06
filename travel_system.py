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

#money off if user stays more than 2 nights
ACCOMODATION_BONUS = 0.8

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

"""prints options and asks user to choose an option """
def ask_for_data(what_choosing, l):
    print ("\n choose", what_choosing, "for your trip: ")
    for i in range(0, len(l)):
        print(i+1, ") ", l[i][0], ", $", l[i][1])
   
        
    #asks user for input 
    
#press one to start
ask = get_correct_input("press 1 to start \n>>>: ", 1)
 
    
#user chooses start point  
ask = ask_for_data("a start point", start_point_list)
start_point = get_correct_input(">>>: ", len(start_point_list))

#prints their choice
print ("you chose", start_point_list[start_point][0], "which costs $", start_point_list[start_point][1])
#finds startpoint connection flight cost

start_point_cost = start_point_list[start_point][1]



#user chooses destination 
ask = ask_for_data("a destination", destination_list)
destination = get_correct_input(">>>: ", len(destination_list))

#prints their choice
print ("you chose", destination_list[destination][0], "which costs $", destination_list[start_point][1] )

#finds destination flight cost
destination_cost = destination_list[destination][1]
#finds accomodation cost per night 
accomodation_cost = accomodation_list[destination][1]



#choose how many nights they will be staying 
trip_length = get_correct_input("\nhow many nights will you be staying here? \n>>>: ") + 1 

#prints their choice
print ("you said you would be staying for", trip_length, "nights")





  
#calculate total costs 
if trip_length > 2:
    trip_cost = start_point_cost + destination_cost + (accomodation_cost * ACCOMODATION_BONUS * trip_length)
else:
    trip_cost = start_point_cost + destination_cost + (accomodation_cost * trip_length)
    
    
#print costs    
print("\nyour trip costs : $", trip_cost, "total (including GST)")
print ("\n\nCOST BREAKDOWN \n(all costs include GST)")

#adds start point costs 
if start_point != 0:
    print("\nthe connecting flight from", start_point_list[start_point][0], "to Auckland cost $", start_point_cost)
print("\nyour flight to", destination_list[destination][0], "from Auckland cost $", destination_cost)
print("\nyour accomodation cost $", accomodation_cost, "per night")

#adds 2+ nights cost reduction
if trip_length > 2:
    print ("\nyour accomodation cost ", ACCOMODATION_BONUS * 100, "% of the original cost because you stayed more than 2 nights")
    print ("this meant your accomodation cost $", accomodation_cost, "x", ACCOMODATION_BONUS, "x trip_length (", trip_length,"nights ) = $", trip_cost)
else:
    print ("\nyour accomodation cost $", accomodation_cost, "x your trip length (", trip_length,"nights ) = $", trip_cost)
#print total again
print("\nyour trip costs : $", trip_cost, "total (including GST)")