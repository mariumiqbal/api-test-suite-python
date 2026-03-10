# api-test-suite-python

Project setup
// Create virtual environment
python -m venv venv
venv\Scripts\activate

run script:
python test_api.py

Install request
pip install requests

Setup Pytest
pip install pytest

Run test
pytest test_posts.py -v  //-v means verbose — it shows each test name and whether it passed or failed.

