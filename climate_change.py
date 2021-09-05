import time

#Set up variables
global score, current_question

score = 0
current_question = 0

#Questions, Answers, & Additional Facts

questions = ['There’s more carbon dioxide in our atmosphere than at any time in human history.',
             'The warmest 5 year period since 1850 was 1990-1995.',
             '20 of the warmest years on record have been in the last 22 years.',
             'The United States contributes only 20% of the greenhouse gasses that are causing climate change.',
             'Climate Change has a major affect on Coral Reef development.',
             'Coal fired power plans account for the largest contrubution to greenhouse gasses from the US.',
             'The amount of emmissions from US cars and trucks is equil to the amount of emmissions from all sources in the UK.',
             'Air conditions and heating elements consume 30% of electricity in America.',
             'Of the three major greenhouse gasses, carbon dioxide is the most dangerous. ',
             'More than half a million deaths per year can be contributed to factors related to climate change. ']
answers = ['T',
           'F',
           'T',
           'F',
           'T',
           'T',
           'F',
           'F',
           'F',
           'T']

statements = ['The last time Earth’s atmosphere contained this much CO2 was more than three million years ago, when sea levels were several metres higher and trees grew at the South Pole.',
              'According to the UN IPPC Report, 2016-2020 is the warmest 5-year period since 1850.',
              'The world’s five warmest years have all occurred since 2016, with nine of the 10 warmest years occurring since 2005',
              'The US actually contributes 22% of global greenhouse gasses even though it only account for just under 5% of the global population.',
              'Between 2014 and 2017, the bleaching of the Northern Great Barrier Reef, combined with the impacts of cyclones, killed around 50% of its corals.',
              'In 2004, an estimated 350 new coal-fired power plants were expected to be online by 2012 in the US, India and China. Nearly 100 of these are expected to be built in the US.',
              'Cars and light trucks account for 40% of US oil use and contribute about as much to climate change as the entire Japanese economy—the world’s fourth-largest carbon emitter.',
              'Air conditions and heating elements consume almost 50% of the total electricity consumed in America.',
              'Other gases like methane and nitrous oxide are far more dangerous than carbon dioxide alone.',
              '95% of these deaths take place in developing countries.']

resources =['https://www.conserve-energy-future.com/various-climate-change-facts-php.php',
            'https://www.wired.co.uk/article/climate-change-facts-2019',
            'https://climate.nasa.gov/evidence/',
            'https://www.conservation.org/stories/11-climate-change-facts-you-need-to-know']

#Start of Game Instructions
def game_start():
    print('Welcome to the Climate Change Trivia Game!')
    time.sleep(2)
    print('The objective of this game is to get as many questions correct as possible.')
    time.sleep(2)
    print('To answer the questions, enter T for True or F for False when prompted.')
    time.sleep(2)
    print('Shall We Play a Game?')
    time.sleep(2)

#Question asking function
def ask_question():
    #Include gloabl Variables
    global score, current_question
    #While Loop to ask all questions in array
    while current_question < len(questions):
        print('Question ', current_question+1,': ', questions[current_question])
        time.sleep(2)
        answer = input('Enter T for True and F for False')
        time.sleep(2)
        #If Statement to check answer and adjust score if necessary
        if answer == answers[current_question]:
            score = score +1
            print('Correct! Your current score is', score,'.')
        else:
            print('Incorrect! Your current score is', score,'.')
        time.sleep(2)
        print(statements[current_question])
        time.sleep(2)
        #Increment current question for loop
        current_question = current_question +1

#end of game function
def end_game():
    print('Thanks for playing')
    time.sleep(2)
    print('Your Final Score is ', score, 'out of ', len(questions),'.')
    time.sleep(2)
    print('To Learn More about Climate Change, please visit the following resources:')
    time.sleep(1)
    for i in range(len(resources)):
        print(resources[i])

#Game Runtime Execution
game_start()
ask_question()
end_game()

    

