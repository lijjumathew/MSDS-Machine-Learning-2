import numpy as np

people = {
    'Sundar': {
        'willingness to travel': 3,
        'desire for new experience': 4,
        'cost': 3,
        'vegetarian': 1,
        'hipster points': 1,
        'mexican food': 1,
        'indian food': 5
    },
    'John': {
        'willingness to travel': 1,
        'desire for new experience': 2,
        'cost': 4,
        'vegetarian': 1,
        'hipster points': 1,
        'mexican food': 5,
        'indian food': 2
    },
    'Juan': {
        'willingness to travel': 4,
        'desire for new experience': 3,
        'cost': 4,
        'vegetarian': 2,
        'hipster points': 3,
        'mexican food': 5,
        'indian food': 1
    },
    'Matt': {
        'willingness to travel': 5,
        'desire for new experience': 4,
        'cost': 3,
        'vegetarian': 3,
        'hipster points': 5,
        'mexican food': 2,
        'indian food': 3
    },
    'Satya': {
        'willingness to travel': 3,
        'desire for new experience': 4,
        'cost': 1,
        'vegetarian': 3,
        'hipster points': 2,
        'mexican food': 3,
        'indian food': 5
    },
    'Jose': {
        'willingness to travel': 5,
        'desire for new experience': 5,
        'cost': 3,
        'vegetarian': 1,
        'hipster points': 3,
        'mexican food': 4,
        'indian food': 4
    },
    'Sanjay': {
        'willingness to travel': 4,
        'desire for new experience': 5,
        'cost': 2,
        'vegetarian': 4,
        'hipster points': 4,
        'mexican food': 1,
        'indian food': 5
    },
    'Jones': {
        'willingness to travel': 1,
        'desire for new experience': 2,
        'cost': 2,
        'vegetarian': 3,
        'hipster points': 5,
        'mexican food': 4,
        'indian food': 2
    },
    'Jay': {
        'willingness to travel': 3,
        'desire for new experience': 4,
        'cost': 1,
        'vegetarian': 3,
        'hipster points': 2,
        'mexican food': 1,
        'indian food': 5
    },
    'Luis': {
        'willingness to travel': 1,
        'desire for new experience': 3,
        'cost': 5,
        'vegetarian': 1,
        'hipster points': 3,
        'mexican food': 5,
        'indian food': 2
    }
}
people_cols = [
    'willingness to travel',
    'desire for new experience',
    'cost',
    'vegetarian',
    'hipster points',
    'mexican food',
    'indian food'
]

resturants = {
    'Purple Cafe': {
        'distance': 3,
        'novelty': 3,
        'cost': 2,
        'cusine': 'hipster points'
    },
    "Torchys Tacos": {
        'distance': 4,
        'novelty': 3,
        'cost': 1,
        'cusine': 'mexican food'
    },
    "Sarvana Bhavan": {
        'distance': 3,
        'novelty': 2,
        'cost': 2,
        'cusine': 'indian food'
    },
    "Mi Cocina": {
        'distance': 2,
        'novelty': 1,
        'cost': 4,
        'cusine': 'mexican food'
    },
    "Biryani Place": {
        'distance': 4,
        'novelty': 5,
        'cost': 2,
        'cusine': 'indian food'
    },
    "Veggie Grill": {
        'distance': 5,
        'novelty': 4,
        'cost': 4,
        'cusine': 'vegetarian'
    },
    "Outlier": {
        'distance': 3,
        'novelty': 5,
        'cost': 1,
        'cusine': 'hipster points'
    },
    "Bombay Choptsticks": {
        'distance': 2,
        'novelty': 2,
        'cost': 4,
        'cusine': 'indian food'
    },
    "Mias": {
        'distance': 1,
        'novelty': 4,
        'cost': 4,
        'cusine': 'mexican food'
    },
    "Adda": {
        'distance': 2,
        'novelty': 1,
        'cost': 5,
        'cusine': 'indian food'
    },
    "Evergreens": {
        'distance': 3,
        'novelty': 1,
        'cost': 4,
        'cusine': 'vegetarian'
    }
}

restaurant_cols = [
    'distance',
    'novelty',
    'cost',
    'cusine: vegetarian',
    'cusine: hipster points',
    'cusine: mexican food',
    'cusine: indian food'
]

people_mtrx = None
restaurant_mtrx = None
resturant_rows = None


def transform_people_matrix():
    global people_mtrx
    global people_cols
    lst_to_mtrx = []
    people_rows = []

    for person, description in people.items():
        people_rows.append(person)
        lst_to_mtrx.append([description[cat] for cat in people_cols])
    people_mtrx = np.matrix(lst_to_mtrx)


def transform_restaurant_matrix():
    global restaurant_mtrx
    global restaurant_cols
    global resturant_rows
    lst_to_mtrx_r = []
    resturant_rows = []

    for restaurant, description in resturants.items():
        resturant_rows.append(restaurant)
        row = [description[cat] for cat in restaurant_cols[:3]]
        for cat in restaurant_cols[3:]:
            if cat.split(':')[-1].strip() != description['cusine']:
                row.append(0)
            else:
                row.append(5)
        lst_to_mtrx_r.append(row)
    restaurant_mtrx = np.matrix(lst_to_mtrx_r)


def find_restaurant_preferences(name):
    person = people[name]
    p = np.matrix([person[col] for col in people_cols])
    prefs = np.dot(p, restaurant_mtrx.T).tolist()[0]
    return {k: v for k, v in zip(resturant_rows, prefs)}


def calculate_all_user_prefs():
    return np.dot(people_mtrx, restaurant_mtrx.T)


def _vals_to_ranks(lst):
    n_vals = []
    preferences = {v: r for r, v in enumerate(sorted(lst))}
    for val in lst:
        n_vals.append(preferences[val])
    return n_vals


def output_restaurant_scores():
    M_usr_x_rest = calculate_all_user_prefs()
    scores = [M_usr_x_rest[:, n].sum() for n in range(M_usr_x_rest.shape[1])]
    ranks = _vals_to_ranks(scores)
    return {rsnt: score for rsnt, score in zip(resturant_rows, ranks)}


def non_parametric_restaurant_scores():
    M_usr_x_rest = calculate_all_user_prefs()
    M_usr_x_rest_rank = \
        np.matrix([_vals_to_ranks(M_usr_x_rest[row].tolist()[0]) for row in range(M_usr_x_rest.shape[0])])
    scores = [M_usr_x_rest_rank[:, n].sum() for n in range(M_usr_x_rest_rank.shape[1])]
    ranks = _vals_to_ranks(scores)
    return {rsnt: score for rsnt, score in zip(resturant_rows, ranks)}


def find_problematic_users():
    user_deltas = {}
    for person, preferences in people.items():
        scores = np.array(list(preferences.values()))
        dist_from_3 = np.abs(scores - 3)
        user_deltas[person] = dist_from_3.mean()
    return user_deltas


def disatistifaction_score1():
    M_usr_x_rest = calculate_all_user_prefs()
    M_usr_x_rest_rank = \
        np.matrix([_vals_to_ranks(M_usr_x_rest[row].tolist()[0]) for row in range(M_usr_x_rest.shape[0])])
    less_then_4 = M_usr_x_rest_rank < 4
    scores = [less_then_4[:, n].sum() for n in range(M_usr_x_rest_rank.shape[1])]
    return {rsnt: score for rsnt, score in zip(resturant_rows, scores)}


def disatistifaction_score2():
    M_usr_x_rest = calculate_all_user_prefs()
    meh_score = np.dot(
        np.ones(people_mtrx.size).reshape(*people_mtrx.shape) * 3, restaurant_mtrx.T)
    shifted = M_usr_x_rest - meh_score
    shifted[shifted > 0] = 0
    scores = [shifted[:, n].sum() for n in range(shifted.shape[1])]
    return {rsnt: score for rsnt, score in zip(resturant_rows, scores)}


def boss_is_paying():
    '''
    Since the boss is paying, we will remove cost from the equation by setting it to 0 for everyone.
    '''
    rests = restaurant_mtrx[:, [0, 1, 3, 4, 5, 6]]
    ppl = people_mtrx[:, [0, 1, 3, 4, 5, 6]]
    M_usr_x_rest_nocost = np.dot(ppl, rests.T)
    scores = [M_usr_x_rest_nocost[:, n].sum() for n in range(M_usr_x_rest_nocost.shape[1])]
    ranks = _vals_to_ranks(scores)
    return {rsnt: score for rsnt, score in zip(resturant_rows, ranks)}


if __name__ == '__main__':
    # Problem 1 - Transform the user data into a matrix(M_people). Keep track of column and row ids.   
    transform_people_matrix()

    # Problem 2 - Transform the restaurant data into a matrix(M_resturants) use the same column index.
    transform_restaurant_matrix()
    # print(restaurant_mtrx)

    # Problem 3 - The most imporant idea in this project is the idea of a linear combination.
    # Informally describe what a linear combination is  and how it will relate to our resturant matrix.
    # Answer 3 - Linear combination is a concept in linear algebra where you multiple 2 vectors together (element wise)
    # to obtain a new vector and then sum up the elements of this new vector to get an aggregate number.
    # The way it applies to our problem is that we have a rating for each resturant in particular categories and
    # each person has also given their preference for those same categories. Hence by multiplying the preferences and
    # ratings appropriately and summing them up, we can get an aggregate score for that person for a particular
    # resturant. This is especially helpful since now we dont have to have every person rate every resturant
    # individually. All they have to do is provide their preferences and based on how the resturant scores on those
    # preferences, we can obtain an aggretae score easily.

    # Problem 4 - Choose a person and compute(using a linear combination) the top restaurant for them.
    # What does each entry in the resulting vector represent.
    # Answer 4 - This method gives a users preferences for each of the restaurants in the survey.
    for rest, score in find_restaurant_preferences('John').items():
        print('\t', rest, ": ", score)

    # Problem 4 - Next compute a new matrix (M_usr_x_rest  i.e. an user by restaurant) from all people.
    # What does the a_ij matrix represent?
    # Answer 4 - The output of this matrix represents the user score for each user on each restaurant.
    print("The group scores are:")
    for rest, score in output_restaurant_scores().items():
        print('\t', rest, ": ", score)

    # Problem 5 -Sum all columns in M_usr_x_rest to get optimal restaurant for all users.
    # What do the entry’s represent?
    # Answer 5 - The sum of the columns in the M_usr_x_rest matrix represent the relative score of each restaurant
    # for the whole group (the restaurant with the highest score will be the most prefered to the group)
    calculate_all_user_prefs()

    # Problem 6 - Now convert each row in the M_usr_x_rest into a ranking for each user and call it M_usr_x_rest_rank.
    # Do the same as above to generate the optimal restaurant choice.
    print("The composite group scores are:")
    for rest, score in non_parametric_restaurant_scores().items():
        print('\t', rest, ": ", score)

    # Problem 7 - Why is there a difference between the two?  What problem arrives?
    # What does represent in the real world?How should you preprocess your data to remove this problem.
    # Answer 7 - Summing all of the scores using method 1 allows one person's preferences to dominate the
    # overall score because that one person may strongly favor a particular resturant.
    # By making the scores non-parametric (adding the ranks of each resturant instead of their raw scores) by method 2,
    # Each participant's rank vote is counted equally.  The result in my survey is that the same places are chosen
    # for first and last by the group, but the other ranks are jumbled by using this diffirent method.
    # Both methods may have their value in the real world, using method 2 is more likley to result in the group
    # going to a place that most people like; while a single person could feel very strongly against it.
    # Method 1 is more likley to result in the group going to a place which most participants do not have
    # a strong opinion of; while a single person may have a very strong preference toward that place.
    # In other words, using a non-parametric system makes it harder for a single person to manipulate the
    # system toward a specific preference. It could be possible to reduce the impact of agressive users by
    # applying weights to the preferences matrix.

    # Problem 8 - Find  user profiles that are problematic, explain why?
    print('Each participant has the following leverage:')
    for person, score in find_problematic_users().items():
        print("\t", person, ':', score)

    # Problem 9 - Think of two metrics to compute the disatistifaction with the group.
    print('Using the rank method, the disatisfaction score for each restaurant is:')
    for rest, score in disatistifaction_score1().items():
        print("\t", rest, ':', score)
    print('Using the points method, the disatisfaction score for each restaurant is:')
    for rest, score in disatistifaction_score2().items():
        print("\t", rest, ':', score)

    # Problem 10 - Should you split in two groups today?
    # Answer 10 - These two methods give very diffirent values, but in both cases, the most highly ranked resturant
    # of both methods is gievn a disastisfaction index.  Using the numeric index, the most highly ranked restaurant ,
    # gets the highest disastisfaction index. Since this method takes into effect how much a person disslikes a place,
    # those that do not want to go to Pink Door, seem to very much be against the idea.
    # This lends some credibility to the arguement that lunch should be split into multipule groups.

    # Problem 11 - Ok. Now you just found out the boss is paying for the meal. How should you adjust.
    # Now what is best restaurant?
    print('Checking on restaurant ranks when the boss is paying:')
    for rest, score in boss_is_paying().items():
        print("\t", rest, ':', score)

    # Problem 12 - Tommorow you visit another team. You have the same restaurants and they told you their optimal
    # ordering for restaurants.  Can you find their weight matrix?
    # Answer 12 - No, I cant find their weight matrix just based on their preferences.  This is because unrecoverable
    # information is lost when converting the output from the restaurant scores matrix to group ranks, but i could
    # find the weight matrix if I was given each participant's score for each resturaunt.  This is because matrix
    # multiplication is reversable.
