import os
import xlsxwriter
filename = []

#Setting up directory
os.chdir("C://Users//sumit4.singh//Documents//JBM")

#Creating a Blank Workbook
workbook = xlsxwriter.Workbook('FileListing.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})
worksheet.set_column(1, 1, 15)
# Write some data headers.
worksheet.write('A1', 'FilePath', bold)
worksheet.write('B1', 'Size', bold)
row = 1
col = 0

#Iterating all the files and there  size listing
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      filePath = os.path.join(root, name)
      size = str(((os.stat(filePath).st_size)/1024))
      print(filePath + ',' +str(size))
      #result = filePath + '' + str(size)
      worksheet.write_string(row, col, filePath)
      worksheet.write_string(row, col+1, size)
      row += 1
workbook.close()


