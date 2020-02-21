#bookstore
#18/2/2020

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

#prints all titles
def print_titles(index = None):
    print("These are our current titles")
    #prints all of list 
    if index == None:
        for i in range (0, len(booklist)):
            print (i+1, booklist[i])
    #prints specific index
    else:
        for i in range (0, len(booklist)):
            print (i+1, booklist[i][index])        
        

#the list of books, their authors, and their prices
# booklist [book][author][price]
booklist = [["Divergent", "Veronica Roth", 20], ["Fairest", "Marissa Meyer", 25], ["Harrry Potter and the Chamber of Secrets", "J.K Rowling", 30]]


while True:
    #tells user options of program
    user_input = get_correct_input("\nthis program lets you: \n 1) print all titles \n 2) view specific title \n 3) add book titles to a list \n 4) edit existing titles \n 5) delete titles \n 6) quit the program. \n >>>: ", 6)
    
    #prints all titles 
    if user_input == 0:
        print_titles(0)
    
    
    #view specifc book
    elif user_input == 1:
        print_titles(0)
        #ask what book they want to view
        selected_book = get_correct_input("enter the number of the book you want to view: ", len(booklist))
        print (booklist[selected_book])
        
    #add title to the list     
    elif user_input == 2:
        new_title = input("enter the title of the new book: ")
        new_author = input("enter the author of the new books name: ")
        new_price = get_correct_input("enter the price of the new book: ")
        booklist.append([new_title, new_author, new_price+1])
        print (booklist[-1])
            
    #edit title
    elif user_input == 3:
        print_titles()
        #choose book to edit
        broken_book = get_correct_input("enter the number of the book you want to edit: " ,len(booklist))
        edit_what = get_correct_input("do you want to \n 1) change book name \n 2) change book author \n 3) change book price \n >>>: ", 3)
        #change book name 
        if edit_what == 0:
            new_title = input("enter the new title of the book: ")
            booklist[broken_book][0] = new_title
        #change book author 
        elif edit_what == 1:
            new_author = input("enter the new author of the book: ")
            booklist[broken_book][1] = new_author
        #change book price
        elif edit_what == 2:
            new_price = get_correct_input("enter the new price of the book: ")
            booklist[broken_book][2] = new_price
        print (booklist[broken_book])
    
    #delete
    elif user_input == 4:   
        print_titles(0)
        begone_book = get_correct_input("enter the number of the book you want to delete: ", len(booklist))
        del booklist[begone_book]
        print_titles(0)
        
    #quit
    elif user_input == 5:         
        print ("bye")
        break