import openpyxl

path = "C:\\Users\\Saurabh\\Desktop\\saurabh1.xlsx"

workbook = openpyxl.load_workbook(path)
sheet = workbook.active

for r in range(1, 5):
    for c in range(1, 8):
        sheet.cell(row=r, column=c).value = "saurabh"

workbook.save(path)
