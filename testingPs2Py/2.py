import sys , openpyxl, os, csv
os.chdir('C:\\MyGit\\Python\\MyPython\\testingPs2Py')

wb = openpyxl.Workbook()
sheet = wb['Sheet']


i = 1

with open('psCsv.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        
        ###########
        sheet.cell(row=i,column=1).value = row[1]
        sheet.cell(row=i,column=2).value = row[0]
        sheet.cell(row=i,column=3).value = row[2]
        ###########
        i +=1


wb.save('Services.xlsx')