#madlibs 
#10/2/2020



theInput = []
ask =["Random Last Name", "time of day", "adjective", "present verb that ends in ing", "body part", "random number", "noun", "verb (base form)", "liquid", "amount of time", "anything", "pet", "plural noun", "your name"]



counter = 0

for counter in range(0, len(ask)):
   userInput = input(ask[counter] + ": ")
   theInput.append(userInput)
   counter = counter+1
   

story = ['Dear Dr.'," I cannot make it to class this ", ". I am very ", " and cannot stop ", " my ", ". I have a fever of ", " degrees and the doctor ordered me to stay in", " and ", " lots of ", ". Also, can I have a " ," extension on the essay about "," ? My "," ate it and now I have to start all over Best ," " ", "", ""]

for counter in range(0, len(theInput)):
   print (story[counter], theInput[counter], end='')
