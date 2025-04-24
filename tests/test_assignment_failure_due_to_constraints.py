import pytest
from models.employee import Employee
from services.assignment_service import AssignmentService


def test_assignment_failure_due_to_constraints():
    """
    Test case to check if the assignment generation fails when all employees have already been assigned to each other
    in the past (previous_pairs).
    """

    # Create List of Employees for Test
    employees = [
        Employee("Hemanth", "hemanth@acme.com"),
        Employee("Gopal", "gopal@acme.com"),
    ]

    # Test previous pairs that include all possible pairings
    previous_pairs = {
        ("hemanth@acme.com", "gopal@acme.com"),
        ("gopal@acme.com", "Hemanth@acme.com"),
    }

    # Initialize the assignment service with employees and previous pairs
    service = AssignmentService(employees, previous_pairs)

    # Assert that an exception is raised when trying to generate assignments
    with pytest.raises(Exception):
        service.generate_assignments()
