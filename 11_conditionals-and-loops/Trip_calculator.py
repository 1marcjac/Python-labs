distance = int (input('How many kilometers do you have to drive to reach your destination?\n'))
feul_efficiency = int (input('What is the average miles per gallon for vehicle on the highway?\n'))
Cost_of_feul = float (input('How much is a liter of feul in your area?\n'))
total_cost = distance * feul_efficiency * Cost_of_feul

print (F'The total cost of your trip is: $ {total_cost:.2f}')