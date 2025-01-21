import csv

#i Step 1: Read users from CSV file
def read_users_from_csv(file_path):
    users = []
    # Open the CSV file for reading
    with open(file_path, 'r') as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)
        # Read each row in the CSV file and append it to the users list
        for row in reader:
            users.append(row)
    return users

# Step 2: Filter users by age
def filter_users_by_age(users, age_threshold=30):
    # Filter users who are 30 years of age and older
    filtered_users = [user for user in users if int(user['age']) >= age_threshold]
    return filtered_users

# Step 3: Write filtered users to a new CSV file
def write_users_to_csv(users, file_path):
    if not users:
        return
    
    # Get the fieldnames from the first user's keys
    fieldnames = users[0].keys()
    # Open the CSV file for writing
    with open(file_path, 'w', newline='') as file:
        # Create a CSV writer object
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Write the header row
        writer.writeheader()
        # Write the user rows
        writer.writerows(users)

# Example usage
file_path = 'users.csv'  # Replace with your file path

# Read users from the CSV file
users = read_users_from_csv(file_path)

# Filter users who are 30 years of age and older
filtered_users = filter_users_by_age(users)

# Write the filtered users to a new CSV file
write_users_to_csv(filtered_users, 'filtered_users.csv')

print("Filtered users have been written to 'filtered_users.csv'")