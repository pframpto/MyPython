import sys , openpyxl, os


#print(sys.argv[1], sys.argv[2],sys.argv[3], str(sys.argv[4]))

os.chdir('C:\\MyGit\\Python\\MyPython\\testingPs2Py')

wb = openpyxl.Workbook()
sheet = wb['Sheet']
sheet['a1'] = 'Status'
sheet['b1'] = 'Name'
sheet['c1'] = 'Display Name'
nrow = int(sys.argv[4])

sheet.cell(row=nrow,column=1).value = str(sys.argv[1])
sheet.cell(row=nrow,column=2).value = str(sys.argv[2])
sheet.cell(row=nrow,column=3).value = str(sys.argv[3])


wb.save('Services.xlsx')

#print(i, sheet.cell(row=i, column=2).value)