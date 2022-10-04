'''
Read in comma-separated lists.
Parse as intcode.
4-digit codes. [what, arg1_position, arg2_position, solution_output_location]
1 = add
2 = multiply
99 = all done

Function should read an intcode, and return the value in a particular location.
'''
import copy


def intcodeSolver(opslist, position):
    working_index = 0
    # Nothing about this is 'for-loop'. It's just so it doesn't run forever accidentally.
    for i in range(len(opslist)):
        # Status updates are cool
        # msg = "Working index: " + str(working_index)
        # print(msg)
        if opslist[working_index] == 99:
            return (opslist[position], opslist)
        action = opslist[working_index]
        # There is an index into your working set
        # The thing found at that index of your opslist...
        # ... is where to look in your opslist.
        arg1 = opslist[opslist[working_index+1]]
        arg2 = opslist[opslist[working_index+2]]
        output_location = opslist[working_index+3]
        if action == 1:
            output = arg1 + arg2
        elif action == 2:
            output = arg1 * arg2
        # always watch for broken things and alert early
        else:
            print("Something went wrong")
            break
            return (-1, ['All is not well.'])
        opslist[output_location] = output
        working_index += 4
    # Should only see this if we get ot the end of our impossible for-loop
    return (-1, ['Something did not go right'])

# quick checks
input = [1,0,0,0,99]
intcodeSolver(input, 2)

input = [2,3,0,3,99]
intcodeSolver(input, 2)

input = [2,4,4,5,99,0]
intcodeSolver(input, 2)

input = [1,1,1,4,99,5,6,0,99]
intcodeSolver(input, 2)

# I lazily copy-pasted this here.
# A better solution would clearly read it from a text file.
week1_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]
week1_input[1] = 12
week1_input[2] = 2
solution = intcodeSolver(week1_input, 0)

###########
## Part 2
'''
Find the replacements for indices 1 and 2, between 0 and 99 inclusive, that
make the value at index 0, after the program ends, 19690720.
'''

def tester(original):
    for i in range(100):
        for j in range(100):
            working = copy.deepcopy(original)
            working[1] = i
            working[2] = j
            output = intcodeSolver(working, 0)
            if output[0] == 19690720:
                print(i)
                print(j)
                ans = 100 * i + j
                msg = "Answer is " + str(ans)
                print(msg)
                break

week1_input = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,19,6,23,2,13,23,27,1,9,27,31,2,31,9,35,1,6,35,39,2,10,39,43,1,5,43,47,1,5,47,51,2,51,6,55,2,10,55,59,1,59,9,63,2,13,63,67,1,10,67,71,1,71,5,75,1,75,6,79,1,10,79,83,1,5,83,87,1,5,87,91,2,91,6,95,2,6,95,99,2,10,99,103,1,103,5,107,1,2,107,111,1,6,111,0,99,2,14,0,0]

tester(week1_input)
