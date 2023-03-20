from openpyxl import Workbook
from openpyxl.styles import Font

wb = Workbook()
ws = wb.active
ws['A5'] = 9

cel = ws
cel = Font(size=12, bold=True, color="ff0000")
wb.save('output.xlsx')
