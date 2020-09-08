# Security Benchmarking Tool
> It's a desktop application which works with cyber security audit policies - which allows configuration of a system’s vulnerability to different attacks and enforce certain security
configurations based on community best practices.

## Table of contents

* [Technologies](#technologies)
* [How to run](#how-to-run)
* [Code examples](#code-examples)
* [Features](#features)
* [Lab1 Feature](#lab1-feature)
* [Status](#status)

## Technologies
* Tech 1 - version 1.0
* Tech 2 - version 2.0
* Tech 3 - version 3.0

## How to run
1. First Select the audit you want to parse  
python BST.py BTS_100_2_Windows_v1.0.audit.
2. Select option from gui:  
To download new version or not

## Code Examples
Show examples of usage:
`

    def parse_args(parameters):
    global show_time, show_verbose

    parser = argparse.ArgumentParser(description=('Display audit structure'))

    parser.add_argument('-t', '--timestamp', action='store_true',
                        help='show timestamp on output')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='show verbose output')

    parser.add_argument('audit', type=str, nargs=1,
                        help='audit file to view')

    args = parser.parse_args(parameters)

    if args.timestamp:
        show_time = True
    if args.verbose:
        show_verbose = True

    args.audit = make_list(args.audit)[0]

    return args
`

## Features
List of features ready and TODOs for future development
* Python 3 and Tkinter

To-do list:
* Lab2
* Lab3
* ...

## Lab1 Feature
Objective of this lab is to find a set of policies suitable for the environment  
it will be working in (i.e. Win, Linux, MacOS etc.) and download them. Then to  
provide persisting the imported policies i.e. parsing and saving them locally   
into a structured form (ex: database). It should be possible to upload the same  
policies multiple times and save them locally under different custom names.  

Application should be able to:  
• Import the manually downloaded policies from a predefined trusted location;  
• Parse and understand the format of data within the imported policy;  
• Save the same set of policies under a different name within a structured form (ex:
database).  

## Status
Project is: _in progress_
