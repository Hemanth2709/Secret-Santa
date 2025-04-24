from models.employee import Employee


class Assignment:
    """
        Represents a Secret Santa assignment between two employees.

    Attributes:
        giver (Employee): The employee giving the gift.
        receiver (Employee): The employee receiving the gift.
    """

    def __init__(self, giver: Employee, receiver: Employee):
        """
        Initializes the assignment with a giver and receiver.

        Args:
            giver (Employee): The person giving the gift.
            receiver (Employee): The person receiving the gift.

        Raises:
            TypeError: If either the giver or receiver is not an Employee.
            ValueError: If the giver and receiver are the same person.
        """
        if not isinstance(giver, Employee):
            raise TypeError(
                f"Giver must be an Employee instance, got {type(giver).__name__}"
            )
        if not isinstance(receiver, Employee):
            raise TypeError(
                f"Receiver must be an Employee instance, got {type(receiver).__name__}"
            )
        if giver.email == receiver.email:
            raise ValueError("Giver and receiver cannot be the same employee.")

        self.giver = giver
        self.receiver = receiver

    def __repr__(self):
        """
        Returns a string representation of the assignment.

        Returns:
            str: A string like "Assignment(giver -> receiver)".
        """

        return f"Assignment({self.giver} -> {self.receiver})"
