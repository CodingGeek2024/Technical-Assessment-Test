import csv
import re

def is_valid_email(email):
    # Simple email validation regex pattern
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def clean_csv_data(input_file, output_file):
    # Dictionary to store unique user entries
    unique_users = {}

    # Read the input CSV file
    with open(input_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        for row in reader:
            user_id = row['user_id']
            email = row['email']

            # Check if the email is valid
            if is_valid_email(email):
                # If the user_id is not in the dictionary or the current row has a valid email
                if user_id not in unique_users or is_valid_email(unique_users[user_id]['email']):
                    unique_users[user_id] = row

    # Write the cleaned data to the output CSV file
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in unique_users.values():
            writer.writerow(row)

    print(f"Cleaned data has been written to {output_file}")

# Example usage
input_file = 'user_data.csv'
output_file = 'cleaned_user_data.csv'
clean_csv_data(input_file, output_file)