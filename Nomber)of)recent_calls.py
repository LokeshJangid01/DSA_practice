from collections import deque

class RecentCounter:
    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the new request to the queue
        self.requests.append(t)
        
        # Remove outdated requests
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # Return the number of requests in the last 3000ms
        return len(self.requests)
    
obj = RecentCounter()
print(obj.ping(1))    # Output: 1
print(obj.ping(100))  # Output: 2
print(obj.ping(3001)) # Output: 3
print(obj.ping(3002)) # Output: 3 (3002 - 3000 = 2, which is less than 3000ms)                          

# Example usage:
# obj = RecentCounter()
# print(obj.ping(1))    # Output: 1
# print(obj.ping(100))  # Output: 2
# print(obj.ping(3001)) # Output: 3
# print(obj.ping(3002)) # Output: 3 (3002 - 3000 = 2, which is less than 3000ms)