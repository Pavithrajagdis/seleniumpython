#import openpyxl




class Testhomepagedata:

    data=[{"firstname":"pavithra","email":"pavi.eshwar05@gmail.com","Pwd":"python","gender":"Male"}]

    @staticmethod
    def getTestdata(test_case_name):   #static methods will not have self parameter
        Dict = {}
        #book = openpyxl.load_workbook("C:\\Users\\pavij\\Documents\\pythondemo.xlsx")
        #sheet = book.active
        #for i in range(1, sheet.max_row + 1):
         #   if sheet.cell(row=i, column=1).value == "test_case_name":
          #      print(sheet.cell(row=i, column=1).value)
           #     for j in range(2, sheet.max_column + 1):
            #        Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value
        #return[Dict]