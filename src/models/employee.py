import re


class Employee:
    """
    Represents an employee with a name and email.

    Attributes:
        name (str): Employee's name.
        email (str): Employee's email address.
    """

    def __init__(self, name: str, email: str):
        """
        Initializes an Employee with a name and email.

        Args:
            name (str): Employee's name.
            email (str): Employee's email address.

        Raises:
            ValueError: If name or email is empty or email format is invalid.
        """
        self.name = name.strip()
        self.email = email.strip()

        if not self.name:
            raise ValueError("Employee name cannot be empty.")
        if not self.email:
            raise ValueError("Employee email cannot be empty.")
        if not self._is_valid_email(self.email):
            raise ValueError(f"Invalid email format: {self.email}")

    def _is_valid_email(self, email: str) -> bool:
        """
        Validates the email format.

        Returns:
            bool: True if valid, False otherwise.
        """
        pattern = r"^[^@]+@[^@]+\.[^@]+$"
        return re.match(pattern, email) is not None

    def __eq__(self, other):
        """
        Compares two Employee objects by email.

        Args:
            other (Employee): Employee to compare.

        Returns:
            bool: True if emails match.
        """
        return isinstance(other, Employee) and self.email == other.email

    def __hash__(self):
        """
        Returns a hash value based on email.

        Returns:
            int: Hash value of the email.
        """
        return hash(self.email)

    def __repr__(self):
        """
        Returns a string representation of the Employee.

        Returns:
            str: String representation of the employee.
        """
        return f"Employee({self.name}, {self.email})"
