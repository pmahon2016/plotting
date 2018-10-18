import matplotlib.pyplot as myplot
import openpyxl

wb = openpyxl.load_workbook("MicrosoftClose.xlsx")
wbFB = openpyxl.load_workbook("FBclose.xlsx")
sheet = wb.active
sheetFB = wbFB.active

sheet.delete_rows(1), sheetFB.delete_rows(1)
my_close_list = [int(col.value) for col in sheet["E"] ]
my_dates_list = [col.value for col in sheet["A"] if col ]
fb_close = [int(col.value) for col in sheetFB["E"] ]

myplot.plot(my_dates_list,my_close_list, c = "red")
myplot.plot(my_dates_list,fb_close, c = "blue")
myplot.xlabel("Last 30 Days", fontsize = 16)
myplot.ylabel("Closing Price", fontsize = 16)

myplot.show()

# for i in my_close_list:
#     print(i)
