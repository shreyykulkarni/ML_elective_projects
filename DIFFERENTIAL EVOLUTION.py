import math
import numpy as np
from random import seed
from random import randint
from random import uniform
from random import random


# Defining fitness function
def opt_fn(x, y):
    #fitness = -((y + 47) * math.sin(math.sqrt(abs((x / 2) + (y + 47))))) - (x * math.sin(math.sqrt(abs(x - (y + 47)))))  # Given Egg-holder function
    fitness =  -abs((math.sin(x))*(math.cos(y))*np.exp(abs(1-(math.sqrt(x*x + y*y)/np.pi))))
    return fitness


# Predefining initial and given parameters
# K and F are relaxation parameters
# Fit is the output value of the aforementioned fitness function
# Given value of crossover probability is 0.8
# r1, r2 and r3 are arbitrarily selected members of the population from generation 'g'
M = []
T = [0.0, 0.0]
K = 0.5
F = 0
fit = 0
min = 10000
min_index = 0
r1 = -1
r2 = -1
r3 = -1
sat = 0
Pop_size = input("Input the value of the population size: \n")
Pop_size = int(Pop_size)
Generation_size = 200
cross_prob = 0.80
cross_val = 0.0
seed(11)

# INITIALIZING FIRST GENERATION
for i in range(Pop_size):
    I = []
    x = uniform(-10, 10)  # Given range of x is [-10,10]
    y = uniform(-10, 10)  # Given range of y is [-10,10]
    fit = opt_fn(x, y)
    if (fit < min):
        min = fit
        min_index = i
    I.append(x)
    I.append(y)
    I.append(fit)
    M.append(I)
    file = open('17XJ1A0348.txt', 'w+')
# M is a 2 dimensional array with each element containing an array of x, y and fitness function output.

# Beginning iterations from generation two onwards; Generating traction vector.
# Given range of F is [-2,2]
for i in range(Generation_size):
    r1 = -1
    r2 = -1
    r3 = -1
    F = uniform(-2, 2)
    for j in range(Pop_size):
        while (1):
            val = []
            for k in range(len(M[j]) - 1):
                # Making sure r1,r2 and r3 are mutually exclusive
                r1 = randint(0, Pop_size - 1)
                while (r1 == j):
                    r1 = randint(0, Pop_size - 1)
                r2 = randint(0, Pop_size - 1)
                while (r2 == r1):
                    r2 = randint(0, Pop_size - 1)
                r3 = randint(0, Pop_size - 1)
                while (r3 == r2):
                    r3 = randint(0, Pop_size - 1)
                val.append(M[j][k] + K * (M[r1][k] - M[j][k]) + F * (M[r2][k] - M[r3][k]))
                cross_val = random()
            if (val[0] >= -10 and val[0] <= 10 and val[1] >= -10 and val[1] <= 10):
                break
        for k in range(len(M[j]) - 1):
            cross_val = random()
            if (cross_val <= cross_prob):                                                                        # If crossover value is greater than crossover probability
                T[k] = val[ k]                                                                                   # We input values from the parent vector( previous generation's mutant vector) into the trial vector
            else:                                                                                                # Else we input values from present generation's mutant vector
                T[k] = M[j][k]
        fit = opt_fn(T[0], T[1])
        if (fit < M[j][2]):
            M[j][0] = T[0]
            M[j][1] = T[1]
            M[j][2] = fit
        if (fit < min):
            min = fit
            min_index = j
    print(M[min_index])
    op = str(M[min_index][2])
    file.write(op)
    file.write('\n')

file.close()


