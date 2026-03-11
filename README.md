# API Test Suite — Python + pytest

A Python-based API test suite built to practice real-world test automation.
Tests the JSONPlaceholder REST API using pytest and requests.

---

## Why I Built This
I built this project to move beyond tutorials and write real automated tests in Python.

---

## What This Tests
- Valid API responses (status code + data)
- Schema validation (correct data types)
- Negative cases (invalid IDs)
- Input validation (bad input rejected before API call)
- Error handling (graceful failure, no crashes)

---

## Tech Stack
- Python 3.11
- pytest
- requests
- GitHub Actions (CI)

---

## How to Run

# Clone the repo
git clone https://github.com/YOUR_USERNAME/api-test-suite-python.git
cd api-test-suite-python

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install requests 
pip install pytest

# Run tests
pytest test_posts.py -v

---

## What I Found
While testing, I noticed that validating status code alone is not enough.
The API can return 200 with empty or incorrect data, so I added schema validation
to check data types and field existence instead of hardcoding expected values.
Hardcoding breaks tests when data changes — testing structure is more reliable.
I also found that calling a non-existent ID returns 404 with an empty body {}.
Without proper logging, this looks the same as a successful empty response.
I fixed this by saving status alongside data in the response log.
---

## Author
[Marium, https://www.linkedin.com/in/marium-iqbal-07728139, https://mariumiqbal.github.io/dev-portfolio/]