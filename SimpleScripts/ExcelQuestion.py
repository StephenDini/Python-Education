# Using pandas to read the Data and openpyxl's workbook to
# create a new book and save this to a new excel file.

import pandas
import pprint
from openpyxl import Workbook

# File in the same folder.
location = "Financial Sample.xlsx"

# Read in data from file
wb = pandas.read_excel(location)

# Create a new workbook and activate it
book = Workbook()
holder = book.active
holder.title = ('Test')

# location of values
counter = 0


# using a for loop and if statements to append data to the workbook
for i in wb['Segment']:
    if (i == 'Government'):
        holder.append(wb.iloc[counter].values.tolist())
    counter += 1

# Save the file
book.save(filename="output.xlsx")