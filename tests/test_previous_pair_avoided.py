from models.employee import Employee
from services.assignment_service import AssignmentService

def test_previous_pair_avoided():
    """
    Ensure that no assignment includes a pair from previous years.
    """
    # Setup employees
    employees = [
        Employee("Alice", "alice@acme.com"),
        Employee("Bob", "bob@acme.com"),
        Employee("Charlie", "charlie@acme.com")
    ]

    # One previous pairing should be avoided
    previous_pairs = {("alice@acme.com", "bob@acme.com")}

    # Generate new assignments
    service = AssignmentService(employees, previous_pairs)
    assignments = service.generate_assignments()

    # Assert previous pair is not reused
    for a in assignments:
        assert (a.giver.email, a.receiver.email) not in previous_pairs, (
            f"Previous pair ({a.giver.email}, {a.receiver.email}) was reused."
        )

    # Optional: Ensure all employees are assigned
    assert len(assignments) == len(employees), "Mismatch in number of assignments."
