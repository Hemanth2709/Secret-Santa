# Secret Santa Assignment System 🎅

Automated system for assigning Secret Santa pairs among employees while avoiding:
- Self-assignment
- Repeating last year's matches

## Project Structure

- `data/` - CSV input files (`current_employees.csv`, `previous_assignments.csv`)
- `src/` - Main logic with models and services
- `tests/` - Unit tests
- `output/` - Generated results

## How to Run

```bash
python src/main.py
```

## Run Tests

```bash
pytest
```

## Input Format

### current_employees.csv
```
Employee_Name,Employee_EmailID
Hamish Murray,hamish.murray@acme.com
..
..
..
..
Matthew King,matthew.king.jr@acme.com
Mark Lawrence,mark.lawrence@acme.com
```

### previous_assignments.csv
```
Employee_Name,Employee_EmailID,Secret_Child_Name,Secret_Child_EmailID
Hamish Murray,hamish.murray@acme.com,Matthew King,matthew.king@acme.com,
Layla Graham,layla.graham@acme.com,Matthew King,matthew.king@acme.com
```
