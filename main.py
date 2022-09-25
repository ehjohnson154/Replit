#Mathbot. Does simple math functions based on user input, continues until program is asked to quit

print("Welcome to Math helper! Type foo for help!")

x = [""] #sets up x variable with empty string

while x[0].lower() != "quit": #Loops program until user types quit in first position
  
  stuff = input("SuperMathyBot > ") #User input here

  x = stuff.split() #splits user input, can handle greater inputs than expected but does not deal with them.

  #if statements for all math functions
  if x[0].lower() == "add":
    sum = round(float(x[1]) + float(x[2]), 2)
    print(sum)
  
  elif x[0].lower() == "sub":
    sum = round(float(x[1]) - float(x[2]), 2)
    print(sum)
  
  elif x[0].lower() == "div":
    if x[2] == "0":
      print("Can't divide by zero.") #divide by zero check
    else:
      sum = round(float(x[1]) / float(x[2]), 2)
      print(sum)

  elif x[0].lower() == "mul":
      sum = round(float(x[1]) * float(x[2]), 2)
      print(sum)

  #helper statement
  elif x[0].lower() == "foo":
    print("usage: add|sub|mul|div v0 v1 \n quit")

  #Prints message on shutdown
  elif x[0].lower() == "quit":
    print("Program shutting down...")
     
  else: #else statement to handle unexpected inputs
    print("Invalid input, try again please!)")