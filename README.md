# Favorite Problems Tracker

A Python application that interfaces with an SQLite database to query and count user-submitted problem preferences from a dataset.

## Features
- Built using Python's standard `sqlite3` library.
- Formats input automatically using `.capitalize()` for accurate database matching.
- Implements secure parameterized SQL queries to prevent SQL injection vulnerabilities.

## File Structure
- `fav-problems.py`: Main Python script for querying the database.
- `fav.csv`: Raw CSV dataset containing language and problem preferences.
- `fav.db`: SQLite database file created from the CSV data.

## Requirements
- Python 3.x
- SQLite3

## How to Run

1. Clone the repository:
   ```bash
   git clone [https://github.com/boodetolah-design/fav-problem.git](https://github.com/boodetolah-design/fav-problem.git)
