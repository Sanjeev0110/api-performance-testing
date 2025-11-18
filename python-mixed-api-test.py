import requests
import time
import threading
import random
import csv

BASE_URL = "https://dummyjson.com"
THREADS = 15
REQUESTS_PER_THREAD = 15

# Load CSV user data if available
USER_DATA_FILE = "test-data/users.csv"
user_data = []

try:
    with open(USER_DATA_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        user_data = list(reader)
        print(f"Loaded {len(user_data)} users from {USER_DATA_FILE}")
except FileNotFoundError:
    print(f"WARNING: {USER_DATA_FILE} not found. POST tests will use dummy data.")


def get_users():
    url = f"{BASE_URL}/users"
    return requests.get(url, timeout=5)


def get_user_by_id():
    user_id = random.randint(1, 30)
    url = f"{BASE_URL}/users/{user_id}"
    return requests.get(url, timeout=5)


def post_user():
    url = f"{BASE_URL}/users/add"
    if user_data:
        user = random.choice(user_data)
        payload = {
            "firstName": user.get("firstName", "John"),
            "lastName": user.get("lastName", "Doe"),
            "email": user.get("email", "john.doe@example.com"),
            "age": int(user.get("age", 25)),
        }
    else:
        payload = {
            "firstName": "John",
            "lastName": "Doe",
            "email": "john.doe@example.com",
            "age": 25,
        }

    return requests.post(url, json=payload, timeout=5)


def timed_request(func, label: str, thread_id: int, index: int):
    start = time.time()
    try:
        response = func()
        end = time.time()
        elapsed_ms = round((end - start) * 1000, 2)
        print(f"[Thread {thread_id}] {label} #{index}: "
              f"Status={response.status_code}, Time={elapsed_ms} ms")
    except requests.exceptions.RequestException as e:
        end = time.time()
        elapsed_ms = round((end - start) * 1000, 2)
        print(f"[Thread {thread_id}] {label} #{index}: ERROR after {elapsed_ms} ms -> {e}")


def mixed_test(thread_id: int):
    for i in range(1, REQUESTS_PER_THREAD + 1):
        # 50% GET /users, 30% GET /users/{id}, 20% POST /users/add
        r = random.random()
        if r < 0.5:
            timed_request(get_users, "GET /users", thread_id, i)
        elif r < 0.8:
            timed_request(get_user_by_id, "GET /users/{id}", thread_id, i)
        else:
            timed_request(post_user, "POST /users/add", thread_id, i)


print("Starting mixed API performance test...")
threads = []
start_overall = time.time()

for t_id in range(1, THREADS + 1):
    t = threading.Thread(target=mixed_test, args=(t_id,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

end_overall = time.time()
total_time = round(end_overall - start_overall, 2)

print(f"\nCompleted mixed API test with {THREADS} threads and "
      f"{REQUESTS_PER_THREAD} requests each.")
print(f"Total elapsed time: {total_time} seconds")
