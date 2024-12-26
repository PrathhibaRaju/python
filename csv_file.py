import csv

def calculate_average(file_path, column_name):
    total = 0
    count = 0

    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert the value to a float and add to the total
                total += float(row[column_name])
                count += 1

        if count == 0:
            raise ValueError("No data found in the specified column.")

        average = total / count
        return average

    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except KeyError:
        print(f"The column '{column_name}' does not exist in the file.")
    except ValueError as e:
        print(f"Error: {e}")

# Example usage
file_path = "data.csv"  # Replace with your CSV file path
column_name = "value"  # Replace with the column name you want to average

average_value = calculate_average(file_path, column_name)
if average_value is not None:
    print(f"The average of the values in the column '{column_name}' is {average_value:.2f}.")
