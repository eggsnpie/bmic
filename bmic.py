##This programs allows the user to calculate their BMI to the tenth decimal place.

#Requests input from the user as to what measuring system they use.
measure_weight = input('Do you measure weight in pounds or kilos? ')

#Sets another condition for if the user input is a 'pounds' string after being lowercased, it will execute the code indented below.
if measure_weight.lower() == 'pounds':
    
    #Prints to the user that they have selected pounds as the weight measuring system.
    print('You have selected pounds.')
    
    #Requests input from the user for what their weight is, excluding the word pounds or lbs.
    weight = input('What is your weight? Please exclude the word pounds or lbs. ')

    #Requests input from the user for what their height is in inches. 
    height_inches = input('What is your height in inches? ')

    #Since the user selected the US measuring systems, the next three variables help to calculate the user's BMI based on the data they provided.
    bmi_inches_formula_step_1 = float(weight) / float(height_inches) **2
    inches_to_meters = 703.0
    bmi_inches_formula_step_2 = bmi_inches_formula_step_1 * inches_to_meters

    #Prints to the user what their BMI is rounded to the tenth decimal.
    print('Your BMI is ' + str(round(bmi_inches_formula_step_2, 1)))
#Sets another condition for if the user input is a 'kilos' string after being lowercased, it will execute the code indented below.
elif measure_weight.lower() == 'kilos':
    print('You have selected kilos.')
    weight_kilos = input('What is your weight? Please exclude the word kilos or kgs. ')
    height_meters = input('What is your height in meters? ')
    
    #The BMI formula is differently coded here because the forumula itself is different based on whether pounds or kilos are used.
    #So, our program accounts for this and provides an equally accurate result for the metric system.
    bmi_formula_kilos = float(weight_kilos) / float(height_meters) **2
    print('Your BMI is ' + str(round(bmi_formula_kilos, 1)))

#Sets a final condition for any other input provided for the measure_weight variable.
else:
    #Tells the user their input was invalid and that they should try again.
    print('Invalid Input. Try Again.')

    #Terminates the program.
    exit()
        
        


