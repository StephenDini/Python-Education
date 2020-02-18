import pandas
from pathlib import Path

location = "Financial Sample.xlsx"
wb =  pandas.read_excel(location)
test1 = wb['Segment']
writer = pandas.ExcelWriter("output.xlsx", engine="xlsxwriter")
# print(wb["Government"])
print(wb.columns.ravel())
holder = pandas.DataFrame(wb.columns.ravel())
print(holder)
# print(test1)
counter = 0
# newSheet = wb.header()
# print(newSheet)
for i in wb['Segment']:
    if (i == 'Government'):
        holder.append(wb.iloc[counter])
    counter += 1
print(holder)