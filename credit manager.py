#list pratice
#storing names and ncea credits
#11/2/2020

#you were up to edinting name

#list of students 
students = [["sophia rofe", 14], ["fergus smith", 14]]

#prints all students
def print_students():
    print('these are our students: ')
    for i in range(0, len(students)):
        print(i+1, students[i][0]) 
   

while True:
    #tells user options 
    print ("\nthis program allows you to\n",
           "1) view students\n", 
           "2) view specific person\n", 
           "3) add a student\n", 
           "4) delete a student\n",
           "5) change student details\n",
           "press a number to select your option")
    
    user_input = int(input(">>>: "))
    
    if user_input == 1:
        print_students()
        
    elif user_input == 2:
        #prints all students
        print_students()
        #asks if user wants specific person
        display_student = int(input("type the number of the student you want to display: "))
        if display_student <= len(students)+1:
            print (students[display_student-1])
         
            
            
            
    elif user_input == 3:    
        #add a student 
        new_student = input("type the name of the student you want to add: ")
        new_score = int(input("type the score of the new student: "))
        students.append([new_student, new_score])
        #prints all students
        print_students()
        
        
        
    elif user_input == 4:
        #prints all students
        print_students()        
        #delete a student
        begone_student = int(input("type the number of the student you want to delete: "))
        del students[begone_student-1]
        #prints all students
        print_students()
         
    elif user_input == 5: 
        #choose to change name or score
        print(" 1)change student name", 
              "\n 2)change student score")
        user_input2 = input(">>>: ")
        #change name
        if user_input2 == 1:
            #prints all students
            print_students()     
            #change student details
            change_student = int(input("type the number of the student you want to edit: "))
            new_name = input("enter updated name: ")
            students[change_student-1][0] = new_name
        #change score
        elif user_input2 == 2:
            #prints all students
            print_students()     
            #change student details
            change_student = int(input("type the number of the student you want to edit: "))
            new_score = input("enter updated name: ")
            students[change_student-1][1] = new_score          
        #prints all students
        print_students()        

    else:
        print ("didnt get that, try again")