import csv
# Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    rows=data.split('\n')
    first_row=rows[0].split(',')
    return list(rows)[1]

# Read the csv file
f=open('data.csv')
print(get_column_names(f.read()))