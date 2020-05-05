# Cal utility

This project features a Python version of the unix Cal utility. Additionally, we provide a set of basic tests for educational purposes.

## Requirements

+ [Python 3.7+](https://www.python.org/)
+ [python3-venv](https://docs.python.org/3/library/venv.html)
+ requirements.txt

## Installation or Getting Started

Getting started:

	sudo apt install python3-venv	
	cd mutation_demo
	python3 -m venv /mutation_demo/venv
	source venv/bin/activate
	pip install -r requirements.txt

## Testing

	# run tests normally
	pytest -vv  cal.py 
	
	#perform tests with line (node) coverage report
	pytest -vv  cal.py  	 --cov=cal

	# perform tests with branch coverage report
	pytest -vv  cal.py  --cov=cal	--cov-branch

	#run tests with mutmut
	mutmut run --paths-to-mutate= .. /mutmut_demo/cal.py

## Contributors

+ Stevão Andrade

## License

feel free to change distribute or suggest corrections and additions.
