from time import time

# calc time between end and start
# stopwatch started
try:
    start = input("Enter 'Y' to start the stopwatch:")
    if start == "y" or start == "Y":
        t1 = time()
        # stopwatch ended
        end = input("Enter 'N' to stop the stopwatch:")
        if end == "n" or end == 'N':
            t2 = time()

    elapsed = t2 - t1
    print('Elapsed time is %f seconds.' % elapsed)
except NameError:
    print("Invalid input!")
