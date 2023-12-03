# Data engineering Python tests

## Setup

Create a venv using `python -m venv venv`

Activate the venv

Run `pip install -r requirements.txt` to download the relevant libraries for the scripts

## Files in the repo

There are 5 scripts in the root of this repo/directory:

- test_1.py
- test_2.py
- test__test_2.py
- test_3.py
- test_test_3.py

### Test 1

This script extracts and structures data from the file `sample.log`. 

Run `python test_1.py` and it will be automatically tested.

### Test 2

This script gets data from an API and matches it with data from the file `people.csv`.

Run `python test_2.py` to recieve the output data.

Run `pytest test_test_2.py` to see the output of the test file for this script.

### Test 3

Contains a function that sums the numbers in a datetime string.

Run `pytest test_test_3.py` to see the output of the test file for this script.

## Future areas for improvement

FIle test_2.py -

* To improve this script, a loading step could've been added on, to upload the .csv data to a database instead. This could improve scalability (if database was created on the cloud e.g. AWS) and querying efficiency for the analysts, as they could then organise the data and search through it quicker, if neccessary.
