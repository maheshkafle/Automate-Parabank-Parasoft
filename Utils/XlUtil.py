import openpyxl
import xlsxwriter

def filecreate(filename):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet()
    workbook.close()

def writetoxl(filepath,sheetname,rownum,colnum,data):
    Workbook = openpyxl.load_workbook(filepath)
    Sheet = Workbook.get_sheet_by_name(sheetname)
    Sheet.cell(rownum,colnum).value = data
    Workbook.save(filepath)