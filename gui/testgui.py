from tkinter import *
from tkinter import filedialog as fd


def insertText():
    file_name = fd.askopenfilename(initialdir="B:\\PROG\\PROJECTS\\PYTHON\\Security\\portal_audits")
    f = open(file_name)
    s = f.read()
    text.insert(1.0, s)
    f.close()


def extractText():
    file_name = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"),
                                                ("All files", "*.*")))
    f = open(file_name, 'w')
    s = text.get(1.0, END)
    f.write(s)
    f.close()


root = Tk()
text = Text(width=50, height=25)
text.grid(columnspan=2)
b1 = Button(text="Открыть", command=insertText)
b1.grid(row=1, sticky=E)
b2 = Button(text="Сохранить", command=extractText)
b2.grid(row=1, column=1, sticky=W)

root.mainloop()