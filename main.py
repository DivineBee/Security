import requests
#import inquirer

import tarfile
import glob

import os


def download_url(url, save_path, chunk_size=1024):
    r = requests.get(url, stream=True)
    with open(save_path, 'wb') as fd:
        for chunk in r.iter_content(chunk_size=chunk_size):
            fd.write(chunk)


url="https://www.tenable.com/downloads/api/v1/public/pages/download-all-compliance-audit-files/downloads/7472/download?i_agree_to_tenable_license_agreement=true"
path="audits.tar.gz"

download_url(url,path)

tf = tarfile.open("audits.tar.gz")
tf.extractall()
print(glob.glob("portal_audits/*"))
# -------
my_path = "portal_audits"
paths = glob.glob(my_path + '/**/*.audit', recursive=True)
print(paths)
files = []
for path in paths:
    print(path.rfind("\\"))
    files.append(path[path.rfind("\\") + 1:len(path)])
print(files)
print(paths[0])
# --------

f = open("menuoptions.txt", "r")
print(f.read())

# function for menu options
# user input for dir
# verify input (register independent)
# to make provodnik gui

path = os.walk('portal_audits')

for root, directories, files in path:
    for directory in directories:
        directory_folders = []
        count = 1
        for i in range(count):
            directory_folders.append(directory)
            count += 1
        print(directory_folders)
        # questions = [
        #     inquirer.List('directory_folders',
        #                   message="Choose audit policy ",
        #                   choices=directory_folders,
        #                   ),
        # ]
        # answers = inquirer.prompt(questions)


def menu():
    choice = input()

    if choice == "1":
        rootDir = 'portal_audits/Adtran'
        fname = "Adtran"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()

    if choice == "2":
        rootDir = 'portal_audits/Alcatel'
        fname = "Alcatel"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                # add to array
                print('\t%s' % fname)
        menu()

    if choice == "3":
        rootDir = 'portal_audits/amazon_aws'
        fname = "amazon_aws"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()

    if choice == "4":
        rootDir = 'portal_audits/Arista'
        fname = "Arista"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()

    if choice == "5":
        rootDir = 'portal_audits/AS400'
        fname = "AS400"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()
    if choice == "6":
        rootDir = 'portal_audits/BlueCoat'
        fname = "BlueCoat"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()

    if choice == "7":
        rootDir = 'portal_audits/Brocade'
        fname = "Brocade"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()

    if choice == "8":
        rootDir = 'portal_audits/Windows'
        fname = "Windows"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()
    if choice == "9":
        rootDir = 'portal_audits/WindowsFileAnalysis'
        fname = "WindowsFileAnalysis"
        for dirName, subdirList, fileList in os.walk(rootDir):
            for fname in fileList:
                print('\t%s' % fname)
        menu()

        # Remove the first entry in the list of sub-directories
        # if there are any sub-directories present


menu()
# os.system("python view_audit_structure.py "+paths[0])
