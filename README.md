# Security Benchmarking Tool
> It's a desktop application which works with cyber security audit policies - which allows configuration of a system’s vulnerability to different attacks and enforce certain security
configurations based on community best practices.

## Table of contents

* [Technologies](#technologies)
* [How to use](#how-to-use)
* [Code examples](#code-examples)
* [Features](#features)
* [Lab1 Feature](#lab1-feature)
* [Lab2 Feature](#lab2-feature)
* [Team](#team)
* [Status](#status)

## Technologies
Python3 and Tkinter  
Working IDE: PyCharm

## How to use
1. Run gui.py
2. Click on download button to get the audits from file(for 1st time usage)
3. Click import to select the needed audit file
4. Select configurations which you need
5. Save the desired selections(it will automatically save as .audit file)

## Code Examples
Lines from function for computing audit structure:
```
for n in range(len(lines)):
if regexes['open'].match(lines[n]):
    finds = regexes['open'].findall(lines[n])
    # audit.append(("TAG", lines[n]))
    stack.append(finds[0])
    record = {}
elif regexes['close'].match(lines[n]):
    finds = regexes['close'].findall(lines[n])
    if len(stack) == 0:
        msg = 'Ran out of stack closing tag: {} (line {})'
        display(msg.format(finds[0], n), exit=1)
    elif finds[0] == stack[-1]:
        stack = stack[:-1]
```
Lines from function for importing audit:

```
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

import_button = Button(frame, text="Import", width=7, height=1, command=import_audit).place(x=10, y=510)
```

## FEATURES
## Lab1 Feature 
• Import the manually downloaded policies from a predefined trusted location  
• Parse and understand the format of data within the imported policy  
• Save the same set of policies under a different name within a structured form (ex:database).    
## Lab2 Feature
• Choose which options they would like to run (by selecting or deselecting options)  
• Search by name for an option (via a search bar)  
• Select or deselect all options in one click  
• Create and save a policy that contains only the selected options under the same name or a different one.  

## Team

> FAF - 182

| <a href="https://github.com/DivineBee" target="_blank">**Vizant Beatrice**</a> | <a href="https://github.com/whysoserious97" target="_blank">**Lesco Andrei**</a>
| :---: |:---:|
| [![Vizant Beatrice](https://avatars0.githubusercontent.com/u/49019844?s=200&u=b232b6a4e7d387d304f0b7938eabe6cf742bacb8&v=4)](http://github.com/DivineBee)    | [![Lesco Andrei](https://avatars2.githubusercontent.com/u/53511833?s=200&u=4b5de9bd5272530cf96b9d5a174dc6af3e3ecbf0&v=4)](//github.com/whysoserious97) |
| <a href="//github.com/DivineBee" target="_blank">`github.com/DivineBee`</a> | <a href="http://github.com/whysoserious97" target="_blank">`github.com/whysoserious97`</a> |


## Status
Project is: _in progress_
