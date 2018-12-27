from tkinter import *
from MyQR import myqr
import sys
import os
import tkinter.messagebox as messagebox
import tkinter.commondialog
import tkinter.filedialog
from  tkinter  import ttk

class TKdemo():
    def __init__(self):
        master = Tk()
        master.title("可以转换动态二维码的小工具")
        # 问题1放在frame1中 (Frame)
        frame1 = Frame(master)
        frame1.pack(fill=X)
        # 问题
        label11 = Label(frame1, text='1,请选择你要转换的文件：')
        label11.grid(row=1, column=0)
        # 按钮  (Button)
        self.filename = StringVar()
        getname = Button(frame1, text='选择', command=self.getfile)
        getname.grid(row=1, column=1)
        self.label1 = Label(frame1, text='')
        self.label1.grid(row=1, column=0)

        frame2 = Frame(master)
        frame2.pack(fill=X)
        label2 = Label(frame2, text='2,请选择你要转换的文本内容：')
        label2.grid(row=2, column=0)
        # 输入框 (Entry)
        self.name = StringVar()
        entryname = Entry(frame2, textvariable=self.name)
        entryname.grid(row=2, column=1)

        frame3 = Frame(master)
        frame3.pack(fill=X)
        # 问题
        label3 = Label(frame3, text='3,请选择是否需要彩色：')
        label3.grid(row=3, column=0)
        # 选择按钮 (Radiobutton)
        self.sex = BooleanVar()
        sex_male = Radiobutton(frame3, text='彩色', fg='blue', variable=self.sex, value=True)
        sex_male.grid(row=3, column=1)
        sex_female = Radiobutton(frame3, text='黑白', fg='black', variable=self.sex, value=False)
        sex_female.grid(row=3, column=2)

        frame4 = Frame(master)
        frame4.pack(fill=X)
        # 问题
        label4 = Label(frame4, text='4,请选择边长：')
        label4.grid(row=0, column=0)
        # 滑动条 (Scale)
        self.age = Scale(frame4, from_=1, to=40, orient=HORIZONTAL, resolution=1)   # 默认垂直
        self.age.grid(row=0, column=1)

        frame5 = Frame(master)
        frame5.pack(fill=X)
        label5 = Label(frame5, text='5,请选择纠错水平：')
        label5.grid(row=0, column=0)
        self.comvalue = StringVar()
        comboxlist =ttk.Combobox(frame5, textvariable=self.comvalue)  # 初始化
        comboxlist["values"] = ("L", "M", "H", "Q")
        comboxlist.current(0)
        comboxlist.grid(row=0,column=1)

        frame6 = Frame(master)
        frame6.pack()
        submit = Button(frame6, text='转换', command=self.get_all)
        submit.grid()
        master.mainloop()

    def getfile(self):
        self.filename = tkinter.filedialog.askopenfilename()
        if self.filename != '':
            self.label1.config(text="您选择的文件是：" + self.filename);
        else:
            self.label1.config(text="您没有选择任何文件");
    def get_all(self):
        level =self.comvalue.get()
        words = self.name.get()
        version = self.age.get()
        picture = self.filename
        colorize = self.sex.get()
        print(colorize)
        version, level, qr_name = myqr.run(
            words,
            version=version,
            level=level,
            picture=picture,
            colorized=colorize,
            contrast=1.0,
            brightness=1.0,
            save_name=None,
            save_dir=os.getcwd()
        )
        messagebox.showinfo("成功！","文件以转换成功并保存到了程序当前目录下")
TKdemo()
