# Set Camp Costs
cost_campers = 435
cost_adults = 100
cost_photos = 13
# Greeting
print('Hello and welcome to camp! I am your check-in chatbot.')
name = input('What is your name?')
print('Hello', name, '!')
# Camper Calculation
campers = input('How many campers have you brought this week?')
ncampers = int(campers)
print('Your cost for campers this year is $', ncampers * cost_campers)
# Adult Calculation
adults = input('How many adult leaders will be here this week?')
nadults = int(adults)
print('Your cost for adults this year is $', nadults * cost_adults)
# Total Camp Fee Calculation
print('Your total camper cost this season is $', (ncampers * cost_campers) + (nadults * cost_adults))
# Photo Order
photos = input('How many camp photos would you like to purchase?')
nphotos = int(photos)
print('Your cost for photos this year is $', nphotos * cost_photos)
print('Thanks for coming to camp this year', name)
