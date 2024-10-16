# TaskTracker
Roadmap.sh project

# Run the tests
python -m unittest tests.py

# Run the tests with coverage
python3 -m coverage run -m unittest discover && python3 -m coverage report -m

# Run the tests with coverage and generate an HTML report
python3 -m coverage run -m unittest discover && python3 -m coverage html

# Run the application examples
python3 app.py add "Buy groceries"
python3 app.py update 1 "Buy groceries and fruits"
python3 app.py delete 1
python3 app.py list
python3 app.py list todo
python3 app.py list in-progress
python3 app.py list done
