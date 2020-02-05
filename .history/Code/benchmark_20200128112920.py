import time as t #import the time module
#https://docs.python.org/3/library/time.html#time.time


def bench(func):
    start_time = t.time()
    func
    end_time = t.time()
    return total_run_time = end_time - start_time

    


#define functions
# def test_function():
#   sum = 0
#   for i in range(100):
#     sum += i
#   return sum

#record the time before running the code
# start_time = t.time()

#call the function
# test_function()

#record the time after the code has finished running
# end_time = t.time()

#The total time in seconds is differece between the start time and the end time
# total_run_time = end_time - start_time