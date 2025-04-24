from models.employee import Employee
from services.assignment_service import AssignmentService

def test_all_secret_children_unique():
    """
    Ensure each employee is assigned a unique secret child.
    """
    employees = [
        Employee("Alice", "alice@acme.com"),
        Employee("Bob", "bob@acme.com"),
        Employee("Charlie", "charlie@acme.com")
    ]
    previous_pairs = set()

    service = AssignmentService(employees, previous_pairs)
    assignments = service.generate_assignments()

    receivers = [a.receiver.email for a in assignments]

    # Check no duplicate receivers
    assert len(receivers) == len(set(receivers)), "Duplicate secret child detected"

    # Optional: Ensure total assignment count matches employee count
    assert len(assignments) == len(employees), "Mismatch in assignment count"
