import copy
import numpy as np

def createAgents(leftists, moderates, rightists):
    return ([0]*leftists + [1]*moderates + [2]*rightists)

def countPeople(people):
    leftists = 0
    moderates = 0
    rightists = 0

    # Counter depending on the initiialization of the people in the array
    for person in people:
        if person == 0:
            leftists += 1
        if person == 1:
            moderates += 1
        if person == 2:
            rightists += 1

    return leftists, moderates, rightists

def runSimulation(people):
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

if __name__== "__main__":
    people = createAgents(10,10,10)

    leftists, moderates, rightists = countPeople(people)

    while moderates != 0:
        people = runSimulation(people)
        leftists, moderates, rightists = countPeople(people)

        print "leftist", leftists, "moderate", moderates, "rightist", rightists
