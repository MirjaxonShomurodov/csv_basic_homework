import csv
def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   rows=data.split('\n')
   return list(rows)[1]

# Read the csv file
f=open('data.csv')
print(get_first_row(f.read()))