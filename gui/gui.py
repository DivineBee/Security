import glob
import tarfile
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import requests
import view_audit_structure

global previous

main = Tk()
main.title("Controls Choice List")
main.geometry("1620x575")
frame = ttk.Frame(main, padding=(4, 4, 16, 16))
frame.grid(column=0, row=0)
previous = []
index = 0

arr = []
valori = StringVar()
tofile = []  # the array of configurations to be send to file


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
    for key in structure[index]:
        str += key + ':' + structure[index][key] + '\n'
    text.insert(END, str)


def import_audit():
    file_name = fd.askopenfilename(initialdir="../portal_audits")  # ../portal_audits/Windows
    global structure
    structure = view_audit_structure.main(file_name)

    for struct in structure:
        if 'description' in struct:
            arr.append(struct['description'])
        else:
            arr.append('Error in selecting')
    valori.set(arr)


lstbox = Listbox(frame, bg="#e6fffa", listvariable=valori, selectmode=MULTIPLE, width=130, height=25)
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
        tofile.append(structure[i])
    file.write(str(tofile))
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
    url="https://www.tenable.com/downloads/api/v1/public/pages/download-all-compliance-audit-files/downloads/7472/download?i_agree_to_tenable_license_agreement=true"
    path="audits.tar.gz"
    download_url(url,path)
    tf = tarfile.open("audits.tar.gz")
    tf.extractall()
    print(glob.glob("portal_audits/*"))


text = Text(frame, bg="#fffffa", width=50, height=27.5)
text.grid(row=0, column=3, columnspan=3, padx=30)
import_button = Button(frame, text="Import", width=7, height=1, command=import_audit).place(x=10, y=510)  # y was 435
openButton = Button(frame, text="Save", width=7, height=1, command=save_config).place(x=80, y=510)
selectAllButton = Button(frame, text="Select All", width=7, height=1, command=select_all).place(x=150, y=510)
deselectAllButton = Button(frame, text="Deselect All", width=10, height=1, command=deselect_all).place(x=220, y=510)
downloadButton = Button(frame, text="Download audits", width=15, height=1, command=extract_download).place(x=310, y=510)

main.mainloop()
