import pandas as pd

def print_excel_data(file_path, sheet_name=None):
    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    
    # Print the data in tabular format
    print(df.to_string(index=False))

# Example usage
file_path = 'example.xlsx'  # Replace with your Excel file path
sheet_name = 'Sheet1'       # Replace with your sheet name (or None for the first sheet)

print_excel_data(file_path, sheet_name)
