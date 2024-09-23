import time
from threading import Lock
from collections import deque

class RateLimiter:
    def __init__(self, limit=5, window=60):
        self.limit = limit  # Maximum number of requests allowed
        self.window = window  # Time window in seconds
        self.user_requests = {}  # Dictionary to store user request timestamps
        self.lock = Lock()  # Lock for thread-safe operations

    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            
            if user_id not in self.user_requests:
                self.user_requests[user_id] = deque()

            # Remove timestamps older than the time window
            while self.user_requests[user_id] and self.user_requests[user_id][0] <= current_time - self.window:
                self.user_requests[user_id].popleft()

            # Check if the user has exceeded the limit
            if len(self.user_requests[user_id]) < self.limit:
                self.user_requests[user_id].append(current_time)
                return True
            else:
                return False

# Example usage
rate_limiter = RateLimiter()

# Simulate multiple requests
for i in range(10):
    user_id = "user1"
    allowed = rate_limiter.allow_request(user_id)
    print(f"Request {i+1} for {user_id}: {'Allowed' if allowed else 'Blocked'}")
    time.sleep(0.1)  # Small delay between requests