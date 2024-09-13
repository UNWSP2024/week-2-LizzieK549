"""Program #2: Average Age Write a program that inputs the ages of five friends,
calculates the average age (as a decimal) and displays the average age to the user.
You can either do this via a loop (which we'll cover later in the class) or you can have 6 variables, one for each of the individual ages and one for the average age."""

def average_age():
    # Get User Input
    #The following are names and scores
    todd= 17
    franny= 16
    jay = 19
    tammy = 19
    suzie = 16

    # Sum ages
    sumAge= (todd + franny+jay+tammy+suzie)
    print("The sum of the ages are", sumAge)

    # Average the ages
    averageAge = sumAge/ 5

    # Print the results
    print("The average age of the friends:", averageAge)
# Line which calls the above function.
average_age()