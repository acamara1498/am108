import numpy as np

people =[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]

leftist = 0
moderate = 0
rightist = 0

# Counter depending on the initiialization of the people in the array
for person in people:
    if person == 0:
        leftist += 1
    if person == 1:
        moderate += 1
    if person == 2:
        rightist += 1

while moderate != 0:

    #  for loop for a single timestep
    for i in range(len(people)):
        coin = np.random.random_sample()
        if people[i] == 0:
            if coin > 0.3:
                people[i] = 0
            else:
                people[i] = 1
                leftist -= 1
                moderate += 1
        elif people[i] == 1:
            if coin < 0.4:
                people[i] = 0
                leftist += 1
                moderate -= 1
            elif coin < 0.6:
                people[i] = 1
            else:
                people[i] = 2
                rightist += 1
                moderate -= 1
        else:
            if coin > 0.3:
                people[i] = 2
            else:
                people[i] = 1
                rightist -= 1
                moderate += 1

    print "leftist", leftist, "moderate", moderate, "rightist", rightist
