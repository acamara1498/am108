import copy
import numpy as np

from simulation1 import create_agents

def interaction_simulation(people, how_many_people_on_each_side=2):
    new_people = copy.deepcopy(people)

    for i in range(len(people)):
        can_interact = []
        if i > how_many_people_on_each_side:
            can_interact += people[i-how_many_people_on_each_side:i]
        if i < len(people)-(how_many_people_on_each_side + 1):
            can_interact += people[i+1:i+how_many_people_on_each_side+1]

        p_to_left = float(can_interact.count(0))/len(can_interact)
        p_to_moderate = float(can_interact.count(1))/len(can_interact)
        p_to_right = float(can_interact.count(2))/len(can_interact)

        coin = np.random.random_sample()
        if people[i] == 0:
            if coin < p_to_left/(p_to_left + p_to_moderate):
                new_people[i] = 0
            else:
                new_people[i] = 1
        if people[i] == 1:
            if coin < p_to_left:
                new_people[i] = 0
            elif coin < p_to_left + p_to_moderate:
                new_people[i] = 1
            else:
                new_people[i] = 2
        if people[i] == 2:
            if coin < p_to_right/(p_to_right + p_to_moderate):
                new_people[i] = 2
            else:
                new_people[i] = 1

    return new_people

def run_simulations(time_steps=10, leftist_initial=10, moderate_initial=10, rightist_initial=10):
    people = create_agents(leftist_initial,moderate_initial,rightist_initial)
    for _ in range(time_steps):
        people = interaction_simulation(people, how_many_people_on_each_side=2)
        # print "leftist", people.count(0), "moderate", people.count(1), "rightist", people.count(2)

    return people.count(0), people.count(1), people.count(2)

def run_n_similations(n, l_initial=10, m_initial=10, r_initial=10):
    left = 0
    mod = 0
    right = 0

    for _ in range(n):
        newleft, newmod, newright = run_simulations(time_steps=300, leftist_initial=l_initial, moderate_initial=m_initial, rightist_initial=r_initial)
        left += float(newleft)/n
        mod += float(newmod)/n
        right += float(newright)/n

    print n, "simulations"
    print "average leftist",left , "average moderate", mod, "average rightist", right

if __name__== "__main__":
    left, mod, right = run_simulations(time_steps=100)
    print "leftist",left , "moderate", mod, "rightist", right
    run_n_similations(n=300, l_initial=1000, m_initial=1000, r_initial=1000)

    # people being born and dying into the model (cults, different birthrate etc)
