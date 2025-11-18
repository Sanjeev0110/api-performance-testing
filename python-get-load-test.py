
## 2️⃣ `python-get-load-test.py`

```python
import requests
import time
import threading
import random

API_URL = "https://dummyjson.com/users"
THREADS = 20
REQUESTS_PER_THREAD = 20

def load_test(thread_id: int):
    for i in range(REQUESTS_PER_THREAD):
        try:
            start = time.time()
            response = requests.get(API_URL, timeout=5)
            end = time.time()

            elapsed_ms = round((end - start) * 1000, 2)
            print(f"[Thread {thread_id}] Request {i+1}: "
                  f"Status={response.status_code}, Time={elapsed_ms} ms")
        except requests.exceptions.RequestException as e:
            print(f"[Thread {thread_id}] Request {i+1}: ERROR -> {e}")

threads = []

print("Starting GET /users load test...")
start_overall = time.time()

for t_id in range(1, THREADS + 1):
    t = threading.Thread(target=load_test, args=(t_id,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_overall = time.time()
total_time = round(end_overall - start_overall, 2)

print(f"\nCompleted load test with {THREADS} threads and "
      f"{REQUESTS_PER_THREAD} requests each.")
print(f"Total elapsed time: {total_time} seconds")
