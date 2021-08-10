import time
print('Welcome to Camp! Where do you want to go today?')
area = input('Pick from the following areas: Waterfront (W), Climbing (C), or Handicraft (H)')
while not (area == 'W' or area == 'C' or area == 'H'):
    area = input('You didn\'t select a valid input. Enter W, C, or H.')
if area == 'W':
    print('It is a hot day out.')
    time.sleep(3)
    print('Enjoy the lake, but make sure you put on sunscreen and stay with a buddy.')
elif area == 'C':
    print('Welcome to our Climbing wall...')
    time.sleep(3)
    print('Don\'t look down it\'s really tall')
elif area == 'H':
    print('There are lots of crafts to make something with.')
    time.sleep(3)
    print('You should make a popsicle boat ')
time.sleep(3)
choice = input('What do you want to do next? Drink Water (W) or Take a quick Nap (N)')
while not (choice == 'W' or choice == 'N'):
    choice = input('You didn\'t select a valid input. Enter W, or N.')
if choice == 'W':
    print('You selected the right choice.')
    time.sleep(3)
    print('Drinking water keeps you hydrated!')
    time.sleep(3)
    print('Enjoy the rest of your day at camp!')
elif choice == 'N':
    print('You should have had water.')
    time.sleep(3)
    print('Now you are dehydrated and have a headache!')
    time.sleep(3)
    print('Enjoy your trip to the nurse.')
time.sleep(3)
lunch = input('What do you want to eat for lunch today? Tacos (T) or a PB&J (P)?')
while not (lunch == 'T' or lunch == 'P'):
    lunch = input('You didn\'t select a valid input. Enter W, C, or H.')
if lunch == 'T':
    print('Tacos are always a good choice.')
    time.sleep(3)
    print('Especially if it is Taco Tuesday!')
elif lunch == 'P':
    print('A classic camp lunch treat.')
    time.sleep(3)
    print('Enjoy!')
print('Enjoy the rest of your day at camp!')
