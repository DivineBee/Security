# -*- coding: utf-8 -*-
import glob
import json
import os
import subprocess
import tarfile
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk
from tkinter.font import Font
import requests
import view_audit_structure
import re

global previous
main = Tk()
myFont = Font(family="Century Gothic", size=12)
s = ttk.Style()
s.configure('TFrame', background='#03161d')
main.title("SBT - Security Benchmarking Tool")
main.geometry("1720x700")
frame = ttk.Frame(main, width=1720, height=800, style='TFrame', padding=(4, 4, 200, 200))
frame.grid(column=0, row=0)
previous = []
index = 0
arr = []  # items selected
matching = []
SystemDict = {}
querry = StringVar()
valori = StringVar()
tofile = []  # the array of configurations to be send to file
structure = []


def check():
    success = []
    fail = []
    unknown = []
    print('Here')
    path = os.getcwd()
    print(path)
    out = subprocess.Popen(['secedit.exe', '/export', '/cfg', path + '\\security.txt'],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.STDOUT)
    output = out.communicate()[0]

    print('Output:', output.decode('ascii', 'ignore'))
    # os.system('secedit.exe /export /cfg '+path+'\\security.txt')
    file = open('security.txt', 'r')
    input = file.read()
    san = ""
    for i in input:
        if i.isprintable() or i.isspace():
            san += i
    san = san.split('\n')
    san = [x for x in san if len(x) > 0]

    # print(san)
    for str in san:
        if '=' in str:
            to_add = str[str.index('=') + 1:]
            key_to_add = str[:str.index('=')]
            resultvalue = ''
            resultkey = ''
            for char in to_add:
                if char != ' ':
                    resultvalue += char
            for char in key_to_add:
                if char != ' ':
                    resultkey += char
            SystemDict[resultkey] = resultvalue
    print(SystemDict)
    print(structure)

    for struct in structure:
        if 'reg_key' in struct and 'reg_item' in struct and 'value_data' in struct:
            query = 'reg query ' + struct['reg_key'] + ' /v ' + struct['reg_item']
            out = subprocess.Popen(query,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
            output = out.communicate()[0].decode('ascii', 'ignore')
            str = ''
            for char in output:
                if char.isprintable() and char != '\n' and char != '\r':
                    str += char
            output = str
            output = output.split(' ')
            output = [x for x in output if len(x) > 0]
            value = ''
            if 'ERROR' in output[0]:
                unknown.append(struct['reg_key'] + struct['reg_item'])
            for i in range(len(output)):
                if 'REG_' in output[i]:
                    for element in output[i + 1:]:
                        value = value + element + ' '
                    value = value[:len(value) - 1]  # last space we delete
                    # print('Value',value)
                    p = re.compile('.*' + struct['value_data'] + '.*')
                    if p.match(value):
                        print('Patern:', struct['value_data'])
                        print('Value:', value)
                        success.append(struct['reg_key'] + struct['reg_item'] + '\n' + 'Value:' + value)
                    else:
                        print('Did not pass: ', struct['value_data'])
                        print('Value which did not pass: ', value)
                        fail.append(
                            struct['reg_key'] + struct['reg_item'] + '\n' + 'Actual:' + value + '\n' + 'Expected:' +
                            struct['value_data'])

    file.close()
    frame2 = Frame(main, bd=10, bg='#03161d', highlightthickness=3)
    frame2.config(highlightbackground="white")
    frame2.place(relx=0.5, rely=0.1, width=800, relwidth=0.4, relheight=0.8, anchor='n')

    text2 = Text(frame2, bg="#afca54", width=50, height=27.5, highlightthickness=3)
    text2.place(relx=0.07, rely=0.03, relwidth=0.4, relheight=0.9)
    text2.insert(END, '\n\n'.join(success))

    listbox_fail = Listbox(frame2, bg="#e45149", font=myFont, fg="white", listvariable=valori, selectmode=MULTIPLE,
                           width=50, height=27, highlightthickness=3)
    listbox_fail.place(relx=0.5, rely=0.03, relwidth=0.4, relheight=0.9)
    listbox_fail.config(highlightbackground="white")
    listbox_fail.bind('<<ListboxSelect>>', on_select_failed)

    def exit():
        frame2.destroy()

    exit_btn = Button(frame2, text='Close', command=exit, bg="#03161d", fg="white", font=myFont, padx='10px',
                      pady='3px')
    exit_btn.place(relx=0.46, rely=0.95)

#change contents
def on_select_failed(evt):
    global previous
    global index
    w = evt.widget
    actual = w.curselection()

    difference = [item for item in actual if item not in previous]
    if len(difference) > 0:
        index = [item for item in actual if item not in previous][0]
    previous = w.curselection()

    text.delete(1.0, END)
    str = '\n'
    for key in matching[index]:
        str += key + ':' + matching[index][key] + '\n'
    text.insert(END, str)


def entersearch(evt):
    search()


def search():
    global structure
    q = querry.get()
    arr = [struct['description'] for struct in structure if q.lower() in struct['description'].lower()]
    global matching
    matching = [struct for struct in structure if q in struct['description']]
    valori.set(arr)


def on_select_configuration(evt):
    global previous
    global index
    w = evt.widget
    actual = w.curselection()

    difference = [item for item in actual if item not in previous]
    if len(difference) > 0:
        index = [item for item in actual if item not in previous][0]
    previous = w.curselection()

    text.delete(1.0, END)
    str = '\n'
    for key in matching[index]:
        str += key + ':' + matching[index][key] + '\n'
    text.insert(END, str)


def import_audit():
    global arr
    file_name = fd.askopenfilename(initialdir="../portal_audits")  # ../portal_audits/Windows
    if file_name:
        arr = []
    global structure
    structure = view_audit_structure.main(file_name)
    for element in structure:
        for key in element:
            str = ''
            for char in element[key]:
                if char != '"' and char != "'":
                    str += char
            isspacefirst = True
            str2 = ''
            for char in str:
                if char == ' ' and isspacefirst:
                    continue
                else:
                    str2 += char
                    isspacefirst = False
            element[key] = str2

    global matching
    matching = structure
    if len(structure) == 0:
        f = open(file_name, 'r')
        structure = json.loads(f.read())
        f.close()
    for struct in structure:
        if 'description' in struct:
            arr.append(struct['description'])
        else:
            arr.append('Error in selecting')
    valori.set(arr)


lstbox = Listbox(frame, bg="#4996b3", font=myFont, fg="white", listvariable=valori, selectmode=MULTIPLE, width=130,
                 height=25, highlightthickness=3)
lstbox.config(highlightbackground="white")
lstbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
lstbox.bind('<<ListboxSelect>>', on_select_configuration)


# Saving file with desired configurations
def save_config():
    file_name = fd.asksaveasfilename(filetypes=(("Audit FILES", ".audit"),
                                                ("All files", ".")))
    file_name += '.audit'
    file = open(file_name, 'w')
    selection = lstbox.curselection()
    for i in selection:
        # file.write(str(tofile))
        tofile.append(matching[i])
    json.dump(tofile, file)
    # file.write(str(tofile))
    file.close()


def select_all():
    lstbox.select_set(0, END)
    for struct in structure:
        lstbox.insert(END, struct)


def deselect_all():
    for struct in structure:
        lstbox.selection_clear(0, END)


def download_url(url, save_path, chunk_size=1024):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


def extract_download():
    url = "https://www.tenable.com/downloads/api/v1/public/pages/download-all-compliance-audit-files/downloads/7472/download?i_agree_to_tenable_license_agreement=true"
    path = "audits.tar.gz"
    download_url(url, path)
    tf = tarfile.open("audits.tar.gz")
    tf.extractall()
    print(glob.glob("portal_audits/*"))


text = Text(frame, bg="#bc4f07", fg="white", font=myFont, width=50, height=26, highlightthickness=3)
text.config(highlightbackground="white")
text.grid(row=0, column=3, columnspan=3, padx=30)
import_button = Button(frame, bg="#bc4f07", fg="white", font=myFont, text="Import", width=7, height=1,
                       command=import_audit).place(relx=0.01, rely=0.999)  # y was 435
openButton = Button(frame, bg="#bc4f07", fg="white", font=myFont, text="Save", width=7, height=1,
                    command=save_config).place(relx=0.06, rely=0.999)
selectAllButton = Button(frame, bg="#bc4f07", fg="white", font=myFont, text="Select All", width=7, height=1,
                         command=select_all).place(relx=0.11, rely=0.999)
deselectAllButton = Button(frame, bg="#bc4f07", fg="white", font=myFont, text="Deselect All", width=10, height=1,
                           command=deselect_all).place(relx=0.16, rely=0.999)
downloadButton = Button(frame, bg="#bc4f07", fg="white", font=myFont, text="Download audits", width=15, height=1,
                        command=extract_download).place(relx=0.227, rely=0.999)
global e
e = Entry(frame, bg="#ffe4d1", font=myFont, width=30, textvariable=querry).place(relx=0.325, rely=0.999)
search_button = Button(frame, bg="#4996b3", fg="white", font=myFont, text="Search", width=7, height=1,
                       command=search).place(relx=0.49, rely=0.999)
check_button = Button(frame, bg="#bc4f07", fg="white", font=myFont, text="Check", width=7, height=1,
                      command=check).place(relx=0.54, rely=0.999)
main.bind('<Return>', entersearch)
main.mainloop()
