# -*- coding: latin -*-
from openpyxl import load_workbook,Workbook
import os,sys,re,csv

def reading(planilha):
    print(planilha)
    data = {}
    wb = load_workbook(filename=planilha)
    ws = wb.active
    for r in range(4,ws.max_row):
        for c in range(1,ws.max_column):
            if ws.cell(row=r,column=c).value is not None:
                # print(ws.cell(row=r,column=c).value)
                # print('coluna 1 {},'.format(ws.cell(row=r,column=1).value))
                # print('coluna 2 {}'.format(ws.cell(row=r,column=2).value))
                # print('coluna 9 {}'.format(ws.cell(row=r,column=9).value))
                nome = ws.cell(row=r,column=1).value
                cidade = ws.cell(row=r,column=2).value
                comprador = ws.cell(row=r,column=9).value
                # data.append[({'nome':nome,'cidade':cidade,'comprador':comprador})]
                print('dados {}'.format(data))
    return planilha