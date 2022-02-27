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
    'city': ['philadelphia', 'chicago', 'denver', 'nyc', 'austin', 'seattle'],
    'restaurants': ['steakhouse', 'sushi', 'fast food', 'pizza', 'five star restaurant'],
    'entertainment': ['live music', 'city tour', 'hike', 'museum'],
    'transportation': ['rental car', 'public transportation','uber', 'bike rental']
}

selection = {}

def while_validation(ans,list):
    if ans == 'y':
        return None
    else:
        while(ans != 'y'):
         new_choice = random.choice(list)
         ans = input(f'What about {new_choice}? y/n: ')
        return new_choice

def if_validation(original,change):
    if change == None:
        return original 
    else: 
        original = change
        return original

def destination():
    rand_dest = random.choice(guide['city'])
    user_choice_dest = input(f'your destination is {rand_dest}. Is this acceptable? y/n: ')
    change = while_validation(user_choice_dest,guide['city'])
    dest_selection = if_validation(rand_dest,change)
    selection['city'] = dest_selection
    return dest_selection

def transpo():
    rand_transpo = random.choice(guide['transportation'])
    user_choice_transpo = input(f'your transportation is {rand_transpo}. Is this acceptable? y/n: ')
    change = while_validation(user_choice_transpo,guide['transportation'])
    transpo_selection = if_validation(rand_transpo,change)
    selection['transportation'] = transpo_selection
    return transpo_selection

def entertainment():
    rand_ent = random.choice(guide['entertainment'])
    user_choice_ent = input(f'your entertainment is {rand_ent}. Is this acceptable? y/n: ')
    change = while_validation(user_choice_ent,guide['entertainment'])
    ent_selection = if_validation(rand_ent,change)
    selection['entertainment'] = ent_selection
    return ent_selection

def restaurant():
    rand_rest = random.choice(guide['restaurants'])
    user_choice_rest = input(f'your restaurant is {rand_rest}. Is this acceptable? y/n: ')
    change = while_validation(user_choice_rest,guide['restaurants'])
    rest_selection = if_validation(rand_rest,change)
    selection['restaurant'] = rest_selection
    return rest_selection

functions = {
    'city' : destination,
    'restaurant' : restaurant,
    'entertainment' : entertainment,
    'transportation' : transpo,
}


def first_selection ():
    destination()
    entertainment()
    transpo()
    restaurant()
    changes = input(f'Your current selection is\
        \n{selection}.\nIs there anything you would like to change?\
        \nSelect city, entertainment, transportation, or restaurant separated by a single comma.\
        \nIf you are happy with you selection, select agree: ').split(',')
    return changes


def random_trip_generator():
    changes = first_selection()
    if len(changes) == 1 and 'agree' in changes:
        print(f'Great, enjoy the following trip:\n{selection}')
    else:
        for i in range(0,len(changes)):
            selection[changes[i]] = functions[changes[i]]()
        print(f'here is your updated itinerary:\n{selection}')

random_trip_generator()