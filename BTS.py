import requests 
import tarfile
from tkinter import *
import xml.etree.ElementTree as ET
import glob

#ALPHA Version to try
import argparse
import datetime
import re
import sys
import os


def download_url(url, save_path, chunk_size=1024):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)
def acceptDownload():
    download_url(url, path)
    tf = tarfile.open("audits.tar.gz")
    tf.extractall()
    go_next()

def dennyDownload():
    go_next()

def go_next():
    my_path="portal_audits"
    paths = glob.glob(my_path + '/**/*.audit', recursive=True)
    #print(paths)
    files=[]
    for path in paths:
        #print(path.rfind("\\"))
        files.append(path[path.rfind("\\")+1:len(path)])
    #print(files)
    #print(paths[0])
    tosend=files.index(sys.argv[1]) #BSI_100_2_Windows_v1.0.audit
    root.destroy()
    os.system("python view_audit_structure.py "+paths[tosend])


url="https://www.tenable.com/downloads/api/v1/public/pages/download-all-compliance-audit-files/downloads/7472/download?i_agree_to_tenable_license_agreement=true"
path="audits.tar.gz"
root=Tk()
label=Label(text='Do you want to download the most recent version of audits?',font=('Arial',14))
label.pack()
#root.geometry('50x20')
but1=Button(text='YES',command=acceptDownload,bg='green')
but1.config(height=20,width=50)
but1.pack(side=LEFT)
but2=Button(text='NO',command=dennyDownload,bg='red')
but2.config(height=20,width=50)
but2.pack(side=RIGHT)
root.mainloop()

#print(glob.glob("portal_audits/*"))

