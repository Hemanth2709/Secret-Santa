from models.employee import Employee
from services.assignment_service import AssignmentService

def test_assignment_no_self_assignment():
    """
    Test case to ensure no employee is assigned to themselves.
    """
    # Set up employees for the test
    employees = [
        Employee("Alice", "alice@acme.com"),
        Employee("Bob", "bob@acme.com"),
        Employee("Charlie", "charlie@acme.com")
    ]
    # No previous assignments (empty set)
    previous_pairs = set()

    # Initialize the service and generate assignments
    service = AssignmentService(employees, previous_pairs)
    assignments = service.generate_assignments()

    # Ensure that no one is assigned to themselves
    for a in assignments:
        assert a.giver != a.receiver, f"Self-assignment error: {a.giver.name} was assigned to themselves."

    # Ensure there is at least one assignment
    assert len(assignments) > 0, "No assignments were generated."

    # Optional: You could also check that the number of assignments matches the number of employees
    assert len(assignments) == len(employees), f"Expected {len(employees)} assignments, got {len(assignments)}."
