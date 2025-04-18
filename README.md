# CM50277 Flight Management

Welcome to the Flight Management Console (CLI) for the CM50277 Coursework 1 (April 2025). 

To get you started you will need
+ Python3 (3.8.10)
+ SQLite3 (3.31.1)
+ ruff (0.11.5)
+ sqlfluff ()

## Getting Started

To run the CLI simply run the below command to enter the CLI

```python
python3 main.py
```

## Tests

Unit tests have been added to this project to promote Test Driven Development (TDD)

```python
python3 -m unittest discover -v
```

## Lint
```python
python3 -m ruff check -v
```

## SQLFluff
```python
python3 -m sqlfluff lint --dialect sqlite --exclude-rules LT05
```


