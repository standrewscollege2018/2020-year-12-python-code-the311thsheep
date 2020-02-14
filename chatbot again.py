#chatbot 10/2/2020

import random


def madlibs():
    import madlibs
    

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']

affirmitive = ["yes", "yeah", "y", "sounds good"]

question = ['How are you?','How are you doing?', 'hows it going']


responses = ['Okay',"I'm fine"]


a=True
counter= 0



while a == True:
    counter = counter+1
    random_greeting = random.choice(greetings)
    random_response = random.choice(responses)
    userInput = input(">>> ")
    
    
    if userInput in greetings:
        print(random_greeting)
    elif userInput in question:
        print(random_response)
    elif userInput == "end":
        print ("bye!")
        a = False
    else:
        print("I did not understand what you said, do you want to play madlibs?")
        print (counter)
        if userInput in affirmitive:
            print (counter)
            madlibs()
      