import csv
from typing import List, Set, Tuple
from models.employee import Employee


class FileService:

    @staticmethod
    def load_employees(filepath: str) -> List[Employee]:
        """
        Loads a list of employees from a CSV file.

        Args:
            filepath (str): Path to the CSV file containing employee details.

        Returns:
            List[Employee]: A list of Employee objects or an empty list in case of an error.
        """
        try:
            with open(filepath, newline="") as f:
                reader = csv.DictReader(f)
                return [
                    Employee(row["Employee_Name"], row["Employee_EmailID"])
                    for row in reader
                ]
        except FileNotFoundError:
            print(f"Error: The file at {filepath} was not found.")
            return []
        except KeyError as e:
            print(f"Error: Missing expected column in the CSV file: {e}")
            return []
        except csv.Error as e:
            print(f"Error reading the CSV file: {e}")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    @staticmethod
    def load_previous_assignments(filepath: str) -> Set[Tuple[str, str]]:
        """
        Loads previous Secret Santa assignments from a CSV file.

        Args:
            filepath (str): Path to the CSV file containing previous pairings.

        Returns:
            Set[Tuple[str, str]]: A set of email pairs representing previous assignments or an empty set in case of an error.
        """
        try:
            with open(filepath, newline="") as f:
                reader = csv.DictReader(f)
                return {
                    (row["Employee_EmailID"], row["Secret_Child_EmailID"])
                    for row in reader
                }
        except FileNotFoundError:
            print(f"Error: The file at {filepath} was not found.")
            return set()
        except KeyError as e:
            print(f"Error: Missing expected column in the CSV file: {e}")
            return set()
        except csv.Error as e:
            print(f"Error reading the CSV file: {e}")
            return set()
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return set()

    @staticmethod
    def save_assignments(assignments, filepath: str):
        """
        Saves Secret Santa assignments to a CSV file.

        Args:
            assignments: A list of Assignment objects to save.
            filepath (str): Path where the CSV file will be saved.

        Raises:
            Exception: If there are issues with writing to the file.
        """
        try:
            with open(filepath, mode="w", newline="") as f:
                fieldnames = [
                    "Employee_Name",
                    "Employee_EmailID",
                    "Secret_Child_Name",
                    "Secret_Child_EmailID",
                ]
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for assignment in assignments:
                    writer.writerow(
                        {
                            "Employee_Name": assignment.giver.name,
                            "Employee_EmailID": assignment.giver.email,
                            "Secret_Child_Name": assignment.receiver.name,
                            "Secret_Child_EmailID": assignment.receiver.email,
                        }
                    )
        except PermissionError:
            print(f"Error: Permission denied to write to {filepath}.")
        except OSError as e:
            print(f"Error: A problem occurred while accessing the file {filepath}: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
