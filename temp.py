import matplotlib.pyplot as myplot
import openpyxl

wb = openpyxl.load_workbook("sandp.xlsx")

wb1 = openpyxl.load_workbook("MicrosoftClose.xlsx")

mysheet = wb.active
mysheet1 = wb1.active

mysheet1.delete_rows(1), mysheet.delete_rows(1)
my_close_list = [int(col.value) for col in mysheet["E"] ]

for i in my_close_list:
    print(i)

my_dates_list = [col.value for col in mysheet["A"] if col ]

ms_close_list = [int(col.value) for col in mysheet1["E"] if col ]



myplot.plot(my_dates_list,my_close_list, c = "red")

#myplot.plot(my_dates_list, ms_close_list, c = "green")
#
myplot.show()

#
# for i in ms_close_list:
#
#     print(i)
#
# print("divide")
#
# for i in my_close_list:
#     print(i)

