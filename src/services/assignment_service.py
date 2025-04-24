import random
from typing import List, Set, Tuple
from models.employee import Employee
from models.assignment import Assignment


class AssignmentService:
    def __init__(self, employees: List[Employee], previous_pairs: Set[Tuple[str, str]]):
        """
        Initializes the AssignmentService with employees and previous assignments.

        Args:
            employees (List[Employee]): List of employees for the assignment.
            previous_pairs (Set[Tuple[str, str]]): Set of previous giver/receiver pairs.

        Raises:
            ValueError: If the employee list is empty.
        """
        if not employees:
            raise ValueError("The list of employees cannot be empty.")
        self.employees = employees
        self.previous_pairs = previous_pairs

    def generate_assignments(self) -> List[Assignment]:
        """
        Generates Secret Santa assignments, avoiding past pairings and self-assignments.

        Returns:
            List[Assignment]: List of valid Secret Santa assignments.

        Raises:
            ValueError: If there are fewer than two employees.
            Exception: If a valid assignment can't be made after 1000 attempts.
        """

        if len(self.employees) < 2:
            raise ValueError(
                "At least two employees are required to generate assignments."
            )

        givers = self.employees[:]
        receivers = self.employees[:]

        max_attempts = 1000
        for _ in range(max_attempts):
            random.shuffle(receivers)
            pairs = list(zip(givers, receivers))

            if all(
                giver != receiver
                and (giver.email, receiver.email) not in self.previous_pairs
                for giver, receiver in pairs
            ):
                return [Assignment(giver, receiver) for giver, receiver in pairs]

        raise Exception(
            "Could not generate valid Secret Santa assignments after maximum attempts."
        )
