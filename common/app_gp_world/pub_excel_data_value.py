# -*- encoding=utf8 -*-

__author__ = "WLX"

import re
import xlrd

# excel操作
class PubExcelOperator:

    # 获取excel的值
    @staticmethod
    def get_excel_value(self):

        # 打开excel，只支持xls格式，xlsx不行
        wb = xlrd.open_workbook(r"E:\UI_Automation\UITestForBabybus_Translate\translate2.xls")
        # 取到sheet
        sheet = wb.sheet_by_index(0)
        excel_value = []
        # 17
        for i in range(1,17):
            # cell(行，列)
            one_data = sheet.cell(i, self)
            cell_value = one_data.value
            excel_value.append(cell_value)
        return excel_value


    # 获取excel最后3列 （必玩页的翻译）
    @staticmethod
    def get_excel_last2colum(self):

        # 打开excel，只支持xls格式，xlsx不行
        wb = xlrd.open_workbook(r"E:\UI_Automation\UITestForBabybus_Translate\translate2.xls")
        # 取到sheet
        sheet = wb.sheet_by_index(0)
        excel_value = []
        # 18-19
        for i in range(17,20):
            # cell(行，列)
            one_data = sheet.cell(i, self)
            cell_value = one_data.value
            excel_value.append(cell_value)
        return excel_value






