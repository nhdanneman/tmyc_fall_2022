'''
The 6-digit password problem.

Passwords are between 111111 and 999999, inclusive.
Must have at least one "double" digit (i.e. two adjacent digits are equal)
Must be monotonically increasing.

Count the number of possible passwords between two given 6-digit numbers.
'''

import numpy as np
# Plan: iterate over lo to high
# Do the "between lower and upper" check
# Break the number up into component digits to do the monotonocity check and zero check as a vector subtraction


def password_counter(lo, hi):
    counter = 0
    # check to see if the number is within the bounds:
    for i in range(lo, (hi+1)):
        if i >= lo and i <= hi:
            digits = np.array([int(x) for x in str(i)])
            # subtract the 1:nth entries from the 0-(n-1)th digits:
            arr = digits[1:] - digits[0:-1]
            # all elements must be positive (monotonicity), and 1 or more must be zero (doubling)
            # this is a quick way to check the monotonicity and doubling constraints!
            if all(arr > -1) and any(arr==0):
                counter += 1
    return counter

answer = password_counter(284639, 748759)

# hm, no tests this time, eh?

# Part two, now with more annoying criteria!
# I read it as: there is at least one double that is ONLY a double...
def password_counter2(lo, hi):
    counter = 0
    tester = np.array([1,0,1])
    # check to see if the number is within the bounds:
    for i in range(lo, (hi+1)):
        if i >= lo and i <= hi:
            digits = np.array([int(x) for x in str(i)])
            # subtract the 1:nth entries from the 0-(n-1)th digits:
            diff_arr = digits[1:] - digits[0:-1]
            if all(diff_arr > -1) and any(diff_arr==0):
                # the extra criteria means in the subtracted array, at least one zero must not be beside another zero
                # idea: make the array 0 where it is zero, and change all other entries to be 1
                # idea: add a 1 to the start and end of the array, then search it for a '101' pattern
                # this would be indicative of a "standalone" double
                # change the array to be 0 where doubles, 1 everywhere else
                diff_arr[diff_arr!=0] = 1
                diff_arr = np.insert(diff_arr, 0, 1) # this is "pre-pend"
                diff_arr = np.append(diff_arr, 1) # this is append
                for k in range(len(diff_arr)-1):
                    triple = diff_arr[k:k+3]
                    if np.all(triple == tester):
                        # found one, add it to counter
                        counter += 1
                        # break out of the k loop, back into the i loop
                        break
    return counter

answer = password_counter2(284639, 748759)

