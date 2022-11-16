import threading
import time

ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

def add_range(start, finish):
    sum = 0
    for i in range(start, finish + 1):
        sum+= i
    return sum

print("Main Thread Running")

result = [0] * len(ranges)

def runner(name, count):
    """ Thread running function. """

    for i in range(len(ranges)):
        print(f"Running: {name} {i}")
        result[i] = add_range(ranges[i][0],ranges[i][1])
        time.sleep(0.2)  # seconds

# We need to keep track of them so that we can join() them later. We'll
# put all the thread references into this array
threads = []

# Launch all threads!!
for i in range(len(ranges)):

    # Give them a name
    name = f"Thread{i}"

    # Set up the thread object. We're going to run the function called
    # "runner" and pass it two arguments: the thread's name and count:
    t = threading.Thread(target=runner, args=(name, i+3))

    # The thread won't start executing until we call `start()`:
    t.start()

    # Keep track of this thread so we can join() it later.
    threads.append(t)

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.

for t in threads:
    t.join()

print(result)
print(sum(result))