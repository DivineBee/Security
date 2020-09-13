from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import view_audit_structure
global previous
def onselect(evt):
    global previous
    global index
    #print('CLicked')
    w = evt.widget
    #print(evt)
    #set_on_click=set(w.get())
    #print(set_on_click)
    actual = w.curselection()

    difference = [item for item in actual if item not in previous]
    if len(difference)>0:
        index=[item for item in actual if item not in previous][0]
    previous=w.curselection()

    text.delete(1.0,END)
    str='\n'
    for key in structure[index]:
        str+=key+':'+structure[index][key]+'\n'
    #str+='}'
    text.insert(END,str)

main = Tk()
main.title("Controls Choice List")
main.geometry("1250x475")
frame = ttk.Frame(main, padding=(4, 4, 16, 16))
frame.grid(column=0, row=0)
previous=[]
index=0


arr=[]
valori = StringVar()
tofile=[] # the array of configurations to be send to file
def import_func():
    file_name = fd.askopenfilename(initialdir="portal_audits/Windows") #../portal_audits
    global structure
    structure = view_audit_structure.main(file_name)

    for struct in structure:
        # if 'info' in struct:
        #     arr.append(struct['info'])
        if 'description' in struct:
            arr.append(struct['description'])
        else:
            arr.append('Error in selecting')
    valori.set(arr)
    # f = open(file_name)
    # s = f.read()
         #text.insert(1.0, structure)
    #f.close()

# file_name parsezi ca argument la view_audit structure
# dupa parsare primim lista cu care vom lucra mai departe
# un exemplu simplu de listbox ( in loc de limbaje vor fi setarile noastre)


lstbox = Listbox(frame, bg="#e6fffa", listvariable=valori, selectmode=MULTIPLE, width=130, height=25)
lstbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
lstbox.bind('<<ListboxSelect>>', onselect)

# pentru a o printa in forma de checklist este functia asta:
def print_console():
    reslist = list()
    seleccion = lstbox.curselection()
    for i in seleccion:
        tofile.append(structure[i])
        # entrada = lstbox.get(i)
        # reslist.append(entrada)
    # for val in reslist:
    #     print(val)

# functie de salvare a fileului, trebuie de gandit cum sa salveze doar continutul la ce e selectat
# poate pentru fileurile selectate de facut un array aparte si pe urma pe el de salvat ca file aparte
def save():
    file_name = fd.asksaveasfilename(filetypes=(("Audit FILES", "*.audit"),
                                                ("All files", ".")))
    f = open(file_name, 'w')

    seleccion = lstbox.curselection()
    for i in seleccion:
        tofile.append(structure[i])

    #s = text.get(1.0, END)
    f.write(str(tofile))
    f.close()

text = Text(frame, bg="#fffffa", width=50, height=27.5)
text.grid(row=0, column=3, columnspan=3, padx=30)
import_button = Button(frame, text="Import", width=7, height=1, command=import_func).place(x=10, y=435)
#import_button.grid(row=1, column=0, sticky=E)
openButton = Button(frame, text="Save", width=7, height=1, command=save).place(x=80, y=435)
#openButton.grid(width=15, height=2).place(x=10, y=30)
printButton = Button(frame, text="Print", width=7, height=1, command=print_console).place(x=150, y=435)
#printButton.grid(row=1, column=1, sticky=E)
main.mainloop()