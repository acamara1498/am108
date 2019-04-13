import copy
import numpy as np

def create_agents(leftists, moderates, rightists):
    return ([0]*leftists + [1]*moderates + [2]*rightists)

def count_people(people):
    return people.count(0), people.count(1), people.count(2)

def run_simulation(people):
    new_people = copy.deepcopy(people)
    for i in range(len(new_people)):
        coin = np.random.random_sample()
        if new_people[i] == 0:
            if coin > 0.3:
                new_people[i] = 0
            else:
                new_people[i] = 1
        elif new_people[i] == 1:
            if coin < 0.4:
                new_people[i] = 0
            elif coin < 0.6:
                new_people[i] = 1
            else:
                new_people[i] = 2
        else:
            if coin > 0.3:
                new_people[i] = 2
            else:
                new_people[i] = 1

    return new_people


def run_n_simulations(n=1, leftist_initial=10, moderate_initial=10, rightist_initial=10):
    avgl = 0
    avgm = 0
    avgr = 0
    for i in range(n):
        people = create_agents(leftist_initial, moderate_initial, rightist_initial)

        leftists, moderates, rightists = count_people(people)

        while moderates != 0:
            people = run_simulation(people)
            leftists, moderates, rightists = count_people(people)

        avgl += leftists
        avgm += moderates
        avgr += rightists

    print "average leftist", avgl/float(n), "average moderate", avgm/float(n), "average rightist", avgr/float(n)

if __name__== "__main__":
    run_n_simulations()
    run_n_simulations(n=2, leftist_initial=5, moderate_initial=10, rightist_initial=4)
