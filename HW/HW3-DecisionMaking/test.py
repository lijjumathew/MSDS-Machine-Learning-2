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
        'average rating': 4,
        'cusine': 'hipster points'
    },
    "Torchys Tacos": {
        'distance': 4,
        'novelty': 3,
        'cost': 1,
        'average rating': 4,
        'cusine': 'mexican food'
    },
    "Sarvana Bhavan": {
        'distance': 3,
        'novelty': 2,
        'cost': 2,
        'average rating': 4,
        'cusine': 'indian food'
    },
    "Mi Cocina": {
        'distance': 2,
        'novelty': 1,
        'cost': 4,
        'average rating': 3,
        'cusine': 'mexican food'
    },
    "Biryani Place": {
        'distance': 4,
        'novelty': 5,
        'cost': 2,
        'average rating': 4,
        'cusine': 'indian food'
    },
    "Veggie Grill": {
        'distance': 3,
        'novelty': 1,
        'cost': 4,
        'average rating': 3,
        'cusine': 'vegetarian'
    },
    "Outlier": {
        'distance': 3,
        'novelty': 5,
        'cost': 1,
        'average rating': 2,
        'cusine': 'hipster points'
    },
    "Bombay Choptsticks": {
        'distance': 2,
        'novelty': 2,
        'cost': 4,
        'average rating': 4,
        'cusine': 'indian food'
    },
    "Mias": {
        'distance': 1,
        'novelty': 4,
        'cost': 4,
        'average rating': 5,
        'cusine': 'mexican food'
    },
    "Adda": {
        'distance': 2,
        'novelty': 1,
        'cost': 5,
        'average rating': 4,
        'cusine': 'indian food'
    },
    "Evergreens": {
        'distance': 3,
        'novelty': 1,
        'cost': 4,
        'average rating': 4,
        'cusine': 'vegetarian'
    }
}

restaurant_cols = [
    'distance',
    'novelty',
    'cost',
    'average rating',
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
        row = [description[cat] for cat in restaurant_cols[:4]]
        for cat in restaurant_cols[4:]:
            if cat.split(':')[-1].strip() != description['cusine']:
                row.append(5)
            else:
                row.append(0)
        lst_to_mtrx_r.append(row)
    restaurant_mtrx = np.matrix(lst_to_mtrx_r)


def find_restaurant_preferences(name):
    person = people[name]
    p = np.matrix([person[col] for col in people_cols])
    print(p)
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


if __name__ == '__main__':
    transform_people_matrix()
    # print(people_mtrx)
    transform_restaurant_matrix()
    # print(restaurant_mtrx)
    for rest, score in find_restaurant_preferences('John').items():
        print('\t', rest, ": ", score)
    print("The group scores are:")
    for rest, score in output_restaurant_scores().items():
        print('\t', rest, ": ", score)
    print("The composite group scores are:")
    for rest, score in non_parametric_restaurant_scores().items():
        print('\t', rest, ": ", score)
    print('Each participant has the following leverage:')
    for person, score in find_problematic_users().items():
        print("\t", person, ':', score)
