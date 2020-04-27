# -*- coding: UTF-8 -*-

from PyPDF2 import PdfFileReader, PdfFileWriter
import os
from tkinter import *
import tkinter.filedialog
root = Tk()
root.resizable(False, False)
root.title('电子发票合并')

import sys  
reload(sys)  
sys.setdefaultencoding('utf8')   

files_list = []
outfile = "Cheat_Sheets.pdf"

def select():
    filenames = tkinter.filedialog.askopenfilenames(filetypes=[("PDF",".pdf")])
    # print filenames
    if len(filenames) != 0:
        string_filename = ""
        for i in range(0,len(filenames)):
            string_filename += str(filenames[i])+"\n"
        lb.config(text = string_filename)
        global files_list
        files_list = filenames
    else:
        lb.config(text = "没有选择任何文件")

def MergePDF():
    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = files_list

    if pdf_fileName:
        for pdf_file in pdf_fileName:
            # print("路径：%s"%pdf_file)

            # 读取源PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))

            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            # print("页数：%d"%pageCount)

            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                PageObj = input.getPage(iPage)
                if PageObj.mediaBox[2] > 650:
                    PageObj.scaleTo(610,394)
                output.addPage(PageObj)

        # print("合并后的总页数:%d."%outputPages)
        # 写入到目标PDF文件
        outputStream = open(outfile, "wb")
        output.write(outputStream)
        outputStream.close()
        # print("PDF文件合并完成！")
        os.popen(outfile)
        

def on_closing():
    if os.path.exists(outfile):
        os.remove(outfile)
    root.destroy()

lb = Label(root,text = '')
lb.pack()
btn1 = Button(root,text="选择电子发票",command=select)
btn2 = Button(root,text="合并并打开",command=MergePDF)
btn1.pack()
btn2.pack()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
