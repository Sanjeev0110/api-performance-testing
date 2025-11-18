# API Performance Testing using JMeter & Python

This project demonstrates performance testing of public REST APIs using **Apache JMeter** and **Python load-testing scripts**.  

The project covers:
- Designing load test plans  
- Parameterized test data  
- REST API load testing  
- Multi-threaded Python scripts  
- Assertions, latency tracking, and reporting  
- Running tests in GUI and Non-GUI JMeter mode  

---

## 📌 APIs Used

Public API used for sample load testing:

Endpoints tested:
- `GET /users` → Fetch all users  
- `GET /users/{id}` → Fetch a single user  
- `POST /users/add` → Create user (dummy API, safe for testing)  

---

## 🧰 Tools & Technologies

- **JMeter** – Performance test plan and reporting  
- **Python** (requests, threading) – Custom load scripts  
- **CSV Test Data** – Parameterized POST requests  
- **GitHub** – Version control and documentation  

Optional future enhancements:
- Grafana dashboards  
- Locust/K6 load tests  
- CloudWatch monitoring  

---


# ▶ How to Run the Project

## 1. Install Dependencies

Python libraries:
```bash
pip install requests


1. Simple GET Load Test
python python-get-load-test.py

2. Mixed API Load Test
python python-mixed-api-test.py

2. Run JMeter in Non-GUI Mode (Recommended)
jmeter -n -t jmeter-test-plan.jmx -l results/results.jtl -e -o results/html-report


⭐ Author
Sanjeev Kulkarni
Performance Testing & Backend Enthusiast
GitHub: https://github.com/Sanjeev0110

