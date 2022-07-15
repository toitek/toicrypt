#!/usr/bin/python3
def rand_gen():
            #seed 
            Xo = 10000
            #modulus, multiplier_term, increment_term 
            m, a, c,  =  1771875, 2416, 374441
            #numbers of rundom numbers to be generated
            no_of_random_nums = 10
            #to store random numbers
            random_nums = [0] * (no_of_random_nums)

            #initilization of seed state
            random_nums[0] = Xo

            #traverse to generate required
            #numbers of random numbers

            for i in range(1, no_of_random_nums):

                #follow the linear congruential method
                random_nums[i] = ((random_nums[i - 1] * a) + c ) % m
            for i in random_nums:

                print(i, end = " ")
L = []
L = rand_gen()
print(L)
