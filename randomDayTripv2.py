# #Day trip generator 
# (5 points): As a developer, I want to make at least three commits with descriptive messages.

# (5 points): As a developer, I want to store my destinations, restaurants, mode of transportations, and entertainments in their own separate lists.

# (5 points): As a user, I want a destination to be randomly selected for my day trip.  

# (5 points): As a user, I want a restaurant to be randomly selected for my day trip. 

# (5 points): As a user, I want a mode of transportation to be randomly selected for my day trip. 

# (5 points): As a user, I want a form of entertainment to be randomly selected for my day trip. 

# (15 points): As a user, I want to be able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things. 

# (10 points): As a user, I want to be able to confirm that my day trip is “complete” once I like all of the random selections. 

# (10 points): As a user, I want to display my completed trip in the console. 

# (5 points): As a developer, I want all of my functions to have a Single Responsibility. Remember, each function should do just one thing

#randomly select destination. have associated lists of restaurants, transportation, and entertainment for each trip. 
#have at least four in each list 

#first code review -- specifics unnecessary, still going to keep
#-- simplify repeated patterns. there are while loop validations all over the place. 
# use comments to explain the why of the code block 
# dictionaries are a better way to implement this code. consider refactoring but get this version finished first. 


import random


guide = {
    'cities': ['philadelphia', 'chicago', 'denver', 'nyc', 'austin', 'seattle'],
    'restaurants': ['steakhouse', 'sushi', 'fast food', 'pizza', 'five star restaurant'],
    'entertainment': ['live music', 'city tour', 'hike', 'museum'],
    'transportation': ['rental car', 'public transportation','uber', 'bike rental']
}


def while_validation(ans,list):
    new_choice = random.choice(list)
    while(ans != 'y'):
        new_choice = random.choice(list)
        ans = input(f'What about {new_choice}? y/n: ')
    print('great. let\'s move on.')
    return new_choice


def destination():
    user_dest = random.choice(guide['cities'])
    ans_dest = input(f'your destination is {user_dest}. Is this acceptable? y/n: ')
    user_dest = while_validation(ans_dest,guide['cities'])
    return user_dest

def transpo():
    user_transpo = random.choice(guide['transportation'])
    ans_transpo = input(f'your transportation is {user_transpo}. Is this acceptable? y/n: ')
    user_transpo = while_validation(ans_transpo,guide['transportation'])
    return user_transpo

def entertainment():
    user_ent = random.choice(guide['entertainment'])
    ans_ent = input(f'your entertainment is {user_ent}. Is this acceptable? y/n: ')
    user_transpo = while_validation(ans_ent,guide['entertainment'])
    return user_ent

def restaurant():
    user_rest = random.choice(guide['restaurants'])
    ans_rest = input(f'your restaurant is {user_rest}. Is this acceptable? y/n: ')
    user_rest = while_validation(ans_rest,guide['restaurants'])
    return user_rest

def first_selection():
    first_dest = destination()
    first_transpo = transpo()
    first_ent = entertainment()
    first_rest = restaurant()
    first_list = [first_dest,first_ent, first_rest, first_transpo]
    validate = input(f'Here is your itinerary \n \
        destination: {first_dest} \n \
        entertainment: {first_ent} \n \
        restaurant: {first_rest} \n \
        transportation: {first_transpo} \n \
        is there anything you want to change? \
        If so, select cities, transporation, entertainment, and/or restaurant separated by commas. If there are no changes, enter none: ').split(',')
    return first_list, validate

def random_trip_generator():
    current,changes = first_selection()
    if 'cities' in changes:
        current[0] = destination()
    elif 'entertainment' in changes:
        current[1] = entertainment()
    elif 'restaurant' in changes:
        current[2] = restaurant()
    elif 'transporation' in changes:
        current[3] = transpo()
    return print(f'Here is your final itinerary \n \
        destination: {current[0]} \n \
        entertainment: {current[1]} \n \
        restaurant: {current[2]} \n \
        transportation: {current[3]}' )

        
random_trip_generator() 
    


