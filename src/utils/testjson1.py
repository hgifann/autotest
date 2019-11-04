__author__ = 'THTF'
# -*- coding: utf-8 -*-

import xlrd


filename=r'C:\Users\THTF\PycharmProjects\autotest4\data\test1.xlsx'
lista=[]


class Read_excel():
    # #逐行读取
    # def read_excel(self):
    #     wb = xlrd.open_workbook(filename=filename)#打开文件
    #     # print(wb.sheet_names())#获取所有表格名字
    #     #
    #     sheet1 = wb.sheet_by_index(0)#通过索引获取表格
    #     # print(sheet1)
    #     # sheet2 = wb.sheet_by_name('年级')#通过名字获取表格
    #     # print(sheet1,sheet2)
    #     # print(sheet1.name,sheet1.nrows,sheet1.ncols)
    #     #
    #     rows = sheet1.row_values(2)#获取行内容
    #     print(rows)
    #     # cols = sheet1.col_values(3)#获取列内容
    #     # print(rows)
    #     # print(cols)
    #     # #
    #     # print(sheet1.cell(1,0).value)#获取表格里的内容，三种方式
    #     # print(sheet1.cell_value(1,0))
    #     # # print(sheet1.row(1)[0].value)
    #     #取表的第几行
    #     dataset1=sheet1.row_values(2)
    # # # print(dataset1)
    # # # print(dataset1[0])
    #     usrdict={
    #     "url":dataset1[0],
    #     "service":dataset1[1],
    #     "username":dataset1[2],
    #     "password":dataset1[3],
    #     "is_allow_many":dataset1[4],
    #     "app_key":dataset1[5]}
    #     # print(app_key)
    #     # print(dataset1)
    #     # print(username)
    #     return usrdict
    # =======================================================================
    #读取所有行
    def read_excel(self,filename=filename):
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_name('Sheet1')
        rows = sheet.nrows #获取行数
        # print(rows)

        cols = sheet.ncols #获取列数
        # print(rows,cols)
        # for c in range(cols): #读取每一列的数据
        #     c_values = sheet.col_values(c)
        #     print(c_values)
        for r in range(1,rows): #读取每一行的数据
            r_values = sheet.row_values(r)
            # print(r_values)
            # print(r_values)
            # if r_values
            lista.append(r_values)
            # print(lista)
        return lista

#
# a=Read_excel().read_excel()
# # print("=====")
# print(lista)