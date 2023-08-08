import csv
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    rows=data.split('\n')
    first_row=rows[2].split(',')
    return len(first_row)

# Read the csv file
f=open('data.csv')
print(find_number_of_columns(f.read())) 