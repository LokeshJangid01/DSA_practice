import threading
x = 0
def print_numbers():
    global x
    x += 1
Th = []

# Create and start the thread
for _ in range(1000):
    t = threading.Thread(target=print_numbers)
    t.start()
    Th.append(t)
    

# Main thread continues running
for t in Th:
    t.join()
print(x)