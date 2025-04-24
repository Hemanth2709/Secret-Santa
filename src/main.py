import sys
from services.file_service import FileService
from services.assignment_service import AssignmentService

def main():
    try:
        print("Loading employee data...")
        # Load current employee list
        employees = FileService.load_employees("data/current_employees.csv")
        if not employees:
            raise ValueError("Employee list is empty. Please check your input file.")

        print("Loading previous year’s assignments...")
        # Load the previous year's Secret Santa pairings
        previous_pairs = FileService.load_previous_assignments(
            "data/previous_assignments.csv"
        )

        print("Generating Secret Santa assignments...")
        # Create the assignment service and generate the new pairings
        service = AssignmentService(employees, previous_pairs)
        assignments = service.generate_assignments()

        print("Saving assignments to output file...")
        # Save the new assignments to a CSV file
        FileService.save_assignments(assignments, "output/secret_santa_output.csv")

        print("Secret Santa assignments completed successfully!")

    except FileNotFoundError as fnf:
        # Handle case where a file is missing
        print(f"File not found: {fnf.filename}")
        sys.exit(1)
    except ValueError as ve:
        # Handle invalid value errors (e.g., empty employee list)
        print(f"Value Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
